import httpx


def generate_speech(provider, model, text, **kwargs):
    """
    Generate speech using the KidJig TTS API.

    Args:
        provider (str): The TTS provider to use (elevenlabs, whisper, sarvam)
        model (str): The model ID to use (e.g., aria, alloy, meera)
        text (str): The text to convert to speech
        **kwargs: Additional provider-specific parameters

    Returns:
        str: URL to the generated audio file, or None if an error occurred
    """
    url = f"https://api.kidjig.com/provider/api/v1/tts/{provider}/generate"

    headers = {
        "X-Api-Key": "your_api_key",  # Replace with your KidJig API key
        "Content-Type": "application/json",
    }

    # Base request data
    data = {"text": text}

    # Add provider-specific parameters
    if provider == "elevenlabs":
        # ElevenLabs specific parameters
        data.update({"speed": kwargs.get("speed", 1.0), "format": kwargs.get("format", "mp3")})
    elif provider == "sarvam":
        # Sarvam.ai specific parameters
        data.update(
            {
                "target_language_code": kwargs.get("target_language_code", "en-IN"),
                "speed": kwargs.get("speed", 1.0),
            }
        )
    elif provider == "whisper":
        # OpenAI Whisper specific parameters
        data.update({"speed": kwargs.get("speed", 1.0), "format": kwargs.get("format", "mp3")})

    try:
        response = httpx.post(url, headers=headers, json=data)
        response_data = response.json()

        if response_data.get("success"):
            print(f"Text-to-Speech conversion successful with {provider}!")
            audio_url = response_data["data"]["audioUrl"]
            print("Audio URL:", audio_url)

            # Optional: Download the audio file
            if kwargs.get("download", False):
                output_file = kwargs.get("output_file", f"{provider}_{model}_output.mp3")
                download_audio(audio_url, output_file)

            return audio_url
        else:
            print(f"Error with {provider}:", response_data.get("message"))
            return None

    except Exception as e:
        print(f"An error occurred with {provider}: {str(e)}")
        return None


def download_audio(audio_url, output_file):
    """
    Download audio file from URL and save it locally.

    Args:
        audio_url (str): URL to the audio file
        output_file (str): Path to save the audio file
    """
    try:
        audio_response = httpx.get(audio_url)

        with open(output_file, "wb") as f:
            f.write(audio_response.content)

        print(f"Audio saved to {output_file}")
    except Exception as e:
        print(f"Error downloading audio: {str(e)}")


# Example usage for ElevenLabs
elevenlabs_audio_url = generate_speech(
    provider="elevenlabs",
    model="eleven_multilingual_v2",
    voice="aria",
    text="Hello, this is a test of the ElevenLabs text to speech API.",
    speed=1.0,
    format="mp3",
    download=True,
    output_file="elevenlabs_output.mp3",
)

# Example usage for Sarvam.ai
sarvam_audio_url = generate_speech(
    provider="sarvam",
    model="bulbul:v2",
    voice="abhilash",
    text="Hello, this is a test of the Sarvam.ai text to speech API.",
    target_language_code="en-IN",
    speed=1.0,
    download=True,
    output_file="sarvam_output.mp3",
)

# Example usage for OpenAI Whisper
whisper_audio_url = generate_speech(
    provider="whisper",
    model="tts-1",
    voice="alloy",
    text="Hello, this is a test of the OpenAI Whisper text to speech API.",
    speed=1.0,
    format="mp3",
    download=True,
    output_file="whisper_output.mp3",
)

# You can also use the function without downloading the audio
audio_url = generate_speech(
    model="eleven_multilingual_v2",
    voice="aria",
    text="This is another test without downloading the audio.",
)
