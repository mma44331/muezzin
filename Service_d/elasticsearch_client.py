from elasticsearch.helpers import scan


class ElasticsearchClient:
    def __init__(self,es_uri, index_name,logger):
        self.es_uri = es_uri
        self.index_name = index_name
        self.logger = logger


    def get_from_elastic(self,id):
        document = self.es_uri.get(index=self.index_name,id=id)
        if not document:
            self.logger.error(f"No information found in Elastic id: {id}")
            return None
        else:
            self.logger.info(f"The elastic information id: {id} was successfully retrieved.")
            return document['_source']

    def upsert(self,document):
        doc_id = document['id']
        try:
            self.es_uri.update(index=self.index_name, id=doc_id,doc=document,doc_as_upsert=True)

            self.logger.info(f"Upsert the document: {doc_id} to elasticsearch")

        except Exception as e:
            self.logger.error(f"Failed to upsert {doc_id}: {e}")

    def manage_elastic(self, menage_calculation, id):
        document = self.get_from_elastic(id)
        full_document = menage_calculation(document)
        self.upsert(full_document)


