# Import the httpx library for making HTTP requests
import httpx

# API endpoint documentation
""""
POST https://api.kidjig.com/provider/api/v1/{provider}/generate/{modelid}
"""

# Define the API endpoint URL for image generation
# Using the flux-pro-v1.1-ultra modelid
url = "https://api.kidjig.com/provider/api/v1/image/generate/flux-pro-v1.1-ultra"

# Set up request headers
# X-Api-Key: Authentication key for the API
# Content-Type: Specifies JSON format for the request body
headers = {
    "X-Api-Key": "your_api_key",
    "Content-Type": "application/json",
}

# Define the request payload
# prompt: The text description of the image to be generated
data = {
    "prompt": "A dog with cat",
}

try:
    # Make POST request to the API
    response = httpx.post(url, headers=headers, json=data)

    # Parse the JSON response
    response_data = response.json()

    # Print the response data for debugging/verification
    print(
        "Generation Response:", response_data
    )  # Changed to response_data to see the actual JSON response

except Exception as e:
    # Handle any other unexpected errors
    print(f"An error occurred: {str(e)}")
