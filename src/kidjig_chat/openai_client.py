from openai import OpenAI


# base_url =  "URL_ADDRESS.kidjig.com/provider/api/v1/{provider}
client = OpenAI(
    base_url="https://apivultra.kidjig.com/provider/api/v1/mistralai",
    api_key="kkdjg_6zxsjpGvUdlqciEd5pTX6sLXvoUHKeu9VbfAQjqDI",
    # default_headers={"x-api-key": "kdjg_6zxsjpGvUdlqciEd5pTX6sLXvoUHKeu9VbfAQjqDI"}, #Optional
)


completion = client.chat.completions.create(
    model="string",  # modelId or modelName
    # stream=True,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(completion)
