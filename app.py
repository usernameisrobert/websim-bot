import discord
import os
from discord import app_commands
from flask import Flask
from threading import Thread

# --- Web Server Section ---
app = Flask('')

@app.route('/')
def home():
    return "great! the bot should now be usable."

def run():
    # Render assigns a PORT via environment variables, default to 8080 or 10000 if missing
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
# --------------------------

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

# Start the web server first
keep_alive()

# Run the bot
if token:
    client.run(token)
else:
    print("Error: BOT_TOKEN environment variable not found.")
