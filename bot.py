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

@bot.command()
async def socials(ctx):
    embed = discord.Embed(title="Ballerbeast86 Links 🔥", color=0xFF0000)
    embed.add_field(name="🌐 Website", value="[ballerbeast1986.beepworld.de](https://ballerbeast1986.beepworld.de/index.htm)", inline=False)
    embed.set_footer(text="Ballerbeast86 - Klick drauf!")
    await ctx.send(embed=embed)

@bot.command()
async def ip(ctx):
    await ctx.send("🎮 Server IP: 123.45.67.89")

@bot.command()
async def regeln(ctx):
    await ctx.send("📜 Regeln: 1. Kein Beef 2. Kein Spam 3. Viel Spaß!")

@bot.command()
async def hilfe(ctx):
    await ctx.send("**Befehle:**\n!hallo\n!socials - Meine Website\n!ip\n!regeln\n!ballern")

@bot.command()
async def ballern(ctx):
    await ctx.send("💥 BOOM! Ballerbeast86 ist am Start!")

bot.run(os.getenv("DISCORD_TOKEN"))
# --- NEU DAZU ---
@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f"{guild.name} Info", color=0x0000FF)
    embed.add_field(name="Owner", value=f"{guild.owner}", inline=True)
    embed.add_field(name="Member", value=f"{guild.member_count}", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"User Info - {member.name}", color=0xFFFF00)
    embed.add_field(name="Beigetreten am", value=f"{member.joined_at.strftime('%d.%m.%Y')}", inline=False)
    embed.set_thumbnail(url=member.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"Avatar von {member.name}", color=0x00FF00)
    embed.set_image(url=member.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(text)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 500):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"✅ {amount} Nachrichten gelöscht!", delete_after=3)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="Kein Grund"):
    await member.kick(reason=reason)
    await ctx.send(f"👢 {member.name} wurde gekickt!")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Kein Grund"):
    await member.ban(reason=reason)
    await ctx.send(f"🔨 {member.name} wurde gebannt!")

@bot.command()
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member, minuten: int = 10):
    await member.timeout(discord.utils.utcnow() + discord.timedelta(minutes=minuten))
    await ctx.send(f"⏰ {member.name} für {minuten} Minuten getimeoutet!")

# --- ENDE NEU ---
