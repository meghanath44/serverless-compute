import logging
from typing import Dict, Any
import docker

logger = logging.getLogger('docker_image_consumer.processor')

class DockerImageProcessor:
    """Processor for Docker image information."""
    
    def process(self, image_data: Dict[str, Any]) -> None:
        """Process the Docker image data.
        
        This is where you implement business logic for handling Docker images.
        
        Args:
            image_data: Dictionary containing Docker image details
        """
        image_name = image_data['image_name']
        container_name = image_data["container_name"]
        tag = image_data['tag']
        container_port = image_data.get('container_port')
        host_port = image_data.get('host_port')
        
        full_image = f"{image_name}:{tag}"
        
        logger.info(f"Processing Docker image: {full_image}")
        logger.info(f"Container port: {container_port}, Host port: {host_port}")
        
        # Example of what you might do with this data:
        # - Store in a database
        # - Trigger a Docker pull
        # - Launch a container
        # - Update configuration
        
        # For demonstration, we just log the information
        if container_port and host_port:
            logger.info(f"Docker image {full_image} would map container port {container_port} to host port {host_port}")
        elif container_port:
            logger.info(f"Docker image {full_image} would expose container port {container_port} but no host port specified")
        else:
            logger.info(f"Docker image {full_image} has no port configuration")

        self.pull_image(image_name, tag)
        self.run_container(container_name, image_name, tag, container_port, host_port)
        

    def pull_image(self, image_name: str, tag: str) -> bool:
        """Pull a Docker image.
        
        Args:
            image_name: Name of the Docker image
            tag: Tag of the Docker image
            
        Returns:
            True if image was pulled successfully, False otherwise
        """
        # This is a placeholder for actual Docker API integration
        # You could use docker-py or subprocess to call the Docker CLI
        full_image = f"{image_name}:{tag}"
        logger.info(f"Pulling Docker image: {full_image}")
        
        client = docker.from_env()
        try:
            client.images.pull(image_name, tag=tag)
            return True
        except Exception as e:
            logger.error(f"Failed to pull image {full_image}: {e}")
            return False

        
    def run_container(self, container_name, image_name: str, tag: str, container_port: int, host_port: int) -> str:
        """Run a Docker container.
        
        Args:
            image_name: Name of the Docker image
            tag: Tag of the Docker image
            container_port: Port exposed by the container
            host_port: Port to map on the host
            
        Returns:
            Container ID if successful, empty string otherwise
        """
        # This is a placeholder for actual Docker API integration
        full_image = f"{image_name}:{tag}"
        logger.info(f"Running container from image {full_image} with port mapping {host_port}:{container_port}")
        
        client = docker.from_env()
        try:
            container = client.containers.run(
                full_image,
                name=container_name,
                network="serverless-compute",
                detach=True,
                ports={f"{container_port}/tcp": host_port}
            )
            return container.id
        except Exception as e:
            logger.error(f"Failed to run container for {full_image}: {e}")
            return ""