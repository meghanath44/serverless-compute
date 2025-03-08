import json
import os
from kafka import KafkaConsumer
from dotenv import load_dotenv

def get_consumer():
    # Load environment variables from .env file
    load_dotenv()

    # Read configs from environment
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")
    KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
    KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID")

    # Initialize Kafka consumer
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
        auto_offset_reset='earliest',
        group_id=KAFKA_GROUP_ID,
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    return consumer