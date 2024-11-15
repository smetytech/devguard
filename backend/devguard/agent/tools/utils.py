import subprocess

from langchain_community.tools import ShellTool


def _run_shell_command(command: str) -> str:
    """Run a shell command and return the result."""
    shell_tool = ShellTool()
    try:
        return shell_tool.run({"commands": [command]})
    except Exception as e:
        return f"An error occurred while running the command: {str(e)}"


def _check_tool_installed(tool_name: str) -> bool:
    """Check if a tool is installed."""
    try:
        subprocess.run(
            [tool_name, "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return True
    except FileNotFoundError:
        return False

def _install_tool(tool_name: str, install_command: str) -> str:
    """Attempt to install a tool or provide manual installation instructions."""
    if _check_tool_installed(tool_name):
        return f"`{tool_name}` is already installed."
    try:
        return _run_shell_command(install_command)
    except Exception:
        return (
            f"The tool `{tool_name}` could not be installed automatically. "
            f"Please install it manually using:\n\n{install_command}\n\n"
            f"After installation, verify it by running `{tool_name} --version`."
        )