# Quick Start — Azure AI Foundry + Cursor

This folder contains scripts to connect Azure AI Foundry models to your IDE.
For the full setup guide, see [README.md](./README.md).

---

## 1. Prerequisites

```bash
# Install Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash   # Linux
# brew install azure-cli                                  # macOS

# Log in
az login

# Install Python dependencies
pip install -r requirements.txt
```

---

## 2. Set Your Values

Every script reads from environment variables. Set these once in your shell (or create a `.env` file — never commit it):

```bash
export AZURE_ENDPOINT="https://YOUR-RESOURCE-NAME.services.ai.azure.com/openai/v1"
export AZURE_DEPLOYMENT="DeepSeek-V4-Pro"
export AZURE_RESOURCE_GROUP="YOUR-RESOURCE-GROUP"
export AZURE_RESOURCE_NAME="YOUR-RESOURCE-NAME"
```

---

## 3. Test the Connection

```bash
python run_model.py
```

Expected output: a short text response from the model.

---

## 4. Get Your API Key (for Cursor / Cline)

```bash
python get_api_key.py
```

Copy the output. Use it as the **API Key** in Cursor Settings → Models.

---

## 5. Run the Local Proxy (optional)

If your IDE doesn’t support Azure Entra ID auth directly:

```bash
python proxy_server.py
# proxy runs at http://127.0.0.1:8080/v1
```

Set `http://127.0.0.1:8080/v1` as the base URL in your IDE and use any dummy API key.

---

For troubleshooting and IDE-specific setup, see [README.md](./README.md).
