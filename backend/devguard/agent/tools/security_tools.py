from langchain_core.tools import tool

from agent.tools.utils import _install_tool, _run_shell_command



# Tool for scanning local file system with Trivy
@tool
def scan_trivy_file_system(target: str = ".") -> str:
    """Scan your local projects for Vulnerabilities, Misconfigurations, Secrets, and Licenses using Trivy."""
    # Run Trivy command to scan file system, ignoring unfixed issues and focusing on HIGH and CRITICAL severity
    return _run_shell_command(
        f"trivy fs {target} --ignore-unfixed --severity HIGH,CRITICAL"
    )


# Tool for scanning GitHub repository with Trivy
@tool
def scan_trivy_github_repo(repo_url: str) -> str:
    """Scan a GitHub repository for Vulnerabilities, Misconfigurations, Secrets, and Licenses using Trivy."""
    # Run Trivy command to scan GitHub repo, ignoring unfixed issues and focusing on HIGH and CRITICAL severity
    return _run_shell_command(
        f"trivy repo {repo_url} --ignore-unfixed --severity HIGH,CRITICAL"
    )


# Tool for scanning Git repository with TruffleHog
@tool
def scan_trufflehog() -> str:
    """Scan Git repository for secrets across all file types using trufflehog."""
    # Run TruffleHog command to scan for secrets, outputting in JSON format
    return _run_shell_command("trufflehog --json .")


# Tool for scanning files for sensitive data patterns
@tool
def scan_sensitive_data(filepath: str) -> str:
    """Scan any file for sensitive data patterns like API keys or credit card numbers."""
    # Define regex patterns for sensitive data
    patterns = [
        r"(?i)(api_key|secret_key|access_token|api_secret)[\s:=]+['\"][a-zA-Z0-9_\-]{16,}['\"]",
        r"\b(?:\d[ -]*?){13,16}\b",  # Credit card pattern
        r"\b\d{3}-\d{2}-\d{4}\b",  # SSN pattern
    ]
    # Create grep commands for each pattern
    commands = [f"grep -E '{pattern}' {filepath}" for pattern in patterns]
    # Execute grep commands and collect results
    results = [_run_shell_command(command) for command in commands]
    # Combine non-empty results
    matches = "\n".join(result for result in results if result)
    # Return matches or a message if no sensitive data found
    return matches if matches else "No sensitive data found."


# Tool for installing the 'safety' package
@tool
def install_safety() -> str:
    """Ensure that the 'safety' tool is installed."""
    # Use _install_tool utility to install 'safety' via pip
    return _install_tool("safety", "pip install safety")


# Tool for installing the 'trufflehog' package
@tool
def install_trufflehog() -> str:
    """Ensure that the 'trufflehog' tool is installed."""
    # Use _install_tool utility to install 'trufflehog' via pip
    return _install_tool("trufflehog", "pip install trufflehog")


# Tool for installing Trivy
@tool
def install_trivy() -> str:
    """Ensure that the 'trivy' tool is installed."""
    # Use _install_tool utility to install Trivy using its official installation script
    return _install_tool(
        "trivy",
        (
            "curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh "
            "| sh -s -- -b /usr/local/bin"
        ),
    )


# List of all security tools available for use
security_tools = [
    scan_trivy_file_system,
    scan_trivy_github_repo,
    scan_trufflehog,
    scan_sensitive_data,
    install_safety,
    install_trufflehog,
    install_trivy,
]
