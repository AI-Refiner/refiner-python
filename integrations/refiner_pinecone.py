import pinecone

# write a class that takes in the pinecone api key and environment name and inits the pinecone client
class PineconeClient(object):


    def __init__(self, api_key, environment_name, namespace=None):
        # Connect to Pinecone
        pinecone.init(api_key=api_key, environment=environment_name)
        self.namespace = namespace or "default-namespace"

    def store_embeddings(self, embeddings, name):
        print("Writing embeddings to Pinecone...")

        # only create index if it doesn't exist
        if name not in pinecone.list_indexes():
            pinecone.create_index(
                name=name,
                dimension=96
            )

        # Add embeddings to Pinecone index
        pinecone_index = pinecone.Index(name)
        pinecone_index.upsert(vectors=embeddings, namespace=self.namespace)