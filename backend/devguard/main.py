import argparse
import uuid
from colorama import Fore, Style, init

from agent.setup import graph
from agent.utils import print_stream

# Initialize colorama for colored terminal output
init(autoreset=True)

def main():
    # Set up argument parser for command line arguments
    parser = argparse.ArgumentParser(description="Chat with the AI agent.")
    parser.add_argument(
        "--message", "-m", type=str, help="Initial message to send to the agent."
    )
    args = parser.parse_args()

    # Welcome message
    print(f"{Fore.CYAN}{Style.BRIGHT}Welcome to the AI Chat Agent!{Style.RESET_ALL}")
    print(
        f"{Fore.YELLOW}Type your message below or enter 'exit' to end the chat.{Style.RESET_ALL}\n"
    )

    # Configuration for the agent
    config = {"configurable": {"thread_id": uuid.uuid4().hex}, "recursion_limit": 100}

    # If an initial message is provided via command line argument
    if args.message:
        inputs = {"messages": [("user", args.message)]}
        print(f"{Fore.BLUE}>> {Fore.RESET}{args.message}")
        print(f"{Fore.GREEN}agent-dev:", end=" ")
        print_stream(graph.stream(inputs, config, stream_mode="values"))
    else:
        # Prompt user for input if no initial message is provided
        user_input = input(f"{Fore.BLUE}{Style.BRIGHT}>>{Style.RESET_ALL} ")
        inputs = {"messages": [("user", user_input)]}
        print(f"{Fore.BLUE}>> {Fore.RESET}{user_input}")
        print(f"{Fore.GREEN}agent-dev:", end=" ")
        print_stream(graph.stream(inputs, config, stream_mode="values"))

    # Main chat loop
    while True:
        user_input = input(f"{Fore.BLUE}{Style.BRIGHT}>>{Style.RESET_ALL} ")

        # Exit the chat if user types 'exit' or 'quit'
        if user_input.lower() in ["exit", "quit"]:
            print(f"{Fore.CYAN}Ending chat. Goodbye!{Style.RESET_ALL}")
            break

        # Process user input and get response from the agent
        inputs = {"messages": [("user", user_input)]}
        print(f"{Fore.GREEN}{Style.BRIGHT}agent-dev:{Style.RESET_ALL} ", end="")
        print_stream(graph.stream(inputs, config, stream_mode="values"))
        print(f"{Fore.YELLOW}{'-'*40}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
