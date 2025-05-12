import httpx

# Get Available TTS Models Example
provider = "elevenlabs"  # Options: elevenlabs, whisper, sarvam
url = f"https://api.kidjig.com/provider/api/v1/tts/{provider}/models"

headers = {
    "X-Api-Key": "your_api_key",  # Replace with your KidJig API key
}

try:
    response = httpx.get(url, headers=headers)
    response_data = response.json()

    if response_data.get("success"):
        print("Available models:", response_data["data"]["models"])
        # You can process the models here
    else:
        print("Error:", response_data.get("message"))

except Exception as e:
    print(f"An error occurred: {str(e)}")

# Available providers and models can be found in the documentation
