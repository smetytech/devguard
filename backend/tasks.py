import subprocess

def run_trivy_scan(target: str) -> str:
    result = subprocess.run(["trivy", "image", target], capture_output=True, text=True)
    return result.stdout or "No vulnerabilities found."

def run_trufflehog_scan(repo: str) -> str:
    result = subprocess.run(["trufflehog", "filesystem", repo], capture_output=True, text=True)
    return result.stdout or "No sensitive data found."
