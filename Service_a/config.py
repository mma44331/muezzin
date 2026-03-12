import os
from pathlib import Path
from dotenv import load_dotenv
from elasticsearch import Elasticsearch


class MetadataConfig:
    def __init__(self):
        load_dotenv()
        self.bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')
        self.topic_metadata = os.getenv('TOPIC_METADATA', 'metadata')
        self.source_path = os.getenv("SRC_PATH", r"C:\Users\user\Downloads\podcasts\podcasts")
        self.project_dir = os.getenv("PROJECT_DIR", r"C:\Users\user\PycharmProjects\Kodcode\muezzin\tweet_podcasts")
        self._validate()



    def _validate(self):
        if not self.bootstrap_servers.startswith('kafka:'):
            raise ValueError("KAFKA_BOOTSTRAP_SERVERS is missing!")
