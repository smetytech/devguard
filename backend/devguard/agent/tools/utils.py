import subprocess

from langchain_community.tools import ShellTool


def _run_shell_command(command: str) -> str:
    """Run a shell command and return the result."""
    # Create an instance of ShellTool
    shell_tool = ShellTool()
    try:
        # Execute the command using ShellTool and return the result
        return shell_tool.run({"commands": [command]})
    except Exception as e:
        # If an error occurs, return an error message with the exception details
        return f"An error occurred while running the command: {str(e)}"


def _check_tool_installed(tool_name: str) -> bool:
    """Check if a tool is installed."""
    try:
        # Attempt to run the tool with --version flag
        subprocess.run(
            [tool_name, "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        # If the command succeeds, the tool is installed
        return True
    except FileNotFoundError:
        # If FileNotFoundError is raised, the tool is not installed
        return False


def _install_tool(tool_name: str, install_command: str) -> str:
    """Attempt to install a tool or provide manual installation instructions."""
    # First, check if the tool is already installed
    if _check_tool_installed(tool_name):
        return f"`{tool_name}` is already installed."
    try:
        # Attempt to install the tool using the provided install command
        return _run_shell_command(install_command)
    except Exception:
        # If installation fails, provide instructions for manual installation
        return (
            f"The tool `{tool_name}` could not be installed automatically. "
            f"Please install it manually using:\n\n{install_command}\n\n"
            f"After installation, verify it by running `{tool_name} --version`."
        )
