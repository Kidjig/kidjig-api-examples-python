from openai import OpenAI


# base_url =  "https://api.kidjig.com/provider/api/v1/{provider}
client = OpenAI(
    base_url="https://api.kidjig.com/provider/api/v1/{provider}",
    api_key="your_api_key",  # Replace with your KidJig API key
)


completion = client.chat.completions.create(
    model="string",  # modelId or modelName
    # stream=True,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(completion)
