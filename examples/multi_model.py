"""
Compare responses across multiple models with FuturMix.

Same prompt, different models — one client, one API key.

Prerequisites:
    pip install openai

Usage:
    export FUTURMIX_API_KEY=your_key_here
    python multi_model.py
"""

import os
import time
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["FUTURMIX_API_KEY"],
    base_url="https://futurmix.ai/v1",
)

MODELS = [
    "gpt-4o",
    "claude-3-5-sonnet-20240620",
    "gemini-2.0-flash",
]

PROMPT = "In one sentence, what is the most important thing to know about building reliable AI applications?"


def call_model(model: str, prompt: str) -> dict:
    start = time.perf_counter()
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    latency_ms = round((time.perf_counter() - start) * 1000)

    return {
        "model": model,
        "response": response.choices[0].message.content,
        "latency_ms": latency_ms,
        "input_tokens": response.usage.prompt_tokens,
        "output_tokens": response.usage.completion_tokens,
    }


print(f"Prompt: {PROMPT}\n")
print("=" * 60)

for model in MODELS:
    result = call_model(model, PROMPT)
    print(f"\n[{result['model']}] ({result['latency_ms']}ms, "
          f"{result['input_tokens']}+{result['output_tokens']} tokens)")
    print(result["response"])
