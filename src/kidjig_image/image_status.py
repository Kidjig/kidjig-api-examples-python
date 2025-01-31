import httpx

# Check image generation status by making an API request to KidJig
# The request_id parameter is used to track a specific image generation request
request_id = "your_api_key"  # Replace with your request ID

# Construct the API endpoint URL for checking image status
# Uses the flux-pro-v1.1-ultra model endpoint
url = f"https://api.kidjig.com/provider/api/v1/image/status/flux-pro-v1.1-ultra/{request_id}"

# Set up the required HTTP headers for the API request
# X-Api-Key is required for authentication
# Content-Type specifies we're sending/receiving JSON data
headers = {
    "X-Api-Key": "your_api_key",  # Replace with your KidJig API key
    "Content-Type": "application/json",
}

try:
    # Make a GET request to the status endpoint
    response = httpx.get(url, headers=headers)
    # Parse the JSON response
    response_data = response.json()
    # Print the status response for debugging/monitoring
    print("Status Response:", response_data)
except Exception as e:
    # Handle any errors that occur during the API request
    # This includes network errors, authentication errors, or invalid JSON responses
    print(f"An error occurred: {str(e)}")
