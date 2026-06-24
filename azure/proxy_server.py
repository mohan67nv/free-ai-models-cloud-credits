#!/usr/bin/env python3
"""
Local proxy server that bridges Cursor (or any OpenAI-compatible client) to Azure AI Foundry.
Uses your logged-in Azure identity (az login) to get bearer tokens automatically.

Usage:
    python proxy_server.py

Then in Cursor, configure a custom model provider:
    - Base URL: http://localhost:8080/v1
    - API Key:  any-value (required by Cursor but not used)
    - Model:    DeepSeek-V4-Pro
"""

import json
import os
import sys
import time
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# ========== CONFIGURATION ==========
ENDPOINT = os.environ.get(
    "AZURE_ENDPOINT",
    "https://YOUR-RESOURCE.services.ai.azure.com/openai/v1"
)
DEPLOYMENT_NAME = os.environ.get("AZURE_DEPLOYMENT", "DeepSeek-V4-Pro")
LISTEN_PORT = int(os.environ.get("PROXY_PORT", 8080))

# Cache token provider (tokens auto-refresh)
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default"
)

# ========== LOGGING ==========
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("proxy")


class ProxyHandler(BaseHTTPRequestHandler):
    """Minimal OpenAI-compatible proxy handler."""

    def do_POST(self):
        path = urlparse(self.path).path
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length > 0 else b"{}"

        try:
            request_data = json.loads(body) if body else {}
        except json.JSONDecodeError:
            self._send_error(400, "Invalid JSON body")
            return

        # Force the model name to our deployment
        if "model" not in request_data:
            request_data["model"] = DEPLOYMENT_NAME

        log.info("→ %s  model=%s  msgs=%d", path, request_data.get("model", "?"),
                 len(request_data.get("messages", [])))

        # Route to the right endpoint
        if path == "/v1/chat/completions":
            self._proxy_chat(request_data)
        elif path == "/v1/completions":
            self._proxy_chat(request_data)  # same endpoint for legacy completions
        elif path == "/v1/embeddings":
            self._proxy_generic(request_data, path)
        elif path == "/v1/models":
            self._list_models()
        else:
            self._proxy_generic(request_data, path)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/v1/models":
            self._list_models()
        elif path == "/" or path == "/health":
            self._send_json(200, {"status": "ok", "endpoint": ENDPOINT, "model": DEPLOYMENT_NAME})
        else:
            self._send_error(404, f"Not found: {path}")

    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        self.send_response(200)
        self._cors_headers()
        self.end_headers()

    # ---- internal helpers ----

    def _proxy_chat(self, data: dict):
        """Forward chat completion to Azure Foundry."""
        try:
            client = OpenAI(base_url=ENDPOINT, api_key=token_provider)
            result = client.chat.completions.create(**data)
            self._send_json(200, result.model_dump())
        except Exception as e:
            log.error("Chat error: %s", e)
            self._send_error(500, str(e))

    def _proxy_generic(self, data: dict, path: str):
        """Passthrough for non-chat endpoints."""
        self._send_error(501, f"Endpoint {path} not yet implemented on proxy")

    def _list_models(self):
        """Return a minimal model list so Cursor sees the available models."""
        self._send_json(200, {
            "object": "list",
            "data": [
                {
                    "id": DEPLOYMENT_NAME,
                    "object": "model",
                    "created": int(time.time()),
                    "owned_by": "azure-ai-foundry",
                }
            ],
        })

    def _send_json(self, status: int, data: dict):
        self.send_response(status)
        self._cors_headers()
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _send_error(self, status: int, message: str):
        self._send_json(status, {"error": {"message": message, "type": "proxy_error", "code": status}})

    def _cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")

    def log_message(self, format, *args):
        """Suppress default HTTP log — we use our own logger."""
        pass


def main():
    server = HTTPServer(("127.0.0.1", LISTEN_PORT), ProxyHandler)
    print(f"""
╔══════════════════════════════════════════════════════╗
║     Azure AI Foundry → Cursor Proxy                  ║
╠══════════════════════════════════════════════════════╣
║  Listening on : http://127.0.0.1:{LISTEN_PORT}             ║
║  Model        : {DEPLOYMENT_NAME}
║  Endpoint     : {ENDPOINT}
╠══════════════════════════════════════════════════════╣
║  Cursor settings:                                    ║
║    Base URL → http://127.0.0.1:{LISTEN_PORT}/v1            ║
║    API Key  → anything (e.g. "dummy")                ║
║    Model    → {DEPLOYMENT_NAME}
╚══════════════════════════════════════════════════════╝

Press Ctrl+C to stop.
""")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down proxy...")
        server.shutdown()


if __name__ == "__main__":
    main()