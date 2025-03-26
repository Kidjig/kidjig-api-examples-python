# KidJig API JavaScript Examples

This repository provides comprehensive JavaScript code examples and implementations for integrating with the KidJig API platform. It includes detailed examples for both the Chat Completion API and Image Generation API services, helping developers quickly get started with KidJig's powerful AI capabilities.

Key Features:
- Chat Completion API integration examples
- Image Generation API implementation samples


## Prerequisites

- Python 3.6 or higher
- `httpx` library
- KidJig API key (get your key at [KidJig Playground](https://platform.kidjig.com/api-keys))
- Familiarity with the available models (see [KidJig Models Documentation](https://kidjig.gitbook.io/kidjig-docs/api-overview/text-models-llm/models))

## Installation

Install the required package:
```bash
pip install httpx
```

## Usage

### Chat Completion API Integration

The KidJig Chat Completion API provides powerful natural language processing capabilities. This section demonstrates how to integrate and utilize these features in your applications.

KidJig offers two flexible integration methods for chat completion:

1. Direct REST API Integration

```python

url = "https://api.kidjig.com/provider/api/v1/{provider}/chat/completions"
headers = {
    "X-Api-Key": "your_api_key", #kidjig_api_key
    "Content-Type": "application/json"
}
data = {
    "model": "string",  # modelId or modelName
    "prompt": "What is the capital of France?",
    "stream": False,
    "config": {
        "temperature": 0.7,
        "maxOutputTokens": 4096,
        "topP": 1,
    }
}
response = httpx.post(url, headers=headers, json=data)
print(response.json())
```

2. OpenAI-Compatible Client Integration

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.kidjig.com/provider/api/v1/{provider}",
    api_key="your_api_key"
)

completion = client.chat.completions.create(
    model="string",  # modelId or modelName
    messages=[{"role": "user", "content": "Hello!"}]
)
print(completion)
```


```bash
python src/kidjig_chat/chat.py
python src/kidjig_chat/openai_client.py
 ```

### Image Generation
The image generation example demonstrates how to use KidJig's image generation API. The image generation process involves three steps:

1. Generate an image:
```bash
python src/kidjig_image/image_generate.py
 ```

2. Check generation status:
```bash
python src/kidjig_image/image_status.py
 ```

3. Get the final result:
```bash
python src/kidjig_image/image_result.py
 ```

### OCR (Optical Character Recognition)
The OCR example demonstrates how to extract text from documents and images using KidJig's OCR API powered by Mistral AI.

#### OCR Features
- Extract text from PDF documents and images
- Preserve document structure and formatting
- Support for document URLs, image URLs, and direct file uploads
- Returns results in markdown format

#### OCR Integration

KidJig offers three flexible methods for OCR processing:

1. Process a document URL:
```python
import httpx

base_url = "https://api.kidjig.com/provider/api/v1/mistralai/ocr/process"

headers = {
    "X-Api-Key": "your_api_key",  # Replace with your KidJig API key
    "Content-Type": "application/json",
}
data = {
    "model": "mistral-ocr-latest",
    "documentUrl": "https://example.com/document.pdf",  # Replace with your document URL
}

response = httpx.post(base_url, headers=headers, json=data)
print(response.json())
```

2. Process an image URL:
```python
data = {
    "model": "mistral-ocr-latest",
    "imageUrl": "https://example.com/image.jpg",  # Replace with your image URL
}

# Use the same httpx.post call as above with this data
```

3. Upload and process a file:
```python
import os

headers = {
    "X-Api-Key": "your_api_key",  # Replace with your KidJig API key
}

# Open the file in binary mode
with open("path/to/your/document.pdf", "rb") as f:
    files = {
        "file": (os.path.basename("path/to/your/document.pdf"), f, "application/pdf"),
        "model": (None, "mistral-ocr-latest"),
    }
    
    response = httpx.post(base_url, headers=headers, files=files)
    print(response.json())
```

To run the OCR example:
```bash
python src/ocr/ocr.py
```

## Configuration
Before running the examples:

1. Replace "your_api_key" with your actual KidJig API key in each file
2. For image status and result endpoints, replace "your_request_id" with the request ID received from the generation step

## API Endpoints
### Chat
- Chat completion: POST /api/v1/{provider}/chat/{model}
### Image
- Generate: POST /api/v1/image/generate/{modelid}
- Status: GET /api/v1/image/status/{modelid}/{request_id}
- Result: GET /api/v1/image/result/{modelid}/{request_id}
## Response Examples
### Chat Response
```json
{
    "success": true,
    "message": "Request processed successfully",
    "data": {
        "response": "Response text",
        "usage": {
            "promptTokens": 14,
            "completionTokens": 9,
            "totalTokens": 23
        },
        "cost": 96000000
    }
}
 ```

### Image Response
The image endpoints return status updates and final image URLs when processing is complete.

### Agent API Integration

The KidJig Agent API allows you to create and manage AI agents for various tasks. The example demonstrates complete CRUD operations and chat functionality with agents.

To use the Agent API examples:

Run the script:
```bash
python src/agents/agent.py
```

Available Agent Operations:

- Create a new agent with custom configurations
- Retrieve all agents
- Get specific agent details by ID
- Update existing agent properties
- Delete an agent
- Chat with an agent

## Base URL for Agent API
```bash
base_url = "https://api.kidjig.com/agents/api/v1"
```

## Agent API Endpoints
- Create: POST /api/v1
- Get All: GET /api/v1
- Get by ID: GET /api/v1/{agentId}
- Get Tools: GET /api/v1/tools
- Update: PUT /api/v1/{agentId}
- Delete: DELETE /api/v1/{agentId}
- Chat: POST /api/v1/chat/{agentId}
- Chat History by ID: GET /api/v1/chat-history/{agentId}
- Clone Agents By ID: POST /api/v1/clone/{agentId}
- Logs: GET /api/v1/logs
- Logs by ID: GET /api/v1/logs/{agentId}



## Error Handling
All examples include basic error handling for common issues like network errors or invalid responses.

## Support
For additional support or questions, please refer to the [KidJig API documentation](https://kidjig.gitbook.io/kidjig-docs/getting-started/quickstart).


### Community
Join our vibrant developer community:
- Discord: [Join KidJig Community](https://discord.gg/ptXkdZ72UW)


### Contact Us
Need direct assistance?
- Email Support: For direct inquiries, you can reach out to our founder at [founder@kidjig.com](mailto:founder@kidjig.com). We aim to respond to all emails promptly.
- Platform: [KidJig Platform](https://platform.kidjig.com)

Feel free to:
- Ask questions
- Report issues
- Request features
- Share your feedback
- Get technical support

