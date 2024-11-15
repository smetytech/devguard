from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.tools import tool
from tools.utils import _run_shell_command

@tool
def web_search(query: str) -> str:
    """Use this to search on the web"""
    search = DuckDuckGoSearchResults(num_results=10)
    return search.invoke(query)


@tool
def execute_shell_command(commands: list[str]) -> str:
    """Execute a sequence of shell commands. Provide a list of commands to execute in order."""
    return _run_shell_command(" ".join(commands))


@tool
def execute_python_command(file_path: str) -> str:
    """Execute a python command. Provide a file_path to execute it with python ."""
    return _run_shell_command(f"python {file_path}")

@tool
def execute_pip_command(pkgs: list[str]) -> str:
    """Execute a sequence of pip commands. Provide a list of python packages to install in order."""
    return _run_shell_command(f"python -m pip install {' '.join(pkgs)}")

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