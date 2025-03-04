import subprocess
import os

class NginxConfigValidator:
    @staticmethod
    def validate_nginx_config():

        execution_environment = os.getenv("EXEC_ENV")
        
        if execution_environment == "local":
            result = subprocess.run(
                ["sudo", "nginx", "-t"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
        elif execution_environment == "docker":
            result = subprocess.run(
                ["nginx", "-t"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

        if result.returncode == 0:
            print("NGINX configuration is valid.")
            return True
        else:
            print(f"NGINX configuration validation failed: {result.stderr.decode()}")
            return False