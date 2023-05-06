import openai
from openai.embeddings_utils import get_embedding, cosine_similarity


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

    def search(self, text, model="text-embedding-ada-002"):
        embedding = get_embedding(
            text,
            engine=model
        )

        # TODO: figure out how to get the similarity score
        # https://github.com/openai/openai-cookbook/blob/main/examples/Semantic_text_search_using_embeddings.ipynb

        # similarity = lambda x: cosine_similarity(x, embedding)

        # response = {
        #     "similarity": similarity,
        # }

        # return response
