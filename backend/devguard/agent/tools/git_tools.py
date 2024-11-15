import os

from dotenv import load_dotenv
from langchain_community.agent_toolkits.github.toolkit import GitHubToolkit
from langchain_community.utilities.github import GitHubAPIWrapper
from langchain_core.tools import tool

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

github = None


@tool
def initialize_github_repository(repo: str):
    """Initialize a GitHub repository."""
    global github
    github = GitHubAPIWrapper(
        github_repository=repo, github_app_private_key=GITHUB_TOKEN
    )
    return "GitHub repository initialized successfully."


def get_git_tools():
    if github is None:
        return []
    toolkit = GitHubToolkit.from_github_api_wrapper(github)
    return [tool for tool in toolkit.get_tools()]

github_tools = get_git_tools()
