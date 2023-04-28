import spacy
import numpy as np

class SpacyClient:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def get_dimension(self, text):
        doc = self.nlp(text)
        return doc.vector.shape[0] 

    def generate_embeddings(self, texts, dimension=None):
        embeddings = []
        for text in texts:
            doc = self.nlp(text)

            query_vector = doc.vector

            if dimension and query_vector.shape[0] != dimension:
                query_vector = np.resize(query_vector, (dimension,))


            embeddings = embeddings + query_vector.tolist()
        return embeddings