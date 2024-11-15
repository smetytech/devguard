from langchain_community.tools import DuckDuckGoSearchResults, ShellTool
from langchain_core.tools import tool


@tool
def web_search(query: str) -> str:
    """Use this to search on the web"""
    search = DuckDuckGoSearchResults(num_results=10)
    return search.invoke(query)


@tool
def execute_shell_command(commands: list[str]) -> str:
    """Execute a sequence of shell commands. Provide a list of commands to execute in order."""
    shell_tool = ShellTool()
    try:
        result = shell_tool.run({"commands": commands})
        return result
    except Exception as e:
        return f"An exception occurred: {str(e)}"


@tool
def execute_python_command(file_path: str) -> str:
    """Execute a python command. Provide a file_path to execute it with python ."""
    shell_tool = ShellTool()
    try:
        result = shell_tool.run({"commands": f"python {file_path}"})
        return result
    except Exception as e:
        return f"An exception occurred: {str(e)}"


@tool
def execute_pip_command(pkgs: list[str]) -> str:
    """Execute a sequence of pip commands. Provide a list of python packages to install in order."""
    shell_tool = ShellTool()
    try:
        result = shell_tool.run({"commands": [f"python -m pip install {pkg}" for pkg in pkgs]})
        return result
    except Exception as e:
        return f"An exception occurred: {str(e)}"

@tool
def read_file(filepath: str) -> str:
    """Read the contents of a file and return as a string."""
    try:
        with open(filepath, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred while reading the file: {str(e)}"


@tool
def write_file(filepath: str, content: str) -> str:
    """Write content to a file, overwriting existing content."""
    try:
        with open(filepath, "w") as file:
            file.write(content)
        return f"File {filepath} has been overwritten successfully."
    except Exception as e:
        return f"An error occurred while writing to the file: {str(e)}"

@tool
def check_tool_is_installed(command: str) -> str:
    """Use this to see if a tool is installed
    Args:
        command: Command to test if a tool is installed, usually it has a flag -v or --version
    """
    shell_tool = ShellTool()
    return shell_tool.run({"commands": [command]})
    
tools = [
    web_search,
    execute_shell_command,
    read_file,
    write_file,
    check_tool_is_installed,
    execute_pip_command,
    execute_python_command
]
