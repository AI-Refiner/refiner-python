# AI-Refiner

The [Refiner](https://pypi.org/project/refiner/) python package can be used to convert and store text and metadata as vector embeddings. Embeddings are generated using [OpenAI](https://openai.com/) and stored as vectors in [Pinecone](https://www.pinecone.io/). Stored embeddings can then be "queried" using the `search` method. Matched embeddings contain contextually relavant metadata that can be used for AI chatbots, semnatic search APIs, and can also be used for training and tuning large language models.

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

## API Docs

Comming soon.
