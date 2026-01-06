import discord
import os  # Import the OS library to read environment variables
from discord import app_commands

class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        await self.tree.sync()
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('Slash commands have been synced!')

client = MyBot()

@client.tree.command(name="gemini", description="Check status for Gemini")
async def gemini(interaction: discord.Interaction):
    await interaction.response.send_message("coming soon...")

@client.tree.command(name="sora2", description="Check status for Sora2")
async def sora2(interaction: discord.Interaction):
    await interaction.response.send_message("coming soon...")

# Retrieve the token from the environment variable
token = os.getenv("BOT_TOKEN")

# Simple check to ensure the token exists before running
if token:
    client.run(token)
else:
    print("Error: BOT_TOKEN environment variable not found.")
