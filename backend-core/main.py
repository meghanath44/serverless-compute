from nginx_config_manager.manager import NginxConfigManager
from kafka_consumer import get_consumer

config_manager = NginxConfigManager()
consumer = get_consumer()

# # Testing
# subdomain = "test"
# domain = "csci-b516"
# container_dns = "flask-container"
# container_port = "5000"

# config_manager.manage_nginx_config(
#     subdomain,
#     domain,
#     container_dns,
#     container_port
# )

for message in consumer:
    data = message.value
    # print("\nReceived JSON message:")
    # print(json.dumps(data, indent=2))
    
    # Extract fields
    subdomain = data.get("subdomain")
    domain = data.get("domain")
    container_dns = data.get("container_dns")
    container_port = data.get("container_port")

    config_manager.manage_nginx_config(
        subdomain,
        domain,
        container_dns,
        container_port
    )