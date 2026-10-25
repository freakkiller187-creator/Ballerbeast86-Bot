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
@bot.command()
async def socials(ctx):
    await ctx.send("🔗 Hier meine Links: TikTok: ... Instagram: ...")

@bot.command()
async def ip(ctx):
    await ctx.send("🎮 Server IP: 123.45.67.89")

@bot.command()
async def regeln(ctx):
    await ctx.send("📜 Regeln: 1. Kein Beef 2. Kein Spam 3. Viel Spaß!")

@bot.command()
async def hilfe(ctx):
    await ctx.send("**Befehle:**\n!hallo - Grüßt dich\n!socials - Meine Links\n!ip - Server IP\n!regeln - Regeln\n!Shisha - ...")

@bot.command()
async def ballern(ctx):
    await ctx.send("💥 BOOM! Ballerbeast86 ist am Start!")
