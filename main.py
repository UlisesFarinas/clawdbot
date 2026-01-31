import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")  # set this in Railway Variables

intents = discord.Intents.default()
intents.message_content = True  # you already toggled this in the Discord portal

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ONLINE as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("ONLINE")

if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("Missing DISCORD_TOKEN environment variable")
    bot.run(TOKEN)
