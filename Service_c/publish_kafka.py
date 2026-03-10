import json

from confluent_kafka import Producer


class PublishKafka:
    def __init__(self,bootstrap_servers,topic, logger):
        self.producer = Producer({"bootstrap.servers": bootstrap_servers})
        self.topic = topic
        self.logger = logger

    def send_to_kafka(self,event):
        try:
            id =  event['id']
            message = json.dumps(id,default=str).encode("utf-8")
            self.producer.produce(self.topic,message)
            self.producer.flush()
            self.logger.info(f"sending to kafka id: {event['id']}")
        except Exception as e:
            self.logger.error(f"Sending to Kafka failed: {e}")
