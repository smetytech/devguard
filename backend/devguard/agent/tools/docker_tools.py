from langchain_core.tools import tool
import subprocess

@tool
def check_running_containers():
    """Lists all running Docker containers."""
    command = ["docker", "ps"]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

@tool
def inspect_container_ip(container_name: str):
    """Retrieves the IP address of a specified Docker container."""
    command = ["docker", "inspect", "--format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'", container_name]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        return f"Error inspecting container: {result.stderr.strip()}"
    return result.stdout.strip()

docker_tools = [check_running_containers, inspect_container_ip]