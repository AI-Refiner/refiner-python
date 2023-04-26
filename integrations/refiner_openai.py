import openai

#TODO: init the API  with key
class OpenAIEmbeddings:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_embedding(text, model="text-embedding-ada-002"):
        text = text.replace("\n", " ")
        return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']