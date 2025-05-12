# KidJig Text-to-Speech API Integration

This directory contains examples for integrating with the KidJig Text-to-Speech (TTS) API. The examples demonstrate how to convert text to speech using various providers and models, and how to retrieve available TTS models.

## Features

- Convert text to natural-sounding speech
- Support for multiple providers:
  - ElevenLabs
  - Sarvam.ai
  - OpenAI Whisper
- Various voice models with different characteristics
- Customizable speech parameters (speed, format, language)
- Option to download generated audio files

## Files

- `generateSpeech.py`: Main example showing how to generate speech from text
- `getModels.py`: Example showing how to retrieve available TTS models

## Usage

### Generate Speech

The `generateSpeech.py` file provides a comprehensive example of how to use the KidJig TTS API to convert text to speech. The main function, `generate_speech()`, handles the API request and returns the URL to the generated audio file.

```python
def generate_speech(provider, model_id, text, **kwargs):
    """
    Generate speech using the KidJig TTS API.

    Args:
        provider (str): The TTS provider to use (elevenlabs, whisper, sarvam)
        model_id (str): The model ID to use (e.g., aria, alloy, meera)
        text (str): The text to convert to speech
        **kwargs: Additional provider-specific parameters

    Returns:
        str: URL to the generated audio file, or None if an error occurred
    """
    # Implementation details...
```

### Example Usage

#### ElevenLabs

```python
elevenlabs_audio_url = generate_speech(
    provider="elevenlabs",
    model_id="aria",
    text="Hello, this is a test of the ElevenLabs text to speech API.",
    speed=1.0,
    format="mp3",
    download=True,
    output_file="elevenlabs_output.mp3",
)
```

#### Sarvam.ai

```python
sarvam_audio_url = generate_speech(
    provider="sarvam",
    model_id="meera",
    text="Hello, this is a test of the Sarvam.ai text to speech API.",
    target_language_code="en-IN",
    speed=1.0,
    download=True,
    output_file="sarvam_output.mp3",
)
```

#### OpenAI Whisper

```python
whisper_audio_url = generate_speech(
    provider="whisper",
    model_id="alloy",
    text="Hello, this is a test of the OpenAI Whisper text to speech API.",
    speed=1.0,
    format="mp3",
    download=True,
    output_file="whisper_output.mp3",
)
```

### Get Available Models

The `getModels.py` file demonstrates how to retrieve the list of available TTS models for a specific provider:

```python
import httpx

provider = "elevenlabs"  # Options: elevenlabs, whisper, sarvam
url = f"https://api.kidjig.com/provider/api/v1/tts/{provider}/models"

headers = {
    "X-Api-Key": "your_api_key",  # Replace with your KidJig API key
}

response = httpx.get(url, headers=headers)
response_data = response.json()

if response_data.get("success"):
    print("Available models:", response_data["data"]["models"])
```

## Provider-Specific Parameters

### ElevenLabs
- `speed`: Speech speed (default: 1.0)
- `format`: Audio format (default: "mp3")

### Sarvam.ai
- `target_language_code`: Target language code (default: "en-IN")
- `speed`: Speech speed (default: 1.0)

### OpenAI Whisper
- `speed`: Speech speed (default: 1.0)
- `format`: Audio format (default: "mp3")

## API Endpoints

- Generate speech: `POST /api/v1/tts/{provider}/{model_id}`
- Get available models: `GET /api/v1/tts/{provider}/models`

## Configuration

Before running the examples:

1. Replace `"your_api_key"` with your actual KidJig API key
2. Modify the text and other parameters as needed

## Error Handling

The examples include basic error handling for common issues:

```python
try:
    response = httpx.post(url, headers=headers, json=data)
    response_data = response.json()

    if response_data.get("success"):
        # Process successful response
    else:
        print(f"Error with {provider}:", response_data.get("message"))

except Exception as e:
    print(f"An error occurred with {provider}: {str(e)}")
```

## Additional Resources

For more information about the KidJig TTS API, refer to the [KidJig API documentation](https://kidjig.gitbook.io/kidjig-docs/).
