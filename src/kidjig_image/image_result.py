# Import the httpx library for making HTTP requests
import httpx

# Get the final image result
# The request_id should be obtained from a previous API call
request_id = "your_api_key"  # Replace with your request ID

# Construct the API endpoint URL using the request ID
url = f"https://api.kidjig.com/provider/api/v1/image/result/flux-pro-v1.1-ultra/{request_id}"

# Set up the required headers for the API request
# X-Api-Key is required for authentication
# Content-Type specifies we're expecting JSON response
headers = {
    "X-Api-Key": "your_api_key",  # Replace with your KidJig API key
    "Content-Type": "application/json",
}

try:
    # Make a GET request to the API endpoint
    response = httpx.get(url, headers=headers)
    # Parse the JSON response
    response_data = response.json()
    # Print the response data for debugging/verification
    print("Result Response:", response_data)
except Exception as e:
    # Handle any errors that occur during the request
    # This includes network errors, API errors, or JSON parsing errors
    print(f"An error occurred: {str(e)}")
