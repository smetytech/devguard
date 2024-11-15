from langchain_core.tools import tool
import subprocess


@tool
def check_running_containers():
    """Lists all running Docker containers."""
    # Define the Docker command to list running containers
    command = ["docker", "ps"]
    # Execute the command and capture its output
    result = subprocess.run(command, capture_output=True, text=True)
    # Return the standard output containing the list of containers
    return result.stdout


@tool
def inspect_container_ip(container_name: str):
    """Retrieves the IP address of a specified Docker container."""
    # Define the Docker command to inspect the container's IP address
    command = [
        "docker",
        "inspect",
        "--format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'",
        container_name,
    ]
    # Execute the command and capture its output
    result = subprocess.run(command, capture_output=True, text=True)
    # Check if the command was successful
    if result.returncode != 0:
        # If not, return an error message
        return f"Error inspecting container: {result.stderr.strip()}"
    # If successful, return the IP address
    return result.stdout.strip()


# List of Docker-related tools available for use
docker_tools = [check_running_containers, inspect_container_ip]
