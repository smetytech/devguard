# from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.tools import tool

from agent.tools.utils import _run_shell_command

# Web search functionality (currently commented out)
# @tool
# def web_search(query: str) -> str:
#     """Use this to search on the web for a specific user information."""
#     search = DuckDuckGoSearchResults(num_results=10)
#     return search.invoke(query)


@tool
def execute_shell_command(commands: list[str]) -> str:
    """Execute a sequence of shell commands. Provide a list of commands to execute in order."""
    # Join the commands with semicolons and execute them using _run_shell_command
    return _run_shell_command("; ".join(commands))


@tool
def execute_python_command(file_path: str) -> str:
    """Execute a python command. Provide a file_path to execute it with python ."""
    # Run the Python file using the python interpreter
    return _run_shell_command(f"python {file_path}")


@tool
def execute_pip_command(pkgs: list[str]) -> str:
    """Execute a sequence of pip commands. Provide a list of python packages to install in order."""
    # Use pip to install the specified packages
    return _run_shell_command(f"python -m pip install {' '.join(pkgs)}")


@tool
def read_file(filepath: str) -> str:
    """Read the contents of a file and return as a string."""
    try:
        # Open and read the file
        with open(filepath, "r") as file:
            return file.read()
    except FileNotFoundError:
        # Handle case where file is not found
        return "Error: File not found."
    except Exception as e:
        # Handle any other exceptions that may occur
        return f"An error occurred while reading the file: {str(e)}"


@tool
def write_file(filepath: str, content: str) -> str:
    """Write content to a file, overwriting existing content."""
    try:
        # Open the file in write mode and write the content
        with open(filepath, "w") as file:
            file.write(content)
        return f"File {filepath} has been overwritten successfully."
    except Exception as e:
        # Handle any exceptions that may occur during writing
        return f"An error occurred while writing to the file: {str(e)}"


@tool
def check_tool_is_installed(command: str) -> str:
    """Use this to see if a tool is installed."""
    # Run the command with --version flag to check if it's installed
    return _run_shell_command(f"{command} --version")


@tool
def generate_assessment_prompt(memory):
    """
    Concatenate all messages from memory and generate a prompt for OpenAI to assess the task and results.
    
    Args:
        memory: An object with a 'messages' property containing a list of ToolMessage, AiMessage, or HumanMessage.
        
    Returns:
        str: A prompt containing concatenated messages for OpenAI to assess.
    """
    try:
        if not hasattr(memory, 'messages') or not memory.messages:
            return "No memory messages available to create an assessment."

        all_messages = []
        for message in memory.messages:
            if hasattr(message, 'content'):
                all_messages.append(f"{message.__class__.__name__}: {message.content}")
            elif hasattr(message, 'tool_name'):
                all_messages.append(f"ToolMessage (Tool: {message.tool_name}): Result: {message.result or 'N/A'}, Error: {message.error or 'N/A'}")

        concatenated_messages = "\n".join(all_messages)
        
        prompt = f"""
You are a seasoned cybersecurity expert tasked with reviewing a historical interaction between a client (the user) and a cybersecurity agent. Your role is critical in delivering actionable insights.

Your objectives:
1. Understand the User's Request: Identify and clearly explain the userss original problem or goal.
2. Provide Detailed Answers: Break down the steps and methodologies used by the agent to address the userss request.
3. Identify the Problems Detected: Highlight any vulnerabilities, misconfigurations, or threats uncovered during the task.
4. Deliver a Comprehensive Assessment: Summarize the findings in a structured and detailed report. Include:
5. A clear explanation of the identified issues.
6. The impact of these issues on the clientss infrastructure.
7. Recommended actions or improvements.

Context:
The assessment you provide will be shared with the client to help them understand the security weaknesses in their infrastructure and implement effective solutions.

Interaction History:
{concatenated_messages}

Assessment:
        """
        
        return prompt.strip()

    except Exception as e:
        return f"An error occurred while generating the assessment prompt: {str(e)}"

utility_tools = [
    # web_search,
    execute_shell_command,
    read_file,
    write_file,
    check_tool_is_installed,
    execute_python_command,
    execute_pip_command,
    generate_assessment_prompt
]