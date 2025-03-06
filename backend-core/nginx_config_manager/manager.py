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