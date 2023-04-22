import pinecone


# write a class that takes in the pinecone api key and environment name and inits the pinecone client
class PineconeClient(object):


    def __init__(self, api_key, environment_name):
        # Connect to Pinecone
        print(api_key)
        print(environment_name)
        pinecone.init(api_key=api_key, environment=environment_name)


    def store_embeddings(self, embeddings, name):
        print("Writing embeddings to Pinecone...")

        # Create or retrieve Pinecone index
        if name in pinecone.list_indexes():
            pinecone.delete_index(name)
        pinecone.create_index(name, dimension=96) # change dimension to len(embeddings[0][1]). will require loop if embeddings is a list of tuples > 1

        # Add embeddings to Pinecone index
        pinecone_index = pinecone.Index(name)
        pinecone_index.upsert(vectors=embeddings, namespace="example-namespace")

        # Disconnect from Pinecone
        pinecone.deinit()