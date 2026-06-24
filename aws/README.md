<div align="center">

# 🆓 Use Claude AI for Free — via AWS Bedrock + Cursor IDE

### Stop paying $20/month. Get frontier-tier Claude models at **$0 out-of-pocket** using **$200 in guaranteed AWS credits**.

[![GitHub Stars](https://img.shields.io/github/stars/mohan67nv/free-ai-models-cloud-credits?style=social)](https://github.com/mohan67nv/free-ai-models-cloud-credits/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/mohan67nv/free-ai-models-cloud-credits?style=social)](https://github.com/mohan67nv/free-ai-models-cloud-credits/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/mohan67nv/free-ai-models-cloud-credits/pulls)

**If this guide saves you money, please ⭐ star and 🍴 fork this repo — it helps others find it!**

← [Back to Hub](../README.md)

</div>

---

## 💡 What Is This?

This is a **step-by-step, beginner-friendly guide** that shows you exactly how to:

- ✅ Claim **$200 in guaranteed free AWS credits** — $100 upfront + $100 from 5 quick tasks
- ✅ Access **Claude 3.5 Sonnet, Claude 3.5 Haiku, and Claude 4.x** via Amazon Bedrock
- ✅ Connect those models directly to **Cursor IDE** — just like a paid subscription
- ✅ Keep your **monthly bill at exactly $0** with budget safeguards

> **No startup required. No company email. No enterprise plan. Just a personal AWS account and 30 minutes.**

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Cost Overview — Why This Is Actually Free](#cost-overview)
3. [Phase 1 — Create & Verify Your AWS Account](#phase-1-create--verify-your-aws-account)
4. [Phase 2 — Claim Your Guaranteed $200 in Free Credits](#phase-2-claim-your-guaranteed-200-in-free-credits)
5. [Phase 3 — Set Up a Budget Safety Net](#phase-3-set-up-a-budget-safety-net)
6. [Phase 4 — Request Claude Model Access on Bedrock](#phase-4-request-claude-model-access-on-bedrock)
7. [Phase 5 — Understand Routing & Rate Limits](#phase-5-understand-routing--rate-limits)
8. [Phase 6 — Smart Model Selection (Make Credits Last)](#phase-6-smart-model-selection-make-credits-last)
9. [Phase 7 — Create a Secure IAM API User](#phase-7-create-a-secure-iam-api-user)
10. [Phase 8 — Connect Cursor IDE to AWS Bedrock](#phase-8-connect-cursor-ide-to-aws-bedrock)
11. [Other Ways to Use These Models](#other-ways-to-use-these-models)
12. [Troubleshooting Common Errors](#troubleshooting-common-errors)
13. [FAQ](#faq)
14. [Contributing](#contributing)

---

## Prerequisites

Before you start, make sure you have:

| Requirement | Details |
| :--- | :--- |
| A **credit or debit card** | Required for AWS identity verification only. A **$1 temporary hold** is placed and returned within 3–5 days. You will **not** be charged if you follow this guide. |
| **Cursor IDE** installed | Download free at [cursor.com](https://cursor.com) |
| ~30 minutes of time | Most steps are one-click. Credits apply automatically. |

> **No prior AWS experience needed.** Every step includes exactly where to click.

---

## Cost Overview

Here is a realistic breakdown of what you will spend:

| Item | Cost |
| :--- | :--- |
| AWS account creation | $0 |
| Identity verification hold | $1 (returned in 3–5 days) |
| AWS account creation credit (automatic) | **−$100** |
| 5 onboarding task credits ($20 × 5) | **−$100** |
| **Total free credits** | **$200** |
| Claude API usage (daily coding) | ~$2–$8/month, fully covered by credits |
| **Your actual out-of-pocket cost** | **$0** |

> AWS deposits the first **$100 automatically** when your account is verified. Complete the 5 short tasks in Phase 2 to unlock the remaining **$100** ($20 each). Both credit pools apply automatically before your card is ever billed.

---

## Phase 1: Create & Verify Your AWS Account

> **Goal:** Get a fully activated AWS account that can access Bedrock.

**Step 1 — Create a standard AWS account**

1. Go to [aws.amazon.com](https://aws.amazon.com/) and click **Create an AWS Account**.
2. Enter your email address, set a root password, and choose an account name (e.g., `my-dev-account`).
3. On the **Contact Information** screen, select **Personal** account type.
4. Enter your **credit or debit card** details. AWS places a temporary **$1 authorization hold** (returned in 3–5 business days) to verify your identity — you are not charged anything.
5. Complete the **SMS or phone call verification** step.
6. Choose the **Basic Support (Free)** plan.
7. You will receive a confirmation email. Sign in to the [AWS Console](https://console.aws.amazon.com/).

**Step 2 — Confirm your account is on the Pay-As-You-Go plan**

This is the most commonly missed step. Without it, AWS restricts your access to Bedrock model registries.

1. In the AWS Console, click your account name (top right) → **Billing and Cost Management**.
2. Go to **Payment methods** in the left sidebar.
3. Confirm your card is listed and verified (green checkmark or no warning banners).
4. Confirm there are no outstanding balances or account holds.

> ℹ️ Being on the Pay-As-You-Go plan does **not** void your Free Tier benefits and does **not** charge you automatically. It simply removes sandbox restrictions so you can access Bedrock and claim credits.

---

## Phase 2: Claim Your Guaranteed $200 in Free Credits

> **Goal:** Unlock all $200 in AWS promotional credits — $100 is automatic, $100 comes from 5 simple tasks.

### Part A — Your First $100 (Automatic)

As soon as your AWS account is verified and on the Pay-As-You-Go plan (Phase 1), AWS automatically deposits **$100 in promotional credits** into your account. You do not need to do anything extra.

1. Go to the [AWS Billing Console](https://console.aws.amazon.com/billing/).
2. In the left sidebar, click **Credits**.
3. You should already see a **$100 credit voucher** listed. If it is not there yet, wait up to 24 hours after verifying your account.

### Part B — Earn the Next $100 via 5 Quick Tasks ($20 each)

AWS rewards you with an additional **$20 credit per task** for completing short console interactions. All 5 tasks take under 15 minutes total.

Navigate to the AWS Console home page. Look for the **"Explore AWS" or "Earn AWS credits"** widget, or browse to each service directly:

| # | Task | What To Do | Credit |
| :-- | :--- | :--- | :--- |
| 1 | **Set up a Budget Alert** | Create any cost budget in AWS Budgets (detailed in Phase 3 below) | $20 |
| 2 | **Use the Bedrock Playground** | Open Bedrock → Playgrounds → Chat → select any model → send one test message | $20 |
| 3 | **Create an AWS Lambda Function** | Go to Lambda → Create function → choose a Node.js or Python blueprint → deploy it | $20 |
| 4 | **Launch and Terminate an EC2 Instance** | Go to EC2 → Launch instance → pick `t2.micro` (Free Tier) → launch → then immediately terminate it | $20 |
| 5 | **Create and Delete an RDS Database** | Go to RDS → Create database → pick MySQL or PostgreSQL → Free Tier template → create → then delete it | $20 |

> ⚠️ **Terminate/delete the EC2 and RDS resources immediately** after creating them. The credit is granted upon creation, not after running.

### Part C — Confirm Your Full $200 Balance

1. Return to **Billing Console → Credits**.
2. You should see **two credit vouchers** — the automatic $100 and the $100 from your 5 tasks — for a total of **$200**.
3. Credits may take up to 24 hours to appear after each task is completed.
4. Credits are applied **automatically** before your card is ever billed.

---

## Phase 3: Set Up a Budget Safety Net

> **Goal:** Set a $5/month alert so you are warned well before credits run out.

1. Go to [AWS Budgets](https://console.aws.amazon.com/billing/home#/budgets).
2. Click **Create budget** → select **Cost budget** → click **Next**.
3. Configure the budget:
   - **Budget name:** `bedrock-safety-net`
   - **Period:** Monthly
   - **Renewal type:** Recurring budget
   - **Budgeting method:** Fixed
   - **Budget amount:** `$5`
4. Click **Next** → **Add an alert threshold**:
   - **Threshold:** `80%` of budgeted amount (alerts you at $4 spent)
   - **Trigger:** Set both **Actual** and **Forecasted**
5. Enter your email address for notifications → click **Next** → **Create budget**.

> You will now receive an email warning the moment your monthly spend approaches $5 — long before credits are depleted.

---

## Phase 4: Request Claude Model Access on Bedrock

> **Goal:** Unlock Anthropic's Claude models in your AWS account.

1. Open the [Amazon Bedrock Console](https://console.aws.amazon.com/bedrock/).
2. **Select your region** using the dropdown in the top-right corner. Recommended: `us-east-1` (N. Virginia) or `us-west-2` (Oregon).
3. In the left sidebar, scroll to the very bottom and click **Model access**.
4. Click the **Manage model access** button (top right of the page).
5. Under the **Anthropic** section, check the following models:
   - ☑ **Claude 3.5 Haiku** — Fast and cheap. Use for most tasks.
   - ☑ **Claude 3.5 Sonnet** — Balanced power and cost.
   - ☑ **Claude Sonnet 4** / **Claude 4.6 Sonnet** — Flagship. Use for complex tasks.
6. Scroll down and click **Save changes**.
7. Wait 1–5 minutes and refresh the page. Each model should show a green **"Access granted"** badge.

> ✅ No approval forms, no company URL, no waiting days. Access is instant for personal accounts.

---

## Phase 5: Understand Routing & Rate Limits

Amazon Bedrock has three routing modes. Choosing the right one determines your speed and reliability.

| Mode | How It Works | Best For | Rate Limit |
| :--- | :--- | :--- | :--- |
| **On-Demand** | Single-region, direct routing | Testing only | Low — can hit 0 TPM during peak hours |
| **Cross-Region (Geo)** | Balances across your continent | Reliable daily use | Medium |
| **Cross-Region (Global)** | Dynamically routes worldwide | Active development | Very High — 6M+ TPM |

**Use Global Cross-Region for Cursor.** The model string format is:

```
us.anthropic.claude-3-5-haiku-20241022-v1:0
us.anthropic.claude-3-5-sonnet-20241022-v2:0
us.anthropic.claude-sonnet-4-5
```

**If you see a "0 TPM" limit on a model:**

1. Go to **Bedrock Console → Model access**.
2. Click the **⋮ menu** next to the model.
3. Select **View quota** → **Request quota increase**.
4. Enter a value like `50000` TPM and submit.
5. For verified Pay-As-You-Go accounts, approval usually takes a few hours.

---

## Phase 6: Smart Model Selection (Make Credits Last)

Route tasks to the right model to maximize how long your $200 lasts.

### Use Claude 3.5 Haiku for ~80% of your work
```
Model string: us.anthropic.claude-3-5-haiku-20241022-v1:0
```
- ✅ Code completion, autocomplete, quick bug fixes
- ✅ Explaining short functions
- ✅ Generating boilerplate
- ✅ Single-file edits

### Use Claude 3.5 Sonnet or Claude 4 Sonnet for complex tasks
```
Model string: us.anthropic.claude-3-5-sonnet-20241022-v2:0
             us.anthropic.claude-sonnet-4-5
```
- ✅ Multi-file refactoring
- ✅ Architecture planning
- ✅ Deep debugging across a full codebase
- ✅ Complex logic or algorithm design

### ⚠️ What to avoid

> **Do NOT use 1M-context variants for daily work.** Feeding a massive context window (200K+ tokens) costs significantly more in input tokens. Keep your Cursor context panel clean — only include files directly relevant to your current task.

---

## Phase 7: Create a Secure IAM API User

> **Goal:** Generate a dedicated API key for Cursor. Never use your root AWS account credentials.

1. Go to the [AWS IAM Console](https://console.aws.amazon.com/iam/).
2. In the left sidebar, click **Users** → **Create user**.
3. **User details:**
   - **User name:** `cursor-bedrock-user`
   - ❌ Do **not** check "Provide user access to the AWS Management Console" — this is an API-only user.
4. Click **Next** → **Attach policies directly**.
5. Search for `AmazonBedrockFullAccess` and check the box next to it.

   > 🔒 **Want tighter security?** Create a custom inline policy with only these permissions:
   > ```json
   > {
   >   "Effect": "Allow",
   >   "Action": [
   >     "bedrock:InvokeModel",
   >     "bedrock:InvokeModelWithResponseStream"
   >   ],
   >   "Resource": "arn:aws:bedrock:*::foundation-model/anthropic.*"
   > }
   > ```

6. Click **Next** → **Create user**.
7. Click on the newly created user → open the **Security credentials** tab.
8. Scroll to **Access keys** → click **Create access key**.
9. Select **Command Line Interface (CLI)** as the use case → click **Next** → **Create access key**.
10. **Copy both values immediately:**
    - `Access Key ID` (starts with `AKIA...`)
    - `Secret Access Key`

> 🚨 **Critical:** The Secret Access Key is shown **only once**. Copy it now or download the `.csv` file. If you lose it, delete and regenerate the key.

---

## Phase 8: Connect Cursor IDE to AWS Bedrock

> **Goal:** Enter your IAM credentials into Cursor and start using Claude for free.

1. Open **Cursor IDE**.
2. Press `Ctrl + Shift + J` (Windows/Linux) or `Cmd + Shift + J` (Mac) to open **Settings**.
3. Click the **Models** tab in the left sidebar.
4. Scroll down to the **AWS Bedrock** section and toggle it **ON**.
5. Fill in the fields:
   - **Access Key ID:** paste your `AKIA...` key
   - **Secret Access Key:** paste your secret key
   - **Region:** `us-east-1` or `us-west-2` (match the region from Phase 4)
6. In the model input field, type the model string:
   ```
   us.anthropic.claude-3-5-sonnet-20241022-v2:0
   ```
7. Click **Verify** or send a test message. You should get a response from Claude within seconds.
8. Add additional model strings for quick switching:
   ```
   us.anthropic.claude-3-5-haiku-20241022-v1:0
   us.anthropic.claude-sonnet-4-5
   ```

> ✅ You are now running frontier Claude AI at $0/month out of pocket.

---

## Other Ways to Use These Models

### Method 2: VS Code + Continue Extension (No Cursor needed)

[Continue](https://continue.dev) is a free, open-source AI coding assistant for VS Code that supports AWS Bedrock natively.

1. Install the **Continue** extension from the VS Code Marketplace.
2. Open the Continue config file: `~/.continue/config.json`
3. Add your Bedrock model under `models`:
   ```json
   {
     "models": [
       {
         "title": "Claude 3.5 Sonnet (Bedrock)",
         "provider": "bedrock",
         "model": "us.anthropic.claude-3-5-sonnet-20241022-v2:0",
         "region": "us-east-1",
         "accessKeyId": "YOUR_ACCESS_KEY_ID",
         "secretAccessKey": "YOUR_SECRET_ACCESS_KEY"
       },
       {
         "title": "Claude 3.5 Haiku (Bedrock)",
         "provider": "bedrock",
         "model": "us.anthropic.claude-3-5-haiku-20241022-v1:0",
         "region": "us-east-1",
         "accessKeyId": "YOUR_ACCESS_KEY_ID",
         "secretAccessKey": "YOUR_SECRET_ACCESS_KEY"
       }
     ]
   }
   ```
4. Save the file and open the Continue sidebar in VS Code. Your models will appear in the dropdown.

---

### Method 3: Python SDK (Direct API Calls)

Use the `boto3` AWS SDK to call Claude from any Python script or notebook.

```bash
pip install boto3
```

```python
import boto3
import json

client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
    aws_access_key_id="YOUR_ACCESS_KEY_ID",
    aws_secret_access_key="YOUR_SECRET_ACCESS_KEY",
)

response = client.invoke_model(
    modelId="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "Explain async/await in Python in 3 sentences."}
        ],
    }),
)

result = json.loads(response["body"].read())
print(result["content"][0]["text"])
```

---

### Method 4: AWS CLI Quick Test

Verify your setup from the terminal without writing any code:

```bash
aws bedrock-runtime invoke-model \
  --model-id us.anthropic.claude-3-5-haiku-20241022-v1:0 \
  --region us-east-1 \
  --body '{"anthropic_version":"bedrock-2023-05-31","max_tokens":256,"messages":[{"role":"user","content":"Hello!"}]}' \
  --cli-binary-format raw-in-base64-out \
  output.json && cat output.json
```

> Requires `aws configure` with your Access Key ID and Secret Access Key first.

---

## Troubleshooting Common Errors

### Error: `Request failed with status code 400: {"message": "model is required"}`

**Cause:** Another provider (Azure OpenAI, local LLM) is leaking its headers into the Bedrock request.

**Fix:**
1. Go to Cursor **Settings → Models**.
2. Toggle **OFF** every provider except AWS Bedrock (especially Azure OpenAI and any local LLM block).
3. Retry your request. This resolves the error immediately.

---

### Error: `ThrottlingException` or `0 TPM`

**Cause:** The model's rate limit is too low for the region.

**Fix:**
1. Switch your model string to the Global Cross-Region prefix: `us.anthropic.claude-...`
2. If still throttled, request a quota increase via **Bedrock Console → Model access → ⋮ → View quota → Request increase**.

---

### Error: `AccessDeniedException`

**Cause:** The IAM user lacks permissions, or you are calling a model in a region where access has not been requested.

**Fix:**
1. Confirm `AmazonBedrockFullAccess` is attached to your `cursor-bedrock-user` in IAM.
2. Confirm the region in Cursor matches the region where you enabled models in Bedrock.

---

### Credits are not showing up

**Fix:** Wait up to 24 hours and check **Billing Console → Credits**. If credits still do not appear after 48 hours, contact AWS Support — they will manually apply eligible credits.

---

## FAQ

**Q: Will AWS charge my card if I follow this guide?**
A: No. The $1 identity verification hold is returned in 3–5 business days. Credits automatically cover API charges. The $5 budget alert warns you before anything else happens.

**Q: What happens when my credits run out?**
A: AWS will start billing your card at standard Bedrock inference rates. At typical daily coding usage (Haiku for 80% of requests), **$200 in credits lasts 6–12+ months**. You can also apply for AWS Activate or AWS research grants to extend your runway.

**Q: Can I use this on a Mac, Windows, or Linux machine?**
A: Yes. Cursor is cross-platform and the AWS configuration is identical on all operating systems.

**Q: Is this against AWS Terms of Service?**
A: No. AWS publicly offers these onboarding credits to all new accounts. Using Bedrock for personal AI coding assistance is a fully supported and intended use case.

**Q: Which Claude model should I use by default?**
A: Start with `us.anthropic.claude-3-5-haiku-20241022-v1:0` for speed and cost-efficiency. Switch to Sonnet only for complex multi-file tasks.

---

## Contributing

Found a better model string, an updated credit task, or a clearer explanation?

1. **Fork** this repository
2. Create a branch: `git checkout -b improve/your-change`
3. Edit `aws/README.md`
4. Open a **Pull Request**

Found an issue? Open an [Issue](https://github.com/mohan67nv/free-ai-models-cloud-credits/issues).

---

<div align="center">

### If this guide helped you save money, give it a ⭐ star!

← [Back to Hub](../README.md) · [GCP Guide →](../gcp/README.md)

**MIT License** · Made with ❤️ for developers who code smart

</div>
