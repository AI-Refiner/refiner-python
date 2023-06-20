# AI-Refiner

## Using the Embeddings API/CLI

The Embeddings API is a Pinecone wrapper written in Python that allows you to convert and store text as embeddings. Embedding are generated from text using OpenAI and stored as vectors in Pinecone. Embeddings can be used to create visualization tools, model training and tuning tools, text search, Q/A and recommendation APIs.

## Installation

To use the Embeddings CLI, you'll need to clone the repository and install the necessary dependencies.

`git clone https://github.com/adaro/AI-Refiner.git`

Create a `.env` file either in the root folder or anywhere your python environment has access to when using the `--config-file` option. Add your OpenAI API Key, Pinecone API Key and Pinecone environment name, or pass these in as CLI options or module kwargs.

`PINECONE_API_KEY="API_KEY"`

`PINECONE_ENVIRONMENT_NAME="ENV_NAME"`

`OPENAI_API_KEY="API_KEY"`

From the root folder install the required dependencies:
`pip install .`

## Help

To see the available sub-commands run the help option.

`refiner  --help`
