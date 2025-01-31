import httpx

url = "https://api.kidjig.com/provider/api/v1/openai/chat/gpt-4o"
headers = {
    "X-Api-Key": "your_api_key",  # Replace with your KidJig API key
    "Content-Type": "application/json",
}
data = {
    "prompt": "What is the capital of France?",
    "stream": False,
    "config": {"temperature": 0.7, "maxOutputTokens": 4096, "topP": 1, "topK": 40},
}

try:
    response = httpx.post(url, headers=headers, json=data)
    response_data = response.json()

    # Extract specific information from the response
    success = response_data["success"]
    message = response_data["message"]
    ai_response = response_data["data"]["response"]
    usage = response_data["data"]["usage"]
    cost = response_data["data"]["cost"]

    print(f"Success: {success}")
    print(f"Message: {message}")
    print(f"AI Response: {ai_response}")
    print(f"Token Usage: {usage}")
    print(f"Cost: {cost}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
