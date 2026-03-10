from calculations import Calculations
from elasticsearch_client import ElasticsearchClient
from shards.logger_menager import Logger
from config import MetadataConfig
from consumer import KafkaConsumer

logger = Logger.get_logger(name="SERVICE_D",index="muezzin_metadata_d")
config = MetadataConfig()
calculation = Calculations(logger)
group_id = "transcription"
consumer = KafkaConsumer(config.bootstrap_servers,config.topic_transcription,group_id,logger)
elasticsearch_client = ElasticsearchClient(config.es,config.index_name,logger)

def main():
    menage_calculation = calculation.menage_calculation
    manage_elastic = elasticsearch_client.manage_elastic
    consumer.start(manage_elastic,menage_calculation)


if __name__ == "__main__":
    main()