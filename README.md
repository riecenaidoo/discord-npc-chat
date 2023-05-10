# README

This is an example of a Python script showing how you can use Discord Webhooks to create a tool that can echo messages from the user, received via the command line interface on their local machine, to a channel in a Discord server.

## Requirements

You'll need the following :

- `Pip` (*To install dependencies*)
- `Discord` Server (*To generate a webhook*)
- `Python` (*To run the script*)

## Setup

1. Install Dependencies:

    *It is recommended you setup a virtual environment to work in.*

    Install `discordwebhook` via pip package management tool.

        pip install discordwebhook

2. Create a Webhook to use with the script.

    *If you are not the server owner or admin, you may need additional permissions to follow the next steps.*

    Select a channel in the server you'd like the messages to appear in.

        Under Settings > Integrations > Webhooks > Create Webhook

    - Create a new Webhook.
    - Select the Webhook.
    - Copy the URL of this Webhook and save it in a text file, e.g. `web_hook_url.txt`, in the same directory as this script.

    ---  

    **Do not upload or share this text file.**

    *Anyone with access to the URL of your Webhook can send content through your Webhook, via that URL. So keep it safe and hidden.*

    ---

3. (Optional) Setup the script

    *If you saved the file in a different folder, or under a different file name, you'll need to edit the script and pass the path to the file into the function `get_webhook()` in the main script.*

4. Run the script

        python main.py

    - Type the messages you'd like to echo into the command line.
    - They will be sent via the Webhook and be displayed in the Discord Channel you've added the Webhook to.
    - Type `quit` to exit.

## Usage

To be used as a learning example, and a skeleton from which to build more complex tools.

*You can extend this example to send automated messages, or more meaningful data such as the output of a program you are running locally and have it echoed into a Discord channel.*

**For Example: [discord-ttrpg-dice-roller](https://github.com/riecenaidoo/discord-ttrpg-dice-roller)**

*A Dice rolling app for a Tabletop RPG with a GUI that lets a user click the dice they want to roll, and have the result of that roll be sent into a Discord channel for them to use in-game*

    Author: riecenaidoo
