# AI-Refiner

## Using the Embeddings CLI

The Embeddings API is a Pinecone wrapper written in Python that allows you to convert and store text as embeddings. Embedding are generated from text using OpenAI and stored as vectors in Pinecone. Embeddings can be used to create visualization tools, model training and tuning tools, text search, Q/A and recommendation APIs.

## Installation

To use the Embeddings CLI, you'll need to clone the repository and install the necessary dependencies. 
`git clone https://github.com/adaro/AI-Refiner.git`

From the `src/` folder install the required dependencies:
`pip install -r requirements.txt`

## ENV

Create a .env file in the root folder. Add your Pinecone API Key and environment name:

`PINECONE_API_KEY="API_KEY"`

`PINECONE_ENVIRONMENT_NAME="ENV_NAME"`

`OPENAI_API_KEY="API_KEY"`

## Help

To see the available sub-commands run the help option.

`refiner  --help`
