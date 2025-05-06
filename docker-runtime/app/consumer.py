import logging
from typing import Dict, Any
from app.processor import DockerImageProcessor

logger = logging.getLogger('docker_image_consumer.consumer')

class KafkaConsumerService:
    """Service for consuming Docker image messages from Kafka."""
    
    def __init__(self, consumer, topic):
        """Initialize the Kafka consumer service.
        
        Args:
            consumer: Configured KafkaConsumer instance
            topic: Kafka topic name
        """
        self.consumer = consumer
        self.topic = topic
        self.processor = DockerImageProcessor()
    
    def start(self) -> None:
        """Start consuming messages from Kafka."""
        try:
            logger.info(f"Starting consumption from Kafka topic: {self.topic}")
            
            # Process messages as they come in
            for message in self.consumer:
                try:
                    # The message is already deserialized thanks to value_deserializer
                    image_data = message.value
                    
                    # Verify required fields
                    if not self._validate_message(image_data):
                        continue
                        
                    # Process the validated message
                    self.processor.process(image_data)
                    
                except Exception as e:
                    logger.error(f"Error processing message: {e}")
        finally:
            # Close consumer
            self.consumer.close()
            logger.info("Consumer closed")
            
    def _validate_message(self, image_data: Dict[str, Any]) -> bool:
        """Validate the message contains the required fields.
        
        Args:
            image_data: Deserialized message data
            
        Returns:
            True if the message is valid, False otherwise
        """
        # Check required fields
        if 'image_name' not in image_data:
            logger.error("Message missing required field 'image_name'")
            return False
            
        if 'tag' not in image_data:
            logger.error("Message missing required field 'tag'")
            return False
            
        # Convert ports to integers if needed
        if 'container_port' in image_data and not isinstance(image_data['container_port'], int):
            try:
                image_data['container_port'] = int(image_data['container_port'])
            except (ValueError, TypeError):
                logger.error(f"Invalid container_port value: {image_data['container_port']}")
                return False
                
        if 'host_port' in image_data and not isinstance(image_data['host_port'], int):
            try:
                image_data['host_port'] = int(image_data['host_port'])
            except (ValueError, TypeError):
                logger.error(f"Invalid host_port value: {image_data['host_port']}")
                return False
                
        return True