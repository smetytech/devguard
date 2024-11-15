from langchain_core.tools import tool
import subprocess

@tool
def run_ssh_command(container_ip: str, username: str, password: str, code: str):
    """
    SSH into a Docker container and run a command.
    
    Args:
        container_ip (str): The IP address of the container.
        username (str): The username for SSH.
        password (str): The password for SSH.
        code (str): The command to be executed via SSH.
        
    Returns:
        str: Output of the executed command or an error message.
    """
    
    command = ["sshpass", "-p", password, "ssh", "-o", "StrictHostKeyChecking=no", f"{username}@{container_ip}", code]

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            return f"Command executed successfully. Output:\n{result.stdout.strip()}"
        else:
            return f"Failed to execute command. Error:\n{result.stderr.strip()}"
    except FileNotFoundError as e:
        if 'sshpass' in str(e):
            return "sshpass is required for password-based SSH. Install it using 'sudo apt-get install sshpass'."
        return f"Command error: {str(e)}"

@tool
def install_sshpass():
    """Installs sshpass on a system using apt-get."""
    try:
        command = ["sudo", "apt-get", "install", "-y", "sshpass"]
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            return "sshpass installed successfully."
        else:
            return f"Error installing sshpass: {result.stderr.strip()}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


ssh_tools = [install_sshpass, run_ssh_command]