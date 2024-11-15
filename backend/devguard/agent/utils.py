def print_stream(stream):
    """Prints a stream of messages in a human-readable format."""
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()