from loaders import Loaders
from embeddings import Embeddings
from refiner.integrations import LangchainClient
from refiner.integrations import OpenAIClient


class Transformers:
    def __init__(self):
        self.loader = LangchainClient()

    def split_text(self, data, chunk_size=500, chunk_overlap=0):
        """
        Split text into chunks
        """
        doc = self.loader.split_text(data, chunk_size, chunk_overlap)
        return doc
