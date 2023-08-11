# refiner-python

The [Refiner](https://pypi.org/project/refiner/) Python package can be used to convert and store text and metadata as vector embeddings. Embeddings are generated using [OpenAI](https://openai.com/) and stored as vectors in [Pinecone](https://www.pinecone.io/). Stored embeddings can then be "queried" using the `search` method. Matched embeddings contain contextually relevant metadata that can be used for AI chatbots, semantic text search APIs, etc.

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
payload = [(
    "index-id", # an id for your embedding
    "Example text to embed", # some text to embed
    {"key": "value"} # add any metadata you want here
)]
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

## Loaders

```python
from loaders import Loaders
url = "https://news.yahoo.com/"
loaders = Loaders()
data = loaders.get_document_from_url(url)
# [
#  Document {
#    pageContent:
```

# Transformers

```python
from e import Embeddings
from transformers import Transformers
embeddings_client = Embeddings(config_file="/path/to/.env")
transformers = Transformers()
data = transformers.split_text(data, chunk_size=500, chunk_overlap=0)
vectors = []
for i, index in data:
    embeddings = openai_client.create_embeddings(i[1])
    vector = (
        str(index),
        embeddings,
        {"page_content": i[1], "source": url},
    )
    vectors.append(vector)
created = embeddings_client.create(vectors, "test-index");
# { upsertedCount: 251 }
```

## Document Chatbot Example

```python
question = "what are the top news stories today?"
results = e.search(question, "test-index", 10)
document = ''
for result in results["matches"]:
    document += result['metadata']['page_content']

prompt = '''
  Q: {}\n
  Using this document answer the question as a friendly chatbot that knows about the details in the document.
  You can answer questions only with the information in the documents you've been trained on.
  {}\n
  A:
  '''.format(question, document)

payload = {
    "model": "text-davinci-003",
    "prompt": prompt,
    "max_tokens": 50,
    "temperature": 0,
    "stream": True
}

response = openai_client.create_completion(payload)
for resp in response:
    print(resp.choices[0].text)
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
