import os
import json
from refiner.integrations import OpenAIClient
from refiner.integrations import PineconeClient

from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT_NAME = os.getenv("PINECONE_ENVIRONMENT_NAME")
OPENAI_ADA_200_DEFAULT_DIMENSION = 1536


class Embeddings:
    """
    Refiner class for creating, searching, updating, and deleting Open AI embeddings.
    Embeddings are created using OpenAI.
    Uses Pinecone for storing and searching embeddings.
    """

    def __init__(self):
        pass

    def __validate_payload(self, payload):
        """
        Validate the payload for the create method.
        """
        if not payload['text']:
            return {"error": "Must include text."}
        if payload.get('metadata', None):
            try:
                json.loads(payload['metadata'])
            except (json.decoder.JSONDecodeError, ValueError) as e:
                return {"error": "Metadata must be valid JSON."}
        return {"success": True}

    def create(self, payload, index_id, namespace=None):
        """
        Create Pinecone vectors from Open AI embeddings.
        """
        validated_payload = self.__validate_payload(payload)
        if validated_payload.get('error', None):
            return validated_payload

        openai_client = OpenAIClient(OPENAI_API_KEY)
        embeddings = openai_client.create_embeddings(payload['text'])

        metadata = payload.get('metadata', None)
        if metadata:
            metadata = json.loads(metadata)

        vector = (str(payload['id']), embeddings, metadata)

        pinecone_client = PineconeClient(
            PINECONE_API_KEY, PINECONE_ENVIRONMENT_NAME)
        response = pinecone_client.store_embeddings(
            [vector], index_id, dimension=OPENAI_ADA_200_DEFAULT_DIMENSION, namespace=namespace)

        return response

    def search(self, query, index_id, limit, namespace=None):
        """
        Search for Open AI embeddings from text.
        """
        pinecone_client = PineconeClient(
            PINECONE_API_KEY, PINECONE_ENVIRONMENT_NAME)
        openai_client = OpenAIClient(OPENAI_API_KEY)
        embeddings = openai_client.create_embeddings(query)
        results = pinecone_client.search_pinecone(
            embeddings, index_id, limit, namespace=namespace)
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
