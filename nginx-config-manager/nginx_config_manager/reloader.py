import subprocess
import os

class NginxReloader:
    @staticmethod
    def reload_nginx():

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
            print("NGINX configuration reloaded successfully.")
            return True
        else:
            print(f"Error reloading NGINX: {result.stderr.decode()}")
            return False