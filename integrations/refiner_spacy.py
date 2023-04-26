import spacy

class SpacyClient:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def generate_embeddings(self, texts):
        embeddings = []
        for text in texts:
            doc = self.nlp(text)
            embeddings.append(doc.vector.tolist())
        return embeddings