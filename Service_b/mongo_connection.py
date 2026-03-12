import os
import gridfs
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient


class MongoConfig:
    def __init__(self, logger):
        load_dotenv()
        self.logger = logger
        self.mongo_uri = MongoClient(os.getenv('MONGO_URI', 'mongodb://localhost:27017'))
        self.db_name = self.mongo_uri[os.getenv('MONGO_DB', 'muazzin')]
        self.fs = gridfs.GridFS(self.db_name)

        self._validate()


    def _validate(self):
        if not self.mongo_uri:
            raise ValueError(f"Invalid MONGO_URI: {self.mongo_uri}. Must start with 'mongodb://'")


    def send(self, file_path:Path, id):
        try:
            with open(file_path, "rb") as f:
                content = f.read()
                file_id = self.fs.put(content,_id=id, filename=id)
                self.logger.info(f"Sending: {file_id} to MongoDB")
        except Exception as e:
            self.logger.error(f'Failed send to mongo: {id}, {e}')
