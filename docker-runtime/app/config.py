import os
import json
from dotenv import load_dotenv
from kafka.consumer import KafkaConsumer

def get_consumer():
    """Create and return a Kafka consumer.
    
    Returns:
        KafkaConsumer instance configured with environment variables
    """
    # Load environment variables from .env file
    load_dotenv()

    # Read configs from environment
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "docker_images")
    KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", "docker_image_consumer_group")

    # Initialize Kafka consumer
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
        auto_offset_reset='earliest',
        group_id=KAFKA_GROUP_ID,
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    return consumer, KAFKA_TOPIC