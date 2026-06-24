#!/usr/bin/env python3
"""
Generate an Azure bearer token for Azure AI Foundry and print it.
Use this to pipe into a file that Cursor reads as an API key.

Usage:
    python get_token.py > ~/.azure-foundry-key.txt

Token expires in ~1 hour. Re-run when needed.
"""

from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
token = credential.get_token("https://ai.azure.com/.default")

print(token.token)