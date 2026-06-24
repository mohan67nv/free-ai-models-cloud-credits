#!/usr/bin/env python3
"""
Generate an Azure AI Services API key for direct access.
This key does NOT expire — use it like a regular OpenAI API key.

PREREQUISITES: az login
USAGE:         python get_api_key.py

For Cursor, VS Code, or any OpenAI-compatible client:
    Base URL → https://YOUR-RESOURCE.services.ai.azure.com/openai/v1
    API Key  → <output from this script>
    Model    → DeepSeek-V4-Pro
"""

import subprocess
import sys
import os

# 🔧 REPLACE these with YOUR values from Azure portal
RESOURCE_GROUP = os.environ.get("AZURE_RESOURCE_GROUP", "YOUR-RESOURCE-GROUP")
RESOURCE_NAME = os.environ.get("AZURE_RESOURCE_NAME", "YOUR-RESOURCE-NAME")

result = subprocess.run(
    ["az", "cognitiveservices", "account", "keys", "list",
     "--resource-group", RESOURCE_GROUP,
     "--name", RESOURCE_NAME,
     "--query", "key1", "-o", "tsv"],
    capture_output=True, text=True
)

if result.returncode != 0:
    print(f"Error: {result.stderr}", file=sys.stderr)
    sys.exit(1)

key = result.stdout.strip()
if not key:
    print("Error: No key returned.", file=sys.stderr)
    sys.exit(1)

print(key)