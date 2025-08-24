# Question Bot

A Discord bot that generates random fun questions with the `/generate` command.

## Setup Instructions

1. First, install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Create a new Discord application and bot:

   - Go to the [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application" and give it a name
   - Go to the "Bot" section and click "Add Bot"
   - Copy the bot token

3. Replace `YOUR_BOT_TOKEN` in `bot.py` with your actual bot token

4. Invite the bot to your server:

   - Go to the "OAuth2" section in your Discord application
   - In "Scopes", select "bot" and "applications.commands"
   - Copy the generated URL and open it in your browser to invite the bot

5. Run the bot:

```bash
python bot.py
```

## Usage

Once the bot is running, you can use the following command in your Discord server:

- `/generate` - Generates a random fun question

## Features

- Generates random fun questions from a curated list
- Uses Discord's slash commands for easy interaction
- Easy to add new questions by updating the `questions.py` file
