import discord
from discord.ext import commands
from discord import app_commands
import os
from flask import Flask
import threading

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} online!")
    try:
        await bot.tree.sync()
    except Exception as e:
        print(e)
    await bot.change_presence(activity=discord.Game(name="?hallo | /avatar"))

@bot.command()
async def hallo(ctx):
    await ctx.send(f"Hallo {ctx.author.mention}! Ich bin online ✅")

@bot.tree.command(name="avatar", description="Zeigt Avatar von User")
async def avatar_slash(interaction: discord.Interaction, user: discord.Member = None):
    await interaction.response.defer()
    user = user or interaction.user
    embed = discord.Embed(title=f"Avatar von {user.display_name}")
    embed.set_image(url=user.display_avatar.url)
    await interaction.followup.send(embed=embed)

@bot.tree.command(name="clear", description="Löscht Nachrichten 1-100")
async def clear_slash(interaction: discord.Interaction, anzahl: int = 5):
    if not interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message("Keine Rechte!", ephemeral=True)
        return
    await interaction.response.defer(ephemeral=True)
    deleted = await interaction.channel.purge(limit=anzahl)
    await interaction.followup.send(f"{len(deleted)} gelöscht!", ephemeral=True)

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is alive!"

def run_web():
    app.run(host='0.0.0.0', port=10000)

threading.Thread(target=run_web).start()

bot.run(TOKEN)
