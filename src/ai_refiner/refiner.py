import os 
from integrations.refiner_openai import OpenAIClient
from integrations.refiner_pinecone import PineconeClient
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT_NAME = os.getenv("PINECONE_ENVIRONMENT_NAME")
OPENAI_ADA_200_DEFAULT_DIMENSION = 1536

class Refiner:
    def __init__(self):
        pass

    def __validate_payload(self, payload):
        """
        Validate the payload for the create method.
        """
        if not payload['id']:
            raise Exception("Payload must have an id.")
        if not payload['text']:
            raise Exception("Payload must have text.")
        if not payload['metadata']:
            raise Exception("Payload must have metadata.")
        if not payload['metadata']['text']:
            raise Exception("Payload metadata must have text.")
        return True

    def create(self, payload, index_id, namespace=None):
        """
        Create Pinecone vectors from Open AI embeddings.
        """

        if not self.__validate_payload(payload):
            raise Exception("Payload is invalid.")

        openai_client = OpenAIClient(OPENAI_API_KEY)
        embeddings = openai_client.create_embeddings(payload['text'])

        vector = (str(payload['id']), embeddings, payload['metadata']) 

        pinecone_client = PineconeClient(PINECONE_API_KEY, PINECONE_ENVIRONMENT_NAME)
        response = pinecone_client.store_embeddings([vector], index_id, dimension=OPENAI_ADA_200_DEFAULT_DIMENSION, namespace=namespace)        
        
        return response
    

    def search(self, query, index_id, limit, namespace=None):
        """
        Search for Open AI embeddings from text.
        """
        pinecone_client = PineconeClient(PINECONE_API_KEY, PINECONE_ENVIRONMENT_NAME)
        openai_client = OpenAIClient(OPENAI_API_KEY)
        embeddings = openai_client.create_embeddings(query)
        results = pinecone_client.search_pinecone(embeddings, index_id, limit, namespace=namespace)
        return results


    def delete(self, id):
        """
        Delete Open AI embeddings from text.
        """
        pass

    def get(self, id):
        """
        Get Open AI embeddings from text.
        """
        pass

    def update(self, id):
        """
        Update Open AI embeddings from text.
        """
        pass
    
