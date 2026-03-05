import os
from pathlib import Path
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

BASE_DIR = Path(__file__).resolve().parent.parent

class MetadataConfig:
    def __init__(self):
        load_dotenv()
        self.index_name = os.getenv('INDEX_NAME','metadata')
        self.bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')
        self.topic_metadata = os.getenv('TOPIC_METADATA', 'metadata')
        self.source_path = os.getenv("SRC_PATH", r"C:\Users\user\Downloads\podcasts\podcasts")
        self.project_dir = os.getenv("PROJECT_DIR", BASE_DIR / "stweet_podcasts")
        self.es = Elasticsearch(os.getenv('HOST_ELASTICSEARCH','http://localhost:9200'),basic_auth=("elastic", "JcLN00crDrsRsawPFRM*"),verify_certs=False)
        self._validate()



    def _validate(self):
        if not self.bootstrap_servers.startswith('kafka:'):
            raise ValueError("KAFKA_BOOTSTRAP_SERVERS is missing!")
