from flask import Flask
import threading
import discord
from discord.ext import commands
from discord import app_commands
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
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} ist online!")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} Slash-Befehle sync")
    except Exception as e:
        print(e)

# --- DEINE LINKS ---
@bot.command()
async def socials(ctx):
    embed = discord.Embed(title="Ballerbeast86 Links 🔥", color=0xff6000)
    embed.add_field(name="Website", value="[ballerbeast1986.beepworld.de](https://ballerbeast1986.beepworld.de)")
    embed.set_footer(text="Ballerbeast86")
    await ctx.send(embed=embed)

@bot.command()
async def hallo(ctx):
    await ctx.send(f"Yo {ctx.author.mention}, was geht? 😎")

# --- MODERATION ---
@bot.hybrid_command(name="avatar", description="Zeigt Avatar an")
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(member.display_avatar.url)

@bot.hybrid_command(name="say", description="Lässt den Bot was sagen")
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, text: str):
    await ctx.defer(ephemeral=True)
    await ctx.channel.send(text)
    await ctx.send("✅ Gesendet!", ephemeral=True)

@bot.hybrid_command(name="clear", description="Löscht Nachrichten")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: app_commands.Range[int, 1, 800] = 800):
    await ctx.defer(ephemeral=True)
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"✅ {amount} Nachrichten gelöscht!", ephemeral=True)

@bot.hybrid_command(name="kick", description="Kickt einen User")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason: str = "Kein Grund"):
    await member.kick(reason=reason)
    await ctx.send(f"👢 {member} wurde gekickt! Grund: {reason}")

@bot.hybrid_command(name="ban", description="Bannt einen User")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason: str = "Kein Grund"):
    await member.ban(reason=reason)
    await ctx.send(f"🔨 {member} wurde gebannt! Grund: {reason}")

@bot.hybrid_command(name="timeout", description="Gibt Timeout")
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member, minuten: int = 10):
    await member.timeout(discord.utils.utcnow() + discord.timedelta(minutes=minuten))
    await ctx.send(f"⏰ {member} hat {minuten} Min Timeout!")

bot.run(os.getenv("TOKEN"))
