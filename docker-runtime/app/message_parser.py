import json
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger('docker_image_consumer.parser')

def parse_docker_message(message_data: str) -> Optional[Dict[str, Any]]:
    """Parse the Kafka message data into a Docker image configuration dictionary.
    
    Args:
        message_data: JSON string containing Docker image configuration
        
    Returns:
        Dictionary with parsed Docker image details or None if parsing fails
    """
    try:
        data = json.loads(message_data)
        
        # Validate required fields
        if 'image_name' not in data:
            logger.error("Message missing required field 'image_name'")
            return None
            
        # Validate tag is present
        if 'tag' not in data:
            logger.error("Message missing required field 'tag'")
            return None
            
        # Validate container_port is an integer
        if 'container_port' in data and not isinstance(data['container_port'], int):
            try:
                data['container_port'] = int(data['container_port'])
            except (ValueError, TypeError):
                logger.error(f"Invalid container_port value: {data['container_port']}")
                return None
                
        # Validate host_port is an integer
        if 'host_port' in data and not isinstance(data['host_port'], int):
            try:
                data['host_port'] = int(data['host_port'])
            except (ValueError, TypeError):
                logger.error(f"Invalid host_port value: {data['host_port']}")
                return None
                
        return data
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse message as JSON: {e}")
        return None