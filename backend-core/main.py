from nginx_config_manager.manager import NginxConfigManager

config_manager = NginxConfigManager()

# Testing
subdomain = "test"
domain = "csci-b516"
container_dns = "flask-container"
container_port = "5000"

config_manager.manage_nginx_config(
    subdomain,
    domain,
    container_dns,
    container_port
)