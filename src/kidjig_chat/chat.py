import httpx

# base_url =  "https://api.kidjig.com/provider/api/v1/{provider}/chat/completions"

base_url = "https://api.kidjig.com/provider/api/v1/openai/chat/completions"
headers = {
    "X-Api-Key": "your_api_key",  # Replace with your KidJig API key
    "Content-Type": "application/json",
}
data = {
    "model": "gpt-4o",  # modelId or modelName
    "prompt": "What is the capital of France?",
    "stream": False,
    "config": {"temperature": 0.7, "maxOutputTokens": 4096, "topP": 1, "topK": 40},
}

try:
    response = httpx.post(base_url, headers=headers, json=data)
    response_data = response.json()
    print(response_data)

except Exception as e:
    print(f"An error occurred: {str(e)}")
