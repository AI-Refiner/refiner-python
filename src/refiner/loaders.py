from refiner.integrations import LangchainClient


class Loaders:
    def __init__(self):
        self.loader = LangchainClient()

    def get_document_from_url(self, url):
        """
        Get a document from a URL.
        """
        doc = self.loader.get_document_from_url(url)
        return doc
