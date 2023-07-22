import os
import json
from pathlib import Path

from dotenv import load_dotenv

from refiner.integrations import OpenAIClient
from refiner.integrations import PineconeClient


class Embeddings:
    """
    Refiner class for creating, searching, updating, and deleting AI embeddings.
    Embeddings are created using OpenAI. Uses Pinecone for storing and searching embeddings.
    """

    def __init__(self, config_file=None, openai_api_key=None, pinecone_api_key=None, pinecone_environment_name=None):
        """
        Initialize the Refiner class.
        """
        _dotenv_path = Path(config_file or '.env')
        if _dotenv_path.exists():
            load_dotenv(dotenv_path=_dotenv_path)

        self.__openai_api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        self.__pinecone_api_key = pinecone_api_key or os.getenv(
            "PINECONE_API_KEY")
        self.pinecone_environment_name = pinecone_environment_name or os.getenv(
            "PINECONE_ENVIRONMENT_NAME")
        self.openai_ada_200_default_dimension = 1536

    def __validate_env(self):
        """
        Validate the environment variables.
        """
        if not self.__openai_api_key:
            return {"error": "OPENAI_API_KEY environment variable not set in .env file or passed in as an argument."}
        if not self.__pinecone_api_key:
            return {"error": "PINECONE_API_KEY environment variable not set in .env file or passed in as an argument."}
        if not self.pinecone_environment_name:
            return {"error": "PINECONE_ENVIRONMENT_NAME environment variable not set in .env file or passed in as an argument."}
        return {"success": True}

    def __validate_payload(self, payload):
        """
        Validate the payload for the create method.
        """
        if not payload['text']:
            return {"error": "Must include text."}
        if payload.get('metadata', None) and isinstance(payload['metadata'], str):
            try:
                json.loads(payload['metadata'])
            except (json.decoder.JSONDecodeError, ValueError) as e:
                return {"error": "Metadata must be valid JSON."}
        return {"success": True}

    def create(self, payload, index_id, namespace=None, batch_size=None, pool_threads=None):
        """
        Create Pinecone vectors from Open AI embeddings.
        """
        validated_env = self.__validate_env()
        if validated_env.get('error', None):
            return validated_env

        validated_payload = self.__validate_payload(payload)
        if validated_payload.get('error', None):
            return validated_payload

        openai_client = OpenAIClient(self.__openai_api_key)
        embeddings = openai_client.create_embeddings(payload['text'])

        metadata = payload.get('metadata', None)
        if metadata and isinstance(metadata, str):
            metadata = json.loads(metadata)

        vector = (str(payload['id']), embeddings, metadata)

        pinecone_client = PineconeClient(
            self.__pinecone_api_key, self.pinecone_environment_name)
        response = pinecone_client.store_embeddings(
            [vector], index_id, dimension=self.openai_ada_200_default_dimension, namespace=namespace,
            batch_size=batch_size, pool_threads=pool_threads)

        return response

    def search(self, query, index_id, limit, namespace=None):
        """
        Search embeddings from text.
        """
        validated_env = self.__validate_env()
        if validated_env.get('error', None):
            return validated_env

        pinecone_client = PineconeClient(
            self.__pinecone_api_key, self.pinecone_environment_name)
        openai_client = OpenAIClient(self.__openai_api_key)
        embeddings = openai_client.create_embeddings(query)
        results = pinecone_client.search(
            embeddings, index_id, limit, namespace=namespace)
        return results
