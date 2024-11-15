import os

from dotenv import load_dotenv
from github import Github
from langchain_core.tools import tool

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


github_client = Github(GITHUB_TOKEN)


@tool
def create_branch(repo_name: str, branch_name: str, base_branch: str = "main"):
    """
    Create a new branch in the specified repository.
    """
    try:
        repo = github_client.get_repo(repo_name)
        source = repo.get_branch(base_branch)
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
        repo = github_client.get_repo(repo_name)
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
        repo = github_client.get_repo(repo_name)
        contents = repo.get_contents(file_path, ref=branch)
        with open(file_path, "r") as file:
            new_content = file.read()
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
        repo = github_client.get_repo(repo_name)
        branches = repo.get_branches()
        return [branch.name for branch in branches]
    except Exception as e:
        return f"Failed to list branches: {str(e)}"


@tool
def delete_branch(repo_name: str, branch_name: str):
    """
    Delete a branch in the specified repository.
    """
    try:
        repo = github_client.get_repo(repo_name)
        ref = repo.get_git_ref(f"heads/{branch_name}")
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
        user = github_client.get_user()
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
        repo = github_client.get_repo(repo_name)
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


github_tools = [
    create_branch,
    create_pull_request,
    commit_and_push,
    list_branches,
    create_repository,
    get_repository_details,
]
