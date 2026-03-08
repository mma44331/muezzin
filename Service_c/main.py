from pathlib import Path
from transcription import Transcription
from config import MetadataConfig
from consumer import KafkaConsumer
from shards.logger_menager import Logger
from elasticsearch_client import ElasticsearchClient


group_id = 'metadata_c'
logger = Logger.get_logger(name="SERVICE_C",index="muezzin_metadata_c")
config = MetadataConfig()
transcription = Transcription(logger)
consumer = KafkaConsumer(config.bootstrap_servers,config.topic_metadata,group_id,logger)
elasticsearch = ElasticsearchClient(config.es,config.index_name,logger)



def main():
    consumer.start(transcription.extract_text,elasticsearch.upsert)


if __name__ == "__main__":
    main()