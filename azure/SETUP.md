# Azure AI Foundry — Setup Guide

This project lets you use **DeepSeek-V4-Pro** (and other models) deployed on **Azure AI Foundry**, billed against your Azure subscription credits.

> 💡 **Project Details** — fill these in with your own values after completing Step 1 of the README.
> | Item | Your Value |
> |------|-------|
> | Subscription | *(your Azure subscription name)* |
> | Resource Group | `YOUR-RESOURCE-GROUP` |
> | Resource | `YOUR-RESOURCE-NAME` (AI Services) |
> | Region | e.g. `swedencentral`, `eastus`, `westeurope` |
> | Endpoint | `https://YOUR-RESOURCE-NAME.services.ai.azure.com/openai/v1` |
> | Model | `DeepSeek-V4-Pro` |
> | Available Models | `DeepSeek-V4-Pro`, `Mistral-Large-3` (Mistral-Large-3-2), `text-embedding-3-large` |

---

## 🔧 Prerequisites (All Methods)

```bash
# 1. Clone & enter the project
git clone https://github.com/mohan67nv/free-ai-models-cloud-credits.git
cd free-ai-models-cloud-credits/azure

# 2. Login to Azure
az login

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Method 1️⃣ : Azure Identity (Bearer Token) — VS Code / Terminal

**Best for:** scripts, Jupyter notebooks, local development. Tokens auto-refresh.

```bash
python run_model.py
```

This uses `DefaultAzureCredential()` from `azure-identity` — it auto-detects your `az login` session and gets bearer tokens. No API key needed. Tokens expire in ~1 hour but auto-refresh.

### How it works:
```python
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default"
)

client = OpenAI(
    base_url="https://YOUR-RESOURCE-NAME.services.ai.azure.com/openai/v1",
    api_key=token_provider   # ← this is a callable, not a string
)
```

---

## Method 2️⃣ : API Key (Static) — Cursor, VS Code, Any Client

**Best for:** Cursor IDE, any OpenAI-compatible tool, long-lived connections.

### Step 1: Get your API key
```bash
python get_api_key.py
```

Or directly:
```bash
az cognitiveservices account keys list \
  --resource-group YOUR-RESOURCE-GROUP \
  --name YOUR-RESOURCE-NAME \
  --query key1 -o tsv
```

### Step 2: Configure your client

| Setting | Value |
|---------|-------|
| **Base URL** | `https://YOUR-RESOURCE-NAME.services.ai.azure.com/openai/v1` |
| **API Key** | *(paste the key from Step 1)* |
| **Model** | `DeepSeek-V4-Pro` |

✅ The API key **never expires**. Set it once and forget it.

### For Cursor IDE:
1. Open Cursor → Settings → Models
2. Add a new model provider with the settings above
3. Select `DeepSeek-V4-Pro` as your model

---

## Method 3️⃣ : Bearer Token from CLI — Manual, One-time

**Best for:** quick one-off testing, no Python needed.

```bash
# Get a token (valid ~1 hour)
TOKEN=$(az account get-access-token \
  --resource https://ai.azure.com/.default \
  --query accessToken -o tsv)

# Test with curl
curl -s "https://YOUR-RESOURCE-NAME.services.ai.azure.com/openai/v1/chat/completions" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "DeepSeek-V4-Pro",
    "messages": [{"role": "user", "content": "Hello!"}]
  }' | python -m json.tool
```

> Re-run the `az account get-access-token` command when the token expires (~1 hour).

---

## Method 4️⃣ : Local Proxy — Cursor, Any Client

**Best for:** using Entra ID auth with clients that don't support it.

Start the proxy:
```bash
python proxy_server.py
```

Then configure Cursor / any client:

| Setting | Value |
|---------|-------|
| **Base URL** | `http://127.0.0.1:8080/v1` |
| **API Key** | `dummy` (ignored) |
| **Model** | `DeepSeek-V4-Pro` |

Keep the proxy running while using the client.

---

## 📦 Project Files

| File | Purpose |
|------|---------|
| `run_model.py` | Test script — calls the model via bearer token |
| `get_api_key.py` | Print your static API key |
| `get_token.py` | Print a one-time bearer token |
| `proxy_server.py` | Local HTTP proxy for Cursor (Entra ID auth) |
| `requirements.txt` | Python dependencies |
| `.env` | Environment variables (Azure project config) |
| `SETUP.md` | This guide |

---

## 💰 Billing

All API calls are billed to your **Azure subscription**. Your free credits cover usage. Monitor costs at [portal.azure.com](https://portal.azure.com) → Cost Management.

### Available models & their pricing:
- **DeepSeek-V4-Pro** — GlobalStandard
- **Mistral-Large-3** — GlobalStandard
- **text-embedding-3-large** — Standard

---

## 🔒 Security Notes

- `.env` contains your Azure project details — don't commit to public repos
- API keys are sensitive — use Method 1 (bearer token) when possible
- The `.gitignore` already excludes `.env` files