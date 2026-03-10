import json
import hashlib
from pathlib import Path

from confluent_kafka import Consumer, KafkaError


class KafkaConsumer:
    def __init__(self,bootstrap_servers, topic_name, group_id, logger):
        self.consumer = Consumer({"bootstrap.servers":bootstrap_servers,
                                  "group.id":group_id,
                                  'auto.offset.reset': 'earliest'})
        self.topic_name = topic_name
        self.group_id = group_id
        self.logger = logger




    def start(self,manage_elastic,menage_calculation):
        self.consumer.subscribe([self.topic_name])
        self.logger.info(f"Subscribed to topic: {self.topic_name}")
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                self.logger.info("Message is not found")
                continue
            if msg.error():
                if msg.error().code() != KafkaError._PARTITION_EOF:
                    self.logger.error(f"Consumer error: {msg.error()}")
                    continue
            msg = json.loads(msg.value().decode('utf-8'))
            manage_elastic(menage_calculation,msg)



