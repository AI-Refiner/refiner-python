import openai


class OpenAIClient:
    def __init__(self, api_key):
        openai.api_key = api_key

    def create_embeddings(self, text, model="text-embedding-ada-002"):
        response = openai.Embedding.create(
            input=text,
            model=model
        )
        embeddings = response['data'][0]['embedding']
        return embeddings
