from discordwebhook import Discord


def get_input():
    """Get non-empty input from the Command Line."""
    
    user_input = input(" > ")
    while (not user_input):
        user_input = input(" > ")
    return user_input


def get_webhook(web_hook_file):
    """Open the file containing the webhook and read the url,
    which should be on a single line."""
    
    try:
        with open(web_hook_file) as f:
            return f.read()
    except(FileNotFoundError):
        print(f"WARNING: '{web_hook_file}' file was not found.")


if __name__ == "__main__":
        
    web_hook_url = get_webhook("web_hook_url.txt" )
    if not web_hook_url:
        print("""
            A web hook url is needed to start this program.
            See README.md
            """
            )
        exit()

    print("Starting Session.")
    discord = Discord(url=web_hook_url) # Create the Webhook

    receiving_input = True
    while receiving_input:
        message = get_input()
        
        if (message == "quit"):
            receiving_input = False
            continue

        discord.post(content=message)   # Send Message
        
    print("Session Over.")    