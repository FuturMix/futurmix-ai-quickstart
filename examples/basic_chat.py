"""
Basic chat completion with FuturMix.

Prerequisites:
    pip install openai

Usage:
    export FUTURMIX_API_KEY=your_key_here
    python basic_chat.py
"""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["FUTURMIX_API_KEY"],
    base_url="https://futurmix.ai/v1",
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
)

print(response.choices[0].message.content)
print(f"\nTokens used: {response.usage.total_tokens}")
