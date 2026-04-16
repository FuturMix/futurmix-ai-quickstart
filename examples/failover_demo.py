"""
Manual failover pattern with FuturMix.

FuturMix handles failover automatically at the gateway level.
This example shows what manual fallback looks like if you want
explicit control over which model to try next.

Prerequisites:
    pip install openai

Usage:
    export FUTURMIX_API_KEY=your_key_here
    python failover_demo.py
"""

import os
import time
from openai import OpenAI
from openai import RateLimitError, APIStatusError

client = OpenAI(
    api_key=os.environ["FUTURMIX_API_KEY"],
    base_url="https://futurmix.ai/v1",
)

# Priority-ordered list of models to try
FALLBACK_CHAIN = [
    "gpt-4o",
    "claude-3-5-sonnet-20240620",
    "gemini-2.0-flash",
]


def call_with_explicit_fallback(messages: list, max_retries: int = 1) -> str:
    """
    Try each model in order. Move to the next on rate limit or server error.
    For most use cases, let the gateway handle this automatically instead.
    """
    last_error = None

    for model in FALLBACK_CHAIN:
        for attempt in range(max_retries + 1):
            try:
                print(f"  Trying {model} (attempt {attempt + 1})...")
                response = client.chat.completions.create(
                    model=model,
                    messages=messages,
                )
                print(f"  ✓ Success with {model}")
                return response.choices[0].message.content

            except RateLimitError as e:
                print(f"  ✗ Rate limited on {model}, trying next model")
                last_error = e
                break  # Don't retry same model on rate limit, move on

            except APIStatusError as e:
                if e.status_code >= 500:
                    print(f"  ✗ Server error on {model} (status {e.status_code})")
                    if attempt < max_retries:
                        time.sleep(2 ** attempt)
                        continue
                    last_error = e
                    break
                raise  # Re-raise client errors (4xx) — those are your bug

    raise RuntimeError(f"All models in fallback chain failed. Last error: {last_error}")


messages = [{"role": "user", "content": "Say hello in one sentence."}]

print("Running explicit fallback chain:\n")
result = call_with_explicit_fallback(messages)
print(f"\nFinal response: {result}")
