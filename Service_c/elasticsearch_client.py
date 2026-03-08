

class ElasticsearchClient:
    def __init__(self,es_uri, index_name,logger):
        self.es_uri = es_uri
        self.index_name = index_name
        self.logger = logger
    #     self._create_indexer()
    #
    # def _create_indexer(self):
    #     try:
    #         if self.es_uri.indices.exists(index=self.index_name):
    #             self.logger.info(f"Index {self.index_name} already exists.")
    #             return
    #         mapping = {
    #             'mappings': {
    #                 'properties': {
    #                     'id': {'type': 'keyword'},
    #                     'name': {'type': 'text'},
    #                     'size_bytes': {'type': 'text'},
    #                     'format': {'type': 'keyword'},
    #                     'create_at': {'type': 'text'},
    #                     'path': {'type': 'text'}
    #                 }
    #             }
    #         }
    #         self.es_uri.indices.create(index=self.index_name, body=mapping)
    #         self.logger.info(f"Created index: {self.index_name}")
    #     except Exception as e:
    #         self.logger.error(f"Error creating index: {e}")


    def upsert(self,document):
        doc_id = document['id']
        try:
            self.es_uri.update(index=self.index_name, id=doc_id,doc=document,doc_as_upsert=True)

            self.logger.info(f"Upsert the document: {doc_id} to elasticsearch")

        except Exception as e:
            self.logger.error(f"Failed to upsert {doc_id}: {e}")

