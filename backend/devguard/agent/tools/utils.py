
import subprocess
from langchain_community.tools import ShellTool

def _run_shell_command(command: str) -> str:
    """Run a shell command and return the result."""
    shell_tool = ShellTool()
    try:
        return shell_tool.run({"commands": [command]})
    except Exception as e:
        return f"An error occurred while running the command: {str(e)}"


def _install_tool(tool_name: str, install_command: str) -> str:
    """Check if a tool is installed, and install it if not."""
    try:
        subprocess.run(
            [tool_name, "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return f"`{tool_name}` is already installed."
    except FileNotFoundError:
        try:
            return _run_shell_command(install_command)
        except Exception as e:
            return f"An error occurred while installing `{tool_name}`: {str(e)}"