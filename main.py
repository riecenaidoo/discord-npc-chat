import os

from dotenv import load_dotenv
from discordwebhook import Discord


def get_input():
    """Get non-empty input from the Command Line."""

    user_input = input(" > ")
    while not user_input:
        user_input = input(" > ")
    return user_input


if __name__ == "__main__":

    print("Starting Session.")
    load_dotenv()
    discord = Discord(url=os.environ["DISCORD_WEBHOOK_URL"])  # Create the Webhook

    custom_name = None
    receiving_input = True
    while receiving_input:
        message = get_input()

        if message.startswith("name="):
            custom_name = message.split("name=")[1]
            if len(custom_name) == 0 and custom_name.isalnum():
                custom_name = None
            continue

        if message == "quit":
            receiving_input = False
            continue

        discord.post(username=custom_name, content=message)  # Send Message

    print("Session Over.")
