"""
Streaming chat completion with FuturMix.

Works with any supported model — the gateway normalizes streaming
across providers to standard OpenAI SSE format.

Prerequisites:
    pip install openai

Usage:
    export FUTURMIX_API_KEY=your_key_here
    python streaming.py
"""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["FUTURMIX_API_KEY"],
    base_url="https://futurmix.ai/v1",
)

print("Streaming response from gpt-4o:\n")

with client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Count from 1 to 10, one number per line."},
    ],
    stream=True,
) as stream:
    for chunk in stream:
        delta = chunk.choices[0].delta
        if delta.content:
            print(delta.content, end="", flush=True)

print("\n\nDone.")
