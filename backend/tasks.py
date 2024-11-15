import subprocess

def run_trivy_scan(target: str) -> str:
    try:
        result = subprocess.run(["trivy", "image", target], capture_output=True, text=True, check=True)
        return result.stdout or "No vulnerabilities found."
    except subprocess.CalledProcessError as e:
        return f"Error while scanning: {e}"

def run_trufflehog_scan(repo: str) -> str:
    try:
        result = subprocess.run(["trufflehog", "filesystem", repo], capture_output=True, text=True, check=True)
        return result.stdout or "No sensitive data found."
    except subprocess.CalledProcessError as e:
        return f"Error while scanning repository: {e}"
