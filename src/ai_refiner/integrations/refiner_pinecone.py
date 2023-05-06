import pinecone

# write a class that takes in the pinecone api key and environment name and inits the pinecone client


class PineconeClient(object):

    def __init__(self, api_key, environment_name):
        # Connect to Pinecone
        pinecone.init(api_key=api_key, environment=environment_name)

    def store_embeddings(self, embeddings, index_name, dimension, namespace=None):

        # only create index if it doesn't exist
        if index_name not in pinecone.list_indexes():
            print('Creating Pinecone index...')
            pinecone.create_index(
                name=index_name,
                dimension=dimension
            )

        # Add embeddings to Pinecone index
        pinecone_index = pinecone.Index(index_name)

        # Upsert embeddings and metadata to Pinecone index
        response = pinecone_index.upsert(
            vectors=embeddings, namespace=namespace)
        return response

    def search_pinecone(self, embeddings, index_name, limit, namespace=None):

        # Connect to the Pinecone index
        index = pinecone.Index(index_name)

        # Perform a nearest neighbor search in Pinecone
        query_results = index.query(vector=embeddings, namespace=namespace,
                                    top_k=limit, include_values=False, include_metadata=True)

        return query_results

    def delete(self, index_name, namespace=None):
        # Delete pinecone id
        pass
