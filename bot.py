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
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} ist online!')
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} Slash-Befehle sync")
    except Exception as e:
        print(e)

# --- DEINE LINKS ---
@bot.command()
async def socials(ctx):
    embed = discord.Embed(title="Ballerbeast86 Links 🔥", color=0xFF0000)
    embed.add_field(name="🌐 Website", value="[ballerbeast1986.beepworld.de](https://ballerbeast1986.beepworld.de/index.htm)", inline=False)
    embed.set_footer(text="Ballerbeast86")
    await ctx.send(embed=embed)

@bot.command()
async def hallo(ctx):
    await ctx.send(f"Yo {ctx.author.mention}, was geht? 😎")

@bot.command()
async def ballern(ctx):
    await ctx.send("💥 BOOM! Ballerbeast86 ist am Start! 💨")

@bot.command()
async def Shisha(ctx):
    await ctx.send("💨 Shisha an, beruhig dich! Wer ist dabei?")

@bot.command()
async def regeln(ctx):
    embed = discord.Embed(title="📜 Server Regeln", color=0xFF0000)
    embed.add_field(name="Regeln", value="1. Kein Beef / Beleidigung\n2. Kein Spam / Werbung\n3. Respektvoll sein\n4. Viel Spaß haben!", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def ip(ctx):
    await ctx.send("🎮 **Server IP:** Kommt bald!")

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
async def hilfe(ctx):
    embed = discord.Embed(title="🤖 Ballerbeast86 Bot Hilfe", color=0xFF0000)
    embed.add_field(name="🌐 Website", value="[ballerbeast1986.beepworld.de](https://ballerbeast1986.beepworld.de/index.htm)", inline=False)
    await ctx.send(embed=embed)

# --- NEU UND GEFIXT - GEHT ALS ! UND / ---
@bot.hybrid_command(name="avatar", description="Zeigt Avatar an")
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"Avatar von {member.name}", color=0x00FF00)
    embed.set_image(url=member.display_avatar.url)
    await ctx.send(embed=embed)

@bot.hybrid_command(name="say", description="Bot sagt was")
async def say(ctx, *, text: str):
    await ctx.send(text)

@bot.hybrid_command(name="clear", description="Löscht Nachrichten")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 700):
    await ctx.defer(ephemeral=True)
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"✅ {amount} Nachrichten gelöscht!", ephemeral=True)

@bot.hybrid_command(name="kick", description="Kickt User")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason: str = "Kein Grund"):
    await member.kick(reason=reason)
    await ctx.send(f"👢 {member.name} wurde gekickt!")

@bot.hybrid_command(name="ban", description="Bannt User")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason: str = "Kein Grund"):
    await member.ban(reason=reason)
    await ctx.send(f"🔨 {member.name} wurde gebannt!")

@bot.hybrid_command(name="timeout", description="Timeout für User")
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member, minuten: int = 10):
    await member.timeout(discord.utils.utcnow() + discord.timedelta(minutes=minuten))
    await ctx.send(f"⏰ {member.name} für {minuten} Minuten getimeoutet!")

bot.run(os.getenv("DISCORD_TOKEN"))
