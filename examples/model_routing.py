"""
Route requests to different models based on task type.

Pattern: use a cheap/fast model for simple tasks,
a capable model for complex ones.

Prerequisites:
    pip install openai

Usage:
    export FUTURMIX_API_KEY=your_key_here
    python model_routing.py
"""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["FUTURMIX_API_KEY"],
    base_url="https://futurmix.ai/v1",
)

# Route different tasks to different models
ROUTING = {
    "classification": "gemini-2.0-flash",       # fast, cheap
    "summarization": "gemini-2.0-flash",         # fast, cheap
    "code_generation": "gpt-4o",                 # best for code
    "creative_writing": "claude-3-5-sonnet-20240620",  # best for writing
    "analysis": "gpt-4o",                        # best for reasoning
}


def chat(task_type: str, prompt: str) -> str:
    model = ROUTING.get(task_type, "gpt-4o")
    print(f"  [{task_type}] routing to {model}")

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


# Examples
tasks = [
    ("classification", "Is this text positive or negative? 'The service was excellent!'"),
    ("code_generation", "Write a Python function that checks if a number is prime."),
    ("creative_writing", "Write a one-sentence tagline for an AI gateway product."),
    ("summarization", "Summarize in one sentence: The quick brown fox jumps over the lazy dog."),
]

print("Model routing demo:\n")
for task_type, prompt in tasks:
    result = chat(task_type, prompt)
    print(f"  → {result}\n")
