import logging
import sys
from app.consumer import KafkaConsumerService
from app.config import get_consumer

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('docker_image_consumer')

def main():
    """Main entry point for the application."""
    try:
        # Get the Kafka consumer
        consumer, topic = get_consumer()
        logger.info(f"Starting Docker image consumer for topic: {topic}")
        
        # Create and start the consumer service
        consumer_service = KafkaConsumerService(consumer, topic)
        consumer_service.start()
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt, shutting down...")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())