import os

from dotenv import load_dotenv
from github import Github
from langchain_core.tools import tool

# Load environment variables from .env file
load_dotenv()
# Get GitHub token from environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Initialize GitHub client with the token
github_client = Github(GITHUB_TOKEN)


@tool
def create_branch(repo_name: str, branch_name: str, base_branch: str = "main"):
    """
    Create a new branch in the specified repository.
    """
    try:
        # Get the repository object
        repo = github_client.get_repo(repo_name)
        # Get the source branch
        source = repo.get_branch(base_branch)
        # Create a new branch referencing the source branch's latest commit
        repo.create_git_ref(f"refs/heads/{branch_name}", source.commit.sha)
        return f"Branch '{branch_name}' created in {repo_name} from {base_branch}."
    except Exception as e:
        return f"Failed to create branch: {str(e)}"


@tool
def create_pull_request(
    repo_name: str, title: str, body: str, head: str, base: str = "main"
):
    """
    Create a pull request in the specified repository.
    """
    try:
        # Get the repository object
        repo = github_client.get_repo(repo_name)
        # Create a new pull request
        pr = repo.create_pull(title=title, body=body, head=head, base=base)
        return f"Pull request created: {pr.html_url}"
    except Exception as e:
        return f"Failed to create pull request: {str(e)}"


@tool
def commit_and_push(
    repo_name: str, file_path: str, commit_message: str, branch: str = "main"
):
    """
    Commit changes to a file and push to the specified branch.
    """
    try:
        # Get the repository object
        repo = github_client.get_repo(repo_name)
        # Get the contents of the file
        contents = repo.get_contents(file_path, ref=branch)
        # Read the new content from the local file
        with open(file_path, "r") as file:
            new_content = file.read()
        # Update the file in the repository
        repo.update_file(
            contents.path, commit_message, new_content, contents.sha, branch=branch
        )
        return f"Changes committed and pushed to {repo_name}/{branch}."
    except Exception as e:
        return f"Failed to commit and push changes: {str(e)}"


@tool
def list_branches(repo_name: str):
    """
    List all branches in the specified repository.
    """
    try:
        # Get the repository object
        repo = github_client.get_repo(repo_name)
        # Get all branches
        branches = repo.get_branches()
        # Return a list of branch names
        return [branch.name for branch in branches]
    except Exception as e:
        return f"Failed to list branches: {str(e)}"


@tool
def delete_branch(repo_name: str, branch_name: str):
    """
    Delete a branch in the specified repository.
    """
    try:
        # Get the repository object
        repo = github_client.get_repo(repo_name)
        # Get the reference to the branch
        ref = repo.get_git_ref(f"heads/{branch_name}")
        # Delete the branch
        ref.delete()
        return f"Branch '{branch_name}' deleted in {repo_name}."
    except Exception as e:
        return f"Failed to delete branch: {str(e)}"


@tool
def create_repository(repo_name: str, description: str = "", private: bool = True):
    """
    Create a new repository.
    """
    try:
        # Get the authenticated user
        user = github_client.get_user()
        # Create a new repository
        repo = user.create_repo(
            name=repo_name, description=description, private=private
        )
        return f"Repository '{repo_name}' created: {repo.html_url}"
    except Exception as e:
        return f"Failed to create repository: {str(e)}"


@tool
def get_repository_details(repo_name: str):
    """
    Get details of a repository.
    """
    try:
        # Get the repository object
        repo = github_client.get_repo(repo_name)
        # Return a dictionary with repository details
        return {
            "name": repo.name,
            "description": repo.description,
            "private": repo.private,
            "owner": repo.owner.login,
            "url": repo.html_url,
            "created_at": repo.created_at.isoformat(),
            "updated_at": repo.updated_at.isoformat(),
        }
    except Exception as e:
        return f"Failed to get repository details: {str(e)}"


# List of all GitHub-related tools
github_tools = [
    create_branch,
    create_pull_request,
    commit_and_push,
    list_branches,
    create_repository,
    get_repository_details,
]
