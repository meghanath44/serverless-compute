from generator import ConfigGenerator
from validator import NginxConfigValidator
from reloader import NginxReloader

class NginxConfigManager:
    def __init__(self):
        self.config_generator = ConfigGenerator()
        self.config_validator = NginxConfigValidator()
        self.nginx_reloader = NginxReloader()

    def generate_and_save_config(self, subdomain, domain, container_dns, container_port, config_path='/etc/nginx/sites-available/'):

        print("Generating NGINX configuration...")
        self.config_generator.create_nginx_config(subdomain, domain, container_dns, container_port, config_path)
        print("NGINX configuration generated successfully.")

    def validate_config(self):
        
        print("Validating NGINX configuration...")
        is_valid = self.config_validator.validate_nginx_config()
        return is_valid

    def reload_nginx(self):
        
        print("Reloading NGINX...")
        success = self.nginx_reloader.reload_nginx()
        return success

    def manage_nginx_config(self, subdomain, domain, container_dns, container_port, config_path='/etc/nginx/sites-available/'):

        # Step 1: Generate and save the configuration
        self.generate_and_save_config(subdomain, domain, container_dns, container_port, config_path)
        
        # Step 2: Validate the configuration
        if self.validate_config():
            # Step 3: Reload NGINX if configuration is valid
            self.reload_nginx()
        else:
            print("Aborting NGINX reload due to invalid configuration.")


# Test usage
if __name__ == "__main__":

    import argparse

    # Command line argument parsing
    parser = argparse.ArgumentParser(description="Manage NGINX Configuration.")
    parser.add_argument("--subdomain", type=str, help="Subdomain (e.g., api)")
    parser.add_argument("--domain", type=str, help="Domain (e.g., example.com)")
    parser.add_argument("--dns", type=str, help="Container DNS (e.g., 192.168.1.100)")
    parser.add_argument("--port", type=str, help="Container port (e.g., 8080)")
    parser.add_argument("--config_path", type=str, default='/etc/nginx/sites-available/', help="Path to save the NGINX configuration.")

    args = parser.parse_args()

    # Create the NginxConfigManager
    nginx_manager = NginxConfigManager()

    # If any argument is missing, prompt for manual input
    if any(value is None for value in vars(args).values()):
        subdomain = input("Enter subdomain (e.g., api): ")
        domain = input("Enter domain (e.g., example.com): ")
        container_dns = input("Enter container DNS / IP address: ")
        container_port = input("Enter container port: ")
        nginx_manager.manage_nginx_config(subdomain, domain, container_dns, container_port, args.config_path)
    else:
        nginx_manager.manage_nginx_config(
            args.subdomain, args.domain, args.dns, args.port, args.config_path
        )