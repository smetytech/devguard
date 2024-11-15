from langchain_core.tools import tool

from agent.tools.utils import _install_tool, _run_shell_command


@tool
def scan_trivy_file_system(target: str = ".") -> str:
    """Scan your local projects for Vulnerabilities, Misconfigurations, Secrets, and Licenses using Trivy."""
    return _run_shell_command(
        f"trivy fs {target} --ignore-unfixed --severity HIGH,CRITICAL"
    )

@tool
def scan_trivy_github_repo(repo_url: str) -> str:
    """Scan a GitHub repository for Vulnerabilities, Misconfigurations, Secrets, and Licenses using Trivy."""
    return _run_shell_command(
        f"trivy repo {repo_url} --ignore-unfixed --severity HIGH,CRITICAL"
    )


@tool
def scan_trufflehog() -> str:
    """Scan Git repository for secrets across all file types using trufflehog."""
    return _run_shell_command("trufflehog --json .")


@tool
def scan_sensitive_data(filepath: str) -> str:
    """Scan any file for sensitive data patterns like API keys or credit card numbers."""
    patterns = [
        r"(?i)(api_key|secret_key|access_token|api_secret)[\s:=]+['\"][a-zA-Z0-9_\-]{16,}['\"]",
        r"\b(?:\d[ -]*?){13,16}\b",  # Credit card
        r"\b\d{3}-\d{2}-\d{4}\b",  # SSN
    ]
    commands = [f"grep -E '{pattern}' {filepath}" for pattern in patterns]
    results = [_run_shell_command(command) for command in commands]
    matches = "\n".join(result for result in results if result)
    return matches if matches else "No sensitive data found."


@tool
def install_safety() -> str:
    """Ensure that the 'safety' tool is installed."""
    return _install_tool("safety", "pip install safety")


@tool
def install_trufflehog() -> str:
    """Ensure that the 'trufflehog' tool is installed."""
    return _install_tool("trufflehog", "pip install trufflehog")


@tool
def install_trivy() -> str:
    """Ensure that the 'trivy' tool is installed."""
    return _install_tool(
        "trivy",
        (
            "curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh "
            "| sh -s -- -b /usr/local/bin"
        ),
    )


security_tools = [
    scan_trivy_file_system,
    scan_trivy_github_repo,
    scan_trufflehog,
    scan_sensitive_data,
    install_safety,
    install_trufflehog,
    install_trivy,
]
