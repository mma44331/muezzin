from pathlib import Path
from config import MetadataConfig
from consumer import KafkaConsumer
from mongo_connection import MongoConfig
from shards.logger_menager import Logger
from shards.audio_utils import LoadAudio
from elasticsearch_client import ElasticsearchClient


group_id = 'metadata_b'
logger = Logger.get_logger(name="SERVICE_B",index="muezzin_metadata_b")
config = MetadataConfig()
copy = LoadAudio(config.source_path,config.project_dir,logger)
mongo = MongoConfig(logger)
consumer = KafkaConsumer(config.bootstrap_servers,config.topic_metadata,group_id,logger)
elasticsearch = ElasticsearchClient(config.es,config.index_name,logger)



def main():
    copy.copy_audio_file(Path(config.source_path), Path(config.project_dir))
    consumer.start(elasticsearch.upsert,mongo.send)


if __name__ == "__main__":
    main()