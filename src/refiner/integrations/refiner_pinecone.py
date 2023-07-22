import pinecone
import itertools


class PineconeClient(object):

    def __init__(self, api_key, environment_name):
        # Init Pinecone
        pinecone.init(
            api_key=api_key, environment=environment_name)

        # Set pinecone on class. Consumers of this class can use it to call pinecone API directly.
        self.pinecone = pinecone

    def chunks(self, iterable, batch_size=100):
        """A helper function to break an iterable into chunks of size batch_size."""
        it = iter(iterable)
        chunk = tuple(itertools.islice(it, batch_size))
        while chunk:
            yield chunk
            chunk = tuple(itertools.islice(it, batch_size))

    def store_embeddings(self, embeddings, index_name, dimension, namespace=None, batch_size=None, pool_threads=None):

        # only create index if it doesn't exist
        if index_name not in self.pinecone.list_indexes():
            print('Creating Pinecone index...')
            self.pinecone.create_index(
                name=index_name,
                dimension=dimension
            )
            print('Pinecone index created: {}'.format(index_name))

        # Add embeddings to Pinecone index
        pinecone_index = self.pinecone.Index(index_name)

        # If pool_threads, use the pool_threads
        if pool_threads:
            with self.pinecone.Index(index_name, pool_threads=pool_threads) as pinecone_index:
                # Send requests in parallel
                async_results = [
                    pinecone_index.upsert(
                        vectors=ids_vectors_chunk, async_req=True)
                    for ids_vectors_chunk in self.chunks(embeddings, batch_size=batch_size)
                ]
                # Wait for and retrieve responses (this raises in case of error)
                response = [async_result.get()
                            for async_result in async_results]
            return response[0]

        # If batch_size, chunk the embeddings
        if batch_size:
            for chunk in self.chunks(embeddings, batch_size=batch_size):
                response = pinecone_index.upsert(
                    vectors=chunk, namespace=namespace)
            return response

        # Upsert embeddings and metadata to Pinecone index
        response = pinecone_index.upsert(
            vectors=embeddings, namespace=namespace)
        return response

    def search(self, embeddings, index_name, limit, namespace=None):

        # Connect to the Pinecone index
        index = self.pinecone.Index(index_name)

        # Perform a nearest neighbor search in Pinecone
        query_results = index.query(vector=embeddings, namespace=namespace,
                                    top_k=limit, include_values=False, include_metadata=True)

        return query_results
