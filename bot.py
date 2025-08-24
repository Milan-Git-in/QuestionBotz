import discord
from discord import app_commands
import random
from questions import questions
import os
from dotenv import load_dotenv
import asyncio
import aiohttp
from aiohttp import web
import os
from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# Start the web server on another thread
threading.Thread(target=run).start()

# Load environment variables
load_dotenv()

class QuestionBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)
        self.health_app = web.Application()
        self.health_app.router.add_get('/health', self.health_check)
        self.health_server = None

    async def setup_hook(self):
        await self.tree.sync()
        # Start health check server
        runner = web.AppRunner(self.health_app)
        await runner.setup()
        self.health_server = web.TCPSite(runner, 'localhost', 8080)
        await self.health_server.start()
        print("Health check endpoint is running on http://localhost:8080/health")

    async def health_check(self, request):
        return web.Response(text="Bot is running!", status=200)

client = QuestionBot()

@client.tree.command(name="generate", description="Generate a random fun question!")
async def generate(interaction: discord.Interaction):
    question = random.choice(questions)
    await interaction.response.send_message(question)

# Get token from environment variable
TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN:
    raise ValueError("No token found. Make sure DISCORD_TOKEN is set in your .env file.")

client.run(TOKEN)
