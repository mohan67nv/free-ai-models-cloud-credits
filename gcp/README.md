<div align="center">

# 🚀 Use Gemini & Claude for Free — via Google Vertex AI + Cursor IDE

### Stop paying $20/month. Get frontier-tier Gemini and Claude models at **$0 out-of-pocket** using **$300 in Google Cloud free trial credits**.

[![GitHub Stars](https://img.shields.io/github/stars/mohan67nv/free-ai-models-cloud-credits?style=social)](https://github.com/mohan67nv/free-ai-models-cloud-credits/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/mohan67nv/free-ai-models-cloud-credits?style=social)](https://github.com/mohan67nv/free-ai-models-cloud-credits/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/mohan67nv/free-ai-models-cloud-credits/pulls)

**If this guide saves you money, please ⭐ star and 🍴 fork this repo — it helps others find it!**

← [Back to Hub](../README.md)

</div>

---

## 💡 What Is This?

This guide walks you through connecting **Cursor IDE** (and VS Code) to **Google Vertex AI** models — including Gemini and Anthropic's Claude — using your own Google Cloud account.

- ✅ Claim **$300 in free Google Cloud credits** (no auto-charge after trial ends)
- ✅ Access **Gemini 2.5 Pro, Claude 3.5 Sonnet, Claude 4 Sonnet** via Vertex AI
- ✅ Connect to Cursor IDE using a **local LiteLLM proxy** (zero-config bridge)
- ✅ Keep your **monthly bill at $0** for 3–12 months of daily AI coding

> **No startup. No company email. Just a Google account and about 30 minutes.**

---

## ⚠️ Critical Warnings — Read Before You Start

These two mistakes will silently drain your $300 credits or charge your card directly. Read them first.

### 1. Never click "Deploy Model" in the Model Garden

The Model Garden shows two paths for each model: a **serverless API** path and a **"Deploy Model"** path.

- The **serverless API** path is what this guide uses — pay per token, no infrastructure, covered by your credits.
- The **"Deploy Model"** path spins up a **dedicated GPU cluster** (NVIDIA A100/H100 nodes). This is enterprise infrastructure that costs approximately **$148/hour (~$108,000/month)**. It will completely wipe out your $300 credits within a few hours.

> ✅ Always choose the **API** or **OpenAI-compatible endpoint** option. Never click the blue **Deploy** button.

### 2. Claude models on Vertex AI are NOT covered by GCP promotional credits

This is the most important billing fact in this entire guide:

| Model | Credit Coverage |
| :--- | :--- |
| **Gemini models** (Gemini 2.5 Pro, Gemini 2.0 Flash, etc.) | ✅ Fully covered by your $300 GCP credits |
| **Anthropic Claude models via Vertex AI** | ❌ Treated as a **Marketplace purchase** — billed **directly to your card**, bypassing your GCP credits entirely |

> Claude models are distributed through the GCP Marketplace as a third-party product. Google's promotional credit pool does not apply to Marketplace purchases. If you use Claude via Vertex AI, those charges go straight to your payment method.

**Recommendation:** Use **Gemini models** to stay fully within your free $300 credits. If you need Claude, use the [AWS Bedrock guide](../aws/README.md) instead — Claude there is covered by the $200 AWS promotional credits.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Cost Overview](#cost-overview)
3. [Phase 1 — Get Your $300 in Free GCP Credits](#phase-1-get-your-300-in-free-gcp-credits)
4. [Phase 2 — Create a Project & Enable Vertex AI](#phase-2-create-a-project--enable-vertex-ai)
5. [Phase 3 — Enable Models in Model Garden](#phase-3-enable-models-in-model-garden)
6. [Phase 4 — Set Up a Budget Alert](#phase-4-set-up-a-budget-alert)
7. [Phase 5 — Install & Authenticate Google Cloud CLI](#phase-5-install--authenticate-google-cloud-cli)
8. [Phase 6 — Install & Configure LiteLLM](#phase-6-install--configure-litellm)
9. [Phase 7 — Run the LiteLLM Proxy Server](#phase-7-run-the-litellm-proxy-server)
10. [Phase 8 — Configure Cursor IDE](#phase-8-configure-cursor-ide)
11. [Other Ways to Use These Models](#other-ways-to-use-these-models)
12. [Troubleshooting](#troubleshooting)
13. [FAQ](#faq)
14. [Contributing](#contributing)

---

## Prerequisites

| Requirement | Details |
| :--- | :--- |
| A **Google account** | Any personal Gmail works |
| A **credit or debit card** | Required for GCP identity verification only. You will **not** be auto-charged after the free trial ends unless you manually upgrade. |
| **Python 3.8+** installed | Required for LiteLLM. Check with `python3 --version` |
| **Cursor IDE** installed | Download free at [cursor.com](https://cursor.com) |
| ~30 minutes of time | All steps are clearly explained |

> **No prior GCP or cloud experience needed.**

---

## Cost Overview

| Item | Cost |
| :--- | :--- |
| GCP account creation | $0 |
| Identity verification hold | ~$1 (returned immediately or within a few days) |
| **Google Cloud free trial credits** | **−$300** |
| Gemini 2.5 Pro daily coding usage | ~$5–$15/month, **covered by $300 credits** |
| Gemini 2.0 Flash daily coding usage | ~$1–$5/month, **covered by $300 credits** |
| Claude via Vertex AI (if used) | Billed **directly to your card** — NOT covered by credits |
| **Your actual out-of-pocket cost (Gemini only)** | **$0** |

> The $300 trial is valid for 90 days. After that, GCP will **not** auto-charge you — your account moves to a free tier and services stop unless you manually upgrade. At typical daily Gemini usage, $300 covers 3–6 months of heavy use.

**💡 Cache cost tip:** Vertex AI uses a tiered caching layer for large codebases. Input tokens that hit the cache (files you sent in a previous prompt) cost ~**$0.25/1M tokens** (cache read). New or modified files cost ~**$3.22/1M tokens** (cache write). The cache TTL is **300 seconds (5 minutes)**. To keep costs low, group related prompts in the same chat tab and avoid switching files constantly — this keeps your context in the hot cache.

---

## Phase 1: Get Your $300 in Free GCP Credits

> **Goal:** Activate your Google Cloud free trial to unlock $300 in credits.

1. Go to [console.cloud.google.com](https://console.cloud.google.com/).
2. Sign in with your Google account.
3. You should see a banner: **"Get $300 in free credits"** or **"Start Free Trial"**. Click it.
4. Fill in the activation form:
   - Select your **country** and agree to the terms.
   - Enter your **credit or debit card** details. This is for identity verification only. A small temporary authorization hold may appear and will be reversed.
   - **Important:** Google will NOT auto-charge you after the trial ends. Your services simply stop.
5. Click **Start my free trial**.
6. You will land on the GCP Console dashboard with $300 in credits active.

> ✅ Your free trial credits are now live. Any Vertex AI usage in this guide will draw from this balance.

---

## Phase 2: Create a Project & Enable Vertex AI

> **Goal:** Set up a dedicated GCP project and turn on the Vertex AI API.

**Step 1 — Create a new project**

1. In the top-left of the GCP Console, click the **project dropdown** (next to the Google Cloud logo).
2. Click **New Project**.
3. Enter a name (e.g., `cursor-vertex-ai`) and click **Create**.
4. Wait a few seconds for the project to be created, then select it from the dropdown.
5. **Copy your Project ID** — it will look like `cursor-vertex-ai-a1b2c3`. You will need this later.

> The **Project ID** is shown below the project name on the project creation screen and on the dashboard. It is different from the project name.

**Step 2 — Enable the Vertex AI API**

1. In the search bar at the top of the console, type **"Vertex AI API"**.
2. Click the result that says **Vertex AI API** (from Google Enterprise APIs).
3. Click the **Enable** button.
4. Wait 30–60 seconds for the API to activate.

---

## Phase 3: Enable Models in Model Garden

> **Goal:** Unlock Gemini and Claude models for your project.

1. In the GCP Console left sidebar, navigate to **Vertex AI → Model Garden**.
   - If you do not see it, use the search bar and type "Model Garden".
2. **Enable Gemini models:**
   - Search for **Gemini 2.5 Pro** (or `gemini-2.5-pro-preview`).
   - Click the model card → click **Enable** or confirm it shows as available.
   - Repeat for **Gemini 2.0 Flash** for a faster, cheaper option.
3. **Enable Anthropic Claude models (optional — read the billing note first):**
   - Search for **Claude** in the Model Garden.
   - Click **Claude 3.5 Sonnet** → you will be asked to **accept Anthropic's terms of service** (a simple click-through agreement).
   - Repeat for **Claude Sonnet 4** / **Claude 3.5 Haiku** if available in your region.
4. Confirm each model shows a green status or **"Enabled"** indicator.

> ⚠️ **Claude billing reminder:** Claude models on Vertex AI are a Marketplace product and are billed directly to your card — your $300 GCP credits do not apply. Gemini models are fully covered. See the [Critical Warnings](#️-critical-warnings--read-before-you-start) section at the top for full details.

---

## Phase 4: Set Up a Budget Alert

> **Goal:** Get an email warning before your $300 credits are significantly consumed.

1. In the GCP Console search bar, type **"Budgets & alerts"** and click it.
2. Click **Create budget**.
3. Configure:
   - **Name:** `vertex-ai-safety-net`
   - **Projects:** Select your project (e.g., `cursor-vertex-ai`)
   - **Budget type:** Specified amount
   - **Amount:** `$50`
4. Click **Next** → set alert thresholds:
   - Add threshold at **50%** ($25 spent) — early warning
   - Add threshold at **90%** ($45 spent) — urgent warning
5. Enter your email address for notifications.
6. Click **Finish**.

> You will receive email alerts at $25 and $45 spent — giving you plenty of runway before anything happens to your $300 balance.

---

## Phase 5: Install & Authenticate Google Cloud CLI

> **Goal:** Connect your local machine to your GCP project using secure credentials that LiteLLM will use automatically.

**Step 1 — Install the gcloud CLI**

Follow the official install guide for your OS: [cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)

Quick install options:
```bash
# macOS (Homebrew)
brew install --cask google-cloud-sdk

# Linux (apt)
sudo apt-get install google-cloud-cli

# Windows
# Download the installer from the official docs link above
```

**Step 2 — Log in and set up Application Default Credentials**

This is the key step. Run:

```bash
gcloud auth application-default login
```

A browser window will open. Log in with your Google account and grant the requested permissions. This saves a local credential file that LiteLLM reads automatically — you never need to paste credentials into config files.

**Step 3 — Set your active project**

```bash
gcloud config set project YOUR_PROJECT_ID
```

Replace `YOUR_PROJECT_ID` with the Project ID you copied in Phase 2 (e.g., `cursor-vertex-ai-a1b2c3`).

**Verify everything is working:**
```bash
gcloud auth application-default print-access-token
```

If this prints a long token string, your credentials are valid.

---

## Phase 6: Install & Configure LiteLLM

> **Goal:** Set up LiteLLM as a local proxy that makes Vertex AI look like an OpenAI-compatible API to Cursor.

**Why LiteLLM?** Cursor's AWS Bedrock integration works natively, but for Google Vertex AI, Cursor expects an OpenAI-compatible endpoint. LiteLLM runs locally on your machine and translates Cursor's requests into Vertex AI API calls — invisibly.

**Step 1 — Install LiteLLM**

```bash
pip install 'litellm[proxy]'
```

**Step 2 — Create the configuration file**

Create a new folder for your config and add a `config.yaml` file:

```bash
mkdir ~/litellm-vertex && cd ~/litellm-vertex
```

Create `config.yaml` with the following content. Replace `YOUR_PROJECT_ID` with your actual GCP Project ID:

```yaml
model_list:
  # Gemini 2.5 Pro — Best for complex reasoning and architecture tasks
  - model_name: gemini-2.5-pro
    litellm_params:
      model: vertex_ai/gemini-2.5-pro-preview-06-05
      vertex_project: "YOUR_PROJECT_ID"
      vertex_location: "us-central1"

  # Gemini 2.0 Flash — Fast and cheap, great for daily work
  - model_name: gemini-2.0-flash
    litellm_params:
      model: vertex_ai/gemini-2.0-flash-001
      vertex_project: "YOUR_PROJECT_ID"
      vertex_location: "us-central1"

  # Claude 3.5 Sonnet via Vertex AI — Balanced power and cost
  - model_name: claude-3.5-sonnet
    litellm_params:
      model: vertex_ai/claude-3-5-sonnet-v2@20241022
      vertex_project: "YOUR_PROJECT_ID"
      vertex_location: "us-east5"

  # Claude Sonnet 4 via Vertex AI — Flagship for complex tasks
  - model_name: claude-sonnet-4
    litellm_params:
      model: vertex_ai/claude-sonnet-4-5
      vertex_project: "YOUR_PROJECT_ID"
      vertex_location: "global"
```

> **Region note:** Gemini models are widely available in `us-central1`. Claude models on Vertex AI are available in `us-east5` and `global`. Check the [Vertex AI model availability page](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations) if a region gives an error.

---

## Phase 7: Run the LiteLLM Proxy Server

> **Goal:** Start the local proxy so Cursor can talk to Vertex AI.

Navigate to the folder with your `config.yaml` and run:

```bash
cd ~/litellm-vertex
litellm --config config.yaml
```

You should see output like:
```
INFO: Started server process [12345]
INFO: Uvicorn running on http://0.0.0.0:4000
```

**Leave this terminal window open** while you use Cursor. The proxy must be running for Cursor to work.

> 💡 **Tip — Auto-start on boot (optional):** To avoid manually running this every time, you can set it up as a system service. On Linux/macOS, create a simple shell script and add it to your startup items.

---

## Phase 8: Configure Cursor IDE

> **Goal:** Point Cursor to your local LiteLLM proxy and start using Gemini and Claude for free.

1. Open **Cursor IDE**.
2. Press `Ctrl + Shift + J` (Windows/Linux) or `Cmd + Shift + J` (Mac) to open **Settings**.
3. Click the **Models** tab.
4. **Disable all default models** (GPT-4o, Claude 3.5, etc.) by toggling them off. This ensures Cursor only routes requests through your proxy.
5. Scroll down to the **Add a model** section and add each model name exactly as written in your `config.yaml`:
   - `gemini-2.5-pro`
   - `gemini-2.0-flash`
   - `claude-3.5-sonnet`
   - `claude-sonnet-4`
6. Scroll down to **OpenAI API Key** and **Override OpenAI Base URL**:
   - **Override OpenAI Base URL:** Toggle **ON** → set to `http://127.0.0.1:4000`
   - **OpenAI API Key:** Enter any placeholder value, e.g. `sk-1234`

   > LiteLLM handles the real Google Cloud authentication via the `gcloud` credentials from Phase 5. Cursor just needs a non-empty API key field — the value itself does not matter.

7. Click **Verify** next to the Base URL field. If the proxy is running, it will show a success message.
8. Open a new Cursor chat, select `gemini-2.5-pro` or `claude-3.5-sonnet` from the model dropdown, and start coding.

> ✅ You are now running frontier Gemini and Claude models at $0/month out of pocket.

---

## Other Ways to Use These Models

### Method 2: Direct Token Connection (No LiteLLM — Gemini Only)

For Gemini models only, you can connect Cursor directly to Vertex AI without running LiteLLM at all. This uses a short-lived OAuth2 bearer token instead of a proxy.

**Step 1 — Generate a temporary access token:**
```bash
gcloud auth print-access-token
```
This prints a long token string. Copy the entire output.

> ⚠️ **This token expires after 1 hour.** If Cursor returns an authentication error later, re-run this command and paste the new token into Cursor's API key field.

**Step 2 — Configure Cursor:**
1. Open Cursor → `Ctrl + Shift + J` → **Models** tab.
2. Toggle the **OpenAI** block **ON**.
3. Paste the token into the **OpenAI API Key** field.
4. Toggle **Override OpenAI Base URL** ON and set it to your regional endpoint:
   ```
   https://REGION-aiplatform.googleapis.com/v1/projects/YOUR_PROJECT_ID/locations/REGION/endpoints/openapi
   ```
   Example for `us-central1`:
   ```
   https://us-central1-aiplatform.googleapis.com/v1/projects/cursor-vertex-ai-a1b2c3/locations/us-central1/endpoints/openapi
   ```
5. Scroll to **Add a model** and add:
   - `google/gemini-2.5-pro-preview-06-05`
   - `google/gemini-2.0-flash-001`
6. **Disable all other model providers** to ensure traffic only goes to your endpoint.
7. Select your model in a chat and send a test message.

> **When to use this vs LiteLLM:** Use the direct token method for a quick test or if you only need Gemini. Use LiteLLM (Phases 6–8) for a permanent setup that doesn't require refreshing tokens every hour.

---

### Method 3: VS Code + Continue Extension (No Cursor, No LiteLLM)

[Continue](https://continue.dev) supports Vertex AI natively in VS Code without needing a proxy.

1. Install the **Continue** extension from the VS Code Marketplace.
2. Open `~/.continue/config.json` and add:

```json
{
  "models": [
    {
      "title": "Gemini 2.5 Pro (Vertex)",
      "provider": "vertexai",
      "model": "gemini-2.5-pro-preview-06-05",
      "projectId": "YOUR_PROJECT_ID",
      "region": "us-central1"
    },
    {
      "title": "Claude 3.5 Sonnet (Vertex)",
      "provider": "vertexai",
      "model": "claude-3-5-sonnet-v2@20241022",
      "projectId": "YOUR_PROJECT_ID",
      "region": "us-east5"
    }
  ]
}
```

3. Continue uses your `gcloud` application default credentials automatically — no API key needed.

---

### Method 4: Python SDK (Direct Vertex AI Calls)

Use the official `google-cloud-aiplatform` SDK for scripts, notebooks, or automation:

```bash
pip install google-cloud-aiplatform
```

**Gemini via Vertex AI:**
```python
import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project="YOUR_PROJECT_ID", location="us-central1")

model = GenerativeModel("gemini-2.5-pro-preview-06-05")
response = model.generate_content("Explain how async/await works in Python.")
print(response.text)
```

**Claude via Vertex AI (using Anthropic's SDK):**
```bash
pip install anthropic[vertex]
```

```python
import anthropic

client = anthropic.AnthropicVertex(
    project_id="YOUR_PROJECT_ID",
    region="us-east5",
)

message = client.messages.create(
    model="claude-3-5-sonnet-v2@20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Refactor this function to be more Pythonic."}
    ],
)
print(message.content[0].text)
```

> Uses your `gcloud auth application-default login` credentials automatically — no API keys needed in code.

---

### Method 5: Google AI Studio (Gemini Only — No Setup)

For quick Gemini testing without any setup:

1. Go to [aistudio.google.com](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Select a Gemini model and start prompting — free usage with Google account limits.

> ⚠️ **Important:** AI Studio credits and your GCP Billing Account are **completely separate** funding pools. Credits added inside AI Studio only apply to the native Gemini developer API (`api.generativeai.google`). They do **not** transfer to Vertex AI. Conversely, your $300 GCP trial credits do not apply to AI Studio. Do not confuse the two consoles.

---

### Method 6: LiteLLM with an API Key (Shareable Setup)

If you want to share the proxy or use it from multiple machines, add an API key to LiteLLM:

Update `config.yaml`:
```yaml
general_settings:
  master_key: "sk-my-secret-key"   # Set any string you choose

model_list:
  # ... your model list as before
```

Then in Cursor, set the **OpenAI API Key** field to `sk-my-secret-key` instead of a placeholder. This prevents anyone else on your network from using your proxy without the key.

---

## Troubleshooting

### LiteLLM starts but Cursor cannot connect

**Check:**
1. Confirm the proxy is running: open `http://127.0.0.1:4000` in your browser — you should see a LiteLLM status page.
2. In Cursor, make sure the Base URL is exactly `http://127.0.0.1:4000` (not `https`, not `0.0.0.0`).
3. Make sure the model names in Cursor match exactly what you wrote under `model_name:` in `config.yaml`.

---

### Error: `google.auth.exceptions.DefaultCredentialsError`

**Cause:** LiteLLM cannot find your Google credentials.

**Fix:**
```bash
gcloud auth application-default login
```

Re-run this command and complete the browser login. Then restart the LiteLLM server.

---

### Error: `403 Permission denied` or `Vertex AI API not enabled`

**Cause:** The Vertex AI API is not enabled, or the model was not activated in Model Garden.

**Fix:**
1. Go to GCP Console → search **"Vertex AI API"** → confirm it shows **Enabled**.
2. Go to **Vertex AI → Model Garden** → confirm the model shows as available/enabled for your project.

---

### Error: `404 Model not found` or wrong region

**Cause:** The model is not available in the `vertex_location` specified in `config.yaml`.

**Fix:**
- For Gemini models, use `us-central1`
- For Claude models, try `us-east5` or `global`
- Check availability at [cloud.google.com/vertex-ai/generative-ai/docs/learn/locations](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations)

---

### Error: `RESOURCE_EXHAUSTED` or quota exceeded

**Cause:** You have hit the requests-per-minute limit for the model.

**Fix:**
1. Go to GCP Console → **IAM & Admin → Quotas**.
2. Search for `Vertex AI`.
3. Find the relevant model quota and click **Edit Quotas** to request an increase.

---

### Error: `resourcemanager.projects.get` — Permission Denied in the Console

**Cause:** Chrome's multi-account session caching is using the wrong Google profile. The console is logged in as a different account than the one holding your credits and project.

**Fix:**
1. Check the **profile icon in the top-right** of the GCP Console — confirm it shows the Google account that created your project and holds your credits.
2. Confirm the **project dropdown** (top navigation bar) shows your active project — not `"My First Project"` or an old default project.
3. If the issue persists, explicitly grant the Viewer role to your account via the terminal:
   ```bash
   gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
     --member="user:your-email@gmail.com" \
     --role="roles/viewer"
   ```

---

### Direct token method: Cursor returns auth error after a while

**Cause:** The `gcloud auth print-access-token` token has expired. Tokens are valid for **1 hour only**.

**Fix:** Re-run the command and paste the new token into Cursor:
```bash
gcloud auth print-access-token
```
Go to Cursor **Settings → Models → OpenAI API Key** and replace the old token. This is why the LiteLLM proxy method (Phases 6–8) is recommended for daily use — it handles token refresh automatically.

---

## FAQ

**Q: Will Google charge my card automatically when the $300 trial ends?**
A: No. Google explicitly does not auto-charge when the free trial expires. Your services will simply pause. You must manually click "Upgrade" to convert to a paid account.

**Q: How long does $300 last for daily AI coding?**
A: It depends on the models you use. With Gemini Flash for ~80% of tasks and Gemini Pro or Claude Sonnet for complex work, $300 typically lasts **3–6 months** of heavy daily use.

**Q: Do I need to keep the LiteLLM terminal open?**
A: Yes — the proxy must be running for Cursor to work. You can set it up as a background service (systemd on Linux, launchd on macOS, or a startup task on Windows) to avoid running it manually each time.

**Q: Can I use both AWS Bedrock and GCP Vertex AI at the same time?**
A: Yes. You can run both — use Bedrock directly in Cursor's built-in AWS integration, and Vertex AI through the LiteLLM proxy. See the [AWS guide](../aws/README.md) for the Bedrock setup.

**Q: Is Claude on Vertex AI the same as Claude on AWS Bedrock?**
A: The underlying model weights are identical. However, there is a critical billing difference: Claude on Vertex AI is a Marketplace product and is **billed directly to your card** — your $300 GCP credits do not apply. Claude on AWS Bedrock is covered by the $200 AWS promotional credits. If you want Claude for free, use the [AWS guide](../aws/README.md).

**Q: Does my $300 GCP credit cover Claude models on Vertex AI?**
A: No. Claude is a third-party Marketplace product on GCP. Only first-party Google models (Gemini family) are covered by GCP promotional credits. Claude usage will be charged directly to your billing payment method.

**Q: Can I use this on Mac, Windows, or Linux?**
A: Yes. The gcloud CLI, Python, and LiteLLM all work on all three platforms.

---

## Contributing

Found a better region, an updated model string, or a clearer explanation?

1. **Fork** this repository
2. Create a branch: `git checkout -b improve/your-change`
3. Edit `gcp/README.md`
4. Open a **Pull Request**

Found an issue? Open an [Issue](https://github.com/mohan67nv/free-ai-models-cloud-credits/issues).

---

<div align="center">

### If this guide helped you save money, give it a ⭐ star!

← [Back to Hub](../README.md) · [AWS Guide →](../aws/README.md)

**MIT License** · Made with ❤️ for developers who code smart

</div>
