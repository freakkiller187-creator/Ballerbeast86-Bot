from flask import Flask
import threading
import discord
from discord.ext import commands
import os

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is alive!"

def run_web():
    app.run(host='0.0.0.0', port=10000)

threading.Thread(target=run_web).start()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} ist online!')

@bot.command()
async def Shisha(ctx):
    await ctx.send("💨 Shisha an, beruhig dich! Wer ist dabei? 😎")

@bot.command()
async def hallo(ctx):
    await ctx.send("Yo, was geht?")

bot.run(os.getenv("DISCORD_TOKEN"))
