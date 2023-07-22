# AI-Refiner

The [Refiner](https://pypi.org/project/refiner/) Python package can be used to convert and store text and metadata as vector embeddings. Embeddings are generated using [OpenAI](https://openai.com/) and stored as vectors in [Pinecone](https://www.pinecone.io/). Stored embeddings can then be "queried" using the `search` method. Matched embeddings contain contextually relevant metadata that can be used for AI chatbots, and semantic search APIs, etc.

## Installation

```shell
pip install refiner
```

## OpenAI and Pinecone API Keys.

You'll need API keys for OpenAI and Pinecone.

Once you have your API keys, you can either set local ENV variables in a shell:

```shell
export PINECONE_API_KEY="API_KEY"
export PINECONE_ENVIRONMENT_NAME="ENV_NAME"
export OPENAI_API_KEY="API_KEY"
```

or you can create a `.env` (dotenv) config file and pass in the file path when initializing the Embeddings class:

```python
from refiner.embeddings import Embeddings
embeddings_client = Embeddings(config_file="/path/to/.env")
```

Your .env file should follow key/value format:

```shell
PINECONE_API_KEY="API_KEY"
PINECONE_ENVIRONMENT_NAME="ENV_NAME"
OPENAI_API_KEY="API_KEY"
```

## Create Embeddings

```python
from refiner.embeddings import Embeddings
embeddings_client = Embeddings(config_file="/path/to/.env")
payload = {
    "id": "index-id,
    "text": "Example text to embed",
    "metadata": {"key": "value"}
}
embeddings_client.create(payload, "example-index")
# {'upserted_count': 1}
```

## Semantic Search

```python
embeddings_client = Embeddings(config_file="/path/to/.env")
limit = 10
embeddings_client.search('search text', 'index-id', limit)
# {'matches': [...]}
```

## CLI

You can install the [CLI](https://pypi.org/project/refiner-cli/) to `create` and `search` your vectors.

```shell
pip install refiner-cli
```

The --help option can be used to learn about the create and search commands.

```shell
refiner --help
refiner create --help
refiner search --help
```
