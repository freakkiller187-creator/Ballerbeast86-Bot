import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} ist online!')

@bot.command()
async def Shisha(ctx):
    await ctx.send("🫖 Shisha an, beruhig dich! Wer ist dabei? 🔥")

bot.run(os.getenv("DISCORD_TOKEN"))
