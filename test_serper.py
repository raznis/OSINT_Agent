import os
import requests

# Test your API key with a simple request
serper_api_key = os.getenv("SERPER_API_KEY")  # Or however you're storing it

headers = {
    "X-API-KEY": serper_api_key,
    "Content-Type": "application/json"
}

payload = {
    "q": "test query",
    "gl": "us",
    "hl": "en"
}

response = requests.post("https://google.serper.dev/search", headers=headers, json=payload)
print(f"Status code: {response.status_code}")
print(f"Response: {response.text}")