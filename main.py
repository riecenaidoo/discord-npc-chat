import os

from dotenv import load_dotenv
from argparse import ArgumentParser
from discordwebhook import Discord


def get_input():
    """Get non-empty input from the Command Line."""

    user_input = input(" > ")
    while not user_input:
        user_input = input(" > ")
    return user_input


def get_npc():
    """Get the name of the NPC that is communicating via this Webhook
    from the command line argument -n/--npc"""

    parser = ArgumentParser()
    parser.add_argument("-n", "--npc",
                        dest="npc",
                        help="Specify the NPC that is communicating via this Webhook.",
                        required=True)
    return parser.parse_args().npc.upper()


if __name__ == "__main__":
    print("[INFO] Loading the NPCs.")
    load_dotenv()
    print("[INFO] Getting the selected NPC.")
    discord = Discord(url=os.environ[get_npc()])  # Create the Webhook
    print("[SUCCESS]!")

    custom_name = None
    receiving_input = True
    while receiving_input:
        message = get_input()

        if message.startswith("name="):
            custom_name = message.split("name=")[1]
            if len(custom_name) == 0:
                print("[INFO] Resetting name to default.")
                custom_name = None
            else:
                print("[INFO] Updated NPC's name.")
            continue

        if message == "quit":
            receiving_input = False
            print("[INFO] Quitting...")
            continue

        discord.post(username=custom_name, content=message)  # Send Message

    print("[END] Session Over!")
