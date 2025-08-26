import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()  # загружаем .env

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} подключен и готов к работе!")

bot.run(TOKEN)
