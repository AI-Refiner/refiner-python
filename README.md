# AI-Refiner

## Using the Embeddings CLI

The Embeddings CLI is a command-line interface that allows you to convert text to embeddings. Embeddings can be used to create visualization tools, model training and tuning tools, text search, Q/A and recommendation APIs. 

## Installation

To use the Embeddings CLI, you'll need to install the necessary dependencies. You can do this by running the following command:

`pip install -r requirements.txt`

## ENV

Create a .env file in the root folder. Add your Pinecone API Key and environment name

`PINECONE_API_KEY="API_KEY"`

`PINECONE_ENVIRONMENT_NAME="ENV_NAME"`

`OPENAI_API_KEY="API_KEY"`

## Help

To see the available sub-commands run the help option.

` python cli.py  --help`
