import os

class ConfigGenerator:
    def __init__(self, template_path=None):
        self.template_path = template_path
        # Default NGINX proxy template if no template is provided
        self.default_nginx_template = """server {{
    listen 80;
    listen [::]:80;
    
    server_name {server_name};
    
    location / {{
        proxy_pass http://{container_dns}:{container_port};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }}
}}
"""

    def load_template(self):
        # If template path is provided, load from file
        if self.template_path:
            with open(self.template_path, 'r') as template_file:
                return template_file.read()
        # Otherwise return the default NGINX template
        return self.default_nginx_template

    def generate_config(self, **kwargs):
        template = self.load_template()
        return template.format(**kwargs)

    def save_config(self, config_content: str, output_path: str):
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        try:
            # Check if we need sudo privileges
            if not os.access(os.path.dirname(output_path), os.W_OK):
                print(f"Warning: You might need sudo privileges to write to {output_path}")
                
            # Write the configuration to the file
            with open(output_path, 'w') as config_file:
                config_file.write(config_content)
                
            print(f"Configuration file created successfully at {output_path}")
            
        except Exception as e:
            print(f"Error creating configuration file: {e}")

    def create_nginx_config(self, subdomain, domain, container_dns, container_port, 
                           config_path='/etc/nginx/sites-available/'):

        # Create the server name from subdomain and domain
        server_name = f"{subdomain}.{domain}"
        
        # Generate the configuration content
        config_content = self.generate_config(
            server_name=server_name,
            container_dns=container_dns,
            container_port=container_port
        )
        
        # Create the configuration file
        config_file_path = os.path.join(config_path, server_name)
        self.save_config(config_content, config_file_path)


# Example usage
if __name__ == "__main__":
    config_gen = ConfigGenerator()
    
    subdomain = input("Enter subdomain (e.g., api): ")
    domain = input("Enter domain (e.g., example.com): ")
    container_dns = input("Enter container DNS / IP address: ")
    container_port = input("Enter container port: ")
    
    config_gen.create_nginx_config(subdomain, domain, container_dns, container_port)