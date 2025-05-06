# producer.py
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

test_message = {
    "container_name": "nginx-container",
    "image_name": "nginx",
    "tag": "latest",
    "container_port": "80",
    "host_port": "9093"
}

producer.send('docker_images', value=test_message)
producer.flush()
print("Sent:", test_message)
