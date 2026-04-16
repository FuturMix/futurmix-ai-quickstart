"""
Image generation with FuturMix using gpt-image-1.

Prerequisites:
    pip install openai requests

Usage:
    export FUTURMIX_API_KEY=your_key_here
    python image_generation.py
"""

import os
import requests
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["FUTURMIX_API_KEY"],
    base_url="https://futurmix.ai/v1",
)

response = client.images.generate(
    model="gpt-image-1",
    prompt="A simple diagram showing an API gateway routing requests to multiple AI providers",
    n=1,
    size="1024x1024",
)

image_url = response.data[0].url
print(f"Generated image URL: {image_url}")

# Optional: download the image
if image_url:
    img_data = requests.get(image_url).content
    with open("generated_image.png", "wb") as f:
        f.write(img_data)
    print("Saved to generated_image.png")
