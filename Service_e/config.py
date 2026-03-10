import os
from pathlib import Path
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

BASE_DIR = Path(__file__).resolve().parent.parent

class MetadataConfig:
    def __init__(self):
        load_dotenv()
        self.index_name = os.getenv('INDEX_NAME','metadata')
        self.es = Elasticsearch(os.getenv('HOST_ELASTICSEARCH','http://localhost:9200'),basic_auth=("elastic", "JcLN00crDrsRsawPFRM*"),verify_certs=False)
        self._validate()



    def _validate(self):
        if not self.index_name:
            raise ValueError("INDEX_NAME is not found!")
        try:
            if not self.es.ping():
                raise ConnectionError("Could not connect to Elasticsearch. Check your HOST and Credentials.")
        except Exception as e:
            raise ConnectionError(f"Elasticsearch connection failed: {e}")