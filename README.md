# README

This is a Python script that uses Discord Webhooks to create a tool that can echo messages from the user, 
received via the command line interface on their local machine, to a channel in a Discord server.

I use it to 'speak' as different NPCs in the Discord during TTRPG sessions.

## Setup

### Create a Webhook to use with the script.

*If you are not the server owner or admin, you may need additional permissions to follow the next steps.*

Select a channel in the server you'd like the messages to appear in.

    Under Settings > Integrations > Webhooks > Create Webhook

- Create a new Webhook.
- Select the Webhook.
- Copy the URL of this Webhook and save it in a `.env` file under, e.g. `MY_NPC=`.
  - You can add multiple Webhooks under different keys.

---  

**Do not upload or share this text file.**

*Anyone with access to the URL of your Webhook can send content through your Webhook, via that URL. So keep it safe and hidden.*

---

## Usage

### Run the Script

*If you have GNU Make, Python3 and Pip package manager installed:*
      
    make run NPC=my_npc

or, after installing the dependencies in `requirements.txt`

    python3 main NPC=my_npc

### Use the Script

- Type the messages you'd like to echo into the command line.
    - They will be sent via the Webhook and be displayed in the Discord Channel you've added the Webhook to.
- Type `quit` to exit.
- Type `name=` followed by the nickname you want the Webhook's messages to display from.
  - Type `name=` by itself to set it to the default Webhook name.
