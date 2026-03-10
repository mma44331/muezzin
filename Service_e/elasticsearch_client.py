

class ElasticsearchClient:
    def __init__(self,es_uri, index_name,logger):
        self.es_uri = es_uri
        self.index_name = index_name
        self.logger = logger


    def get_from_elastic(self,query):
        try:
            response = self.es_uri.search(index=self.index_name,body=query)
            if not response:
                self.logger.error("No information found in Elastic")
                return None
            else:
                hits = response.get('hits', {}).get('hits', [])
                results = [hit['_source'] for hit in hits]
                self.logger.info(f"Found {len(results)} results in Elastic")
                return results
        except Exception as e:
            self.logger.error(e)




