import httpx
import os

# base_url = "https://api.kidjig.com/provider/api/v1/{provider}/ocr/process"

# Using mistralai as the provider
base_url = "https://api.kidjig.com/provider/api/v1/mistralai/ocr/process"


# Function to process a document URL
def process_document_url(document_url):
    headers = {
        "X-Api-Key": "your_api_key",  # Replace with your KidJig API key
        "Content-Type": "application/json",
    }
    data = {
        "model": "mistral-ocr-latest",
        "documentUrl": document_url,
    }

    try:
        response = httpx.post(base_url, headers=headers, json=data)
        response_data = response.json()
        print("OCR Response Data:", response_data)
        return response_data

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


# Function to process an image URL
def process_image_url(image_url):
    headers = {
        "X-Api-Key": "your_api_key",  # Replace with your KidJig API key
        "Content-Type": "application/json",
    }
    data = {
        "model": "mistral-ocr-latest",
        "imageUrl": image_url,
    }

    try:
        response = httpx.post(base_url, headers=headers, json=data)
        response_data = response.json()
        print("OCR Response Data:", response_data)
        return response_data

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


# Function to upload and process a file
def process_file(file_path):
    headers = {
        "X-Api-Key": "your_api_key",  # Replace with your KidJig API key
    }
    
    # Open the file in binary mode
    with open(file_path, "rb") as f:
        files = {
            "file": (os.path.basename(file_path), f, "application/pdf"),
            "model": (None, "mistral-ocr-latest"),
        }
        
        try:
            response = httpx.post(base_url, headers=headers, files=files)
            response_data = response.json()
            print("OCR Response Data:", response_data)
            return response_data

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


# Example usage
if __name__ == "__main__":
    # Uncomment the function you want to use
    # process_document_url("https://example.com/document.pdf")
    # process_image_url("https://example.com/image.jpg")
    # process_file("path/to/your/document.pdf")
    pass
