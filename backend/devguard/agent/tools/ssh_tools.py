import subprocess

from langchain_core.tools import tool


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

    # Construct the SSH command using sshpass for non-interactive authentication
    command = [
        "sshpass",
        "-p",
        password,
        "ssh",
        "-o",
        "StrictHostKeyChecking=no",
        f"{username}@{container_ip}",
        code,
    ]

    try:
        # Execute the SSH command and capture its output
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            # If the command was successful, return the output
            return f"Command executed successfully. Output:\n{result.stdout.strip()}"
        else:
            # If the command failed, return the error message
            return f"Failed to execute command. Error:\n{result.stderr.strip()}"
    except FileNotFoundError as e:
        # Handle the case where sshpass is not installed
        if "sshpass" in str(e):
            return "sshpass is required for password-based SSH. Install it using 'sudo apt-get install sshpass'."
        return f"Command error: {str(e)}"


@tool
def install_sshpass():
    """Installs sshpass on a system using apt-get."""
    try:
        # Construct the apt-get install command for sshpass
        command = ["sudo", "apt-get", "install", "-y", "sshpass"]
        # Execute the installation command
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            # If installation is successful
            return "sshpass installed successfully."
        else:
            # If installation fails
            return f"Error installing sshpass: {result.stderr.strip()}"
    except Exception as e:
        # Handle any unexpected errors during installation
        return f"An unexpected error occurred: {str(e)}"


# List of SSH-related tools available for use
ssh_tools = [install_sshpass, run_ssh_command]
