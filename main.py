import sys
import discord
import os
from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

@bot.slash_command(name="restart", description="Restartet den Main bot")
@commands.is_owner()
async def restart(ctx):
    await ctx.respond("Bot wird neu gestartet.", ephemeral=True)
    os.execv(sys.executable, ['python'] + sys.argv)

@bot.event
async def on_ready():
    print(f'Eingeloggt als {bot.user} (ID: {bot.user.id})')

    activity = discord.Game(name="Internet Treffpunkt <3", type=1)

    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")
    print(f"version: {discord.__version__}")



@bot.event 
async def on_apllication_command(ctx, error):
    await ctx.respond(
        embed = discord.Embed(
            title = "Error",
            description = f"Folgender Fehler ist aufgetreten: ```{error}```",
            color = discord.Color.red()
        ),
        ephemeral = True
    )
    raise error




@bot.event
async def on_member_remove(member):
    em = discord.Embed(
        title = "Member Verlassen",
        description=f"{member.name} hat den Server verlassen",
        color = discord.Color.red(),
        timestamp = datetime.utcnow()
    )
    await bot.get_channel(1036820950580219917).send(embed=em)


@bot.event
async def on_member_join(member):
    em = discord.Embed(
        title = "Member Beigetreten",
        description=f"{member.name} ist dem Server beigetreten",
        color = discord.Color.green(),
        timestamp = datetime.utcnow()
    )
    await bot.get_channel(1036820950580219917).send(embed=em)
############################################################################################################
@bot.event
async def on_guild_delete(channel):
    em = discord.Embed(
        title="Channel gelöscht",
        description=f"Der Channel {channel.name} wurde gelöscht",
        color = discord.Color.red(),
        timestamp = datetime.utcnow()
    )
    await bot.get_channel(1036820950580219919).send(embed=em)


@bot.event
async def on_guild_create(channel):
    em = discord.Embed(
        title="Channel erstellt",
        description=f"Der Channel {channel.name} wurde erstellt",
        color = discord.Color.green(),
        timestamp = datetime.utcnow()
    )
    await bot.get_channel(1036820950580219919).send(embed=em)
############################################################################################################
#@bot.event
#async def on_member_update(before, after):
    #if len(before.roles) > len(after.roles):
        #em = discord.Embed(
            #title="Rolle entfernt",
           #description=f"Die Rolle von {before.name} haben sich geändert ```{before.roles[1]}``` wurde entfernt",
            #color = discord.Color.red(),
            #timestamp = datetime.utcnow()
        #)
       # em = discord.Embed(
            #title="Rolle hinzugefügt",
            #description=f"Die Rolle von {before.name} haben sich geändert ``{after.roles[1]}`` wurde hinzugefügt",
            #color = discord.Color.green(),
            #timestamp=datetime.utcnow()
        #)
    #elif before.nick != after.nick:
        #em = discord.Embed(
            #title="Nickname geändert",
            #description=f"Der Nickname von **{before.name}** wurde von ```{before.nick}``` zu ```{after.nick}``` geändert",
            #color=discord.Color.blue(),
            #timestamp=datetime.utcnow()
        #)
    #else:
        #return
    #await bot.get_channel(1036820950580219917).send(embed=em)
############################################################################################################
@bot.event
async def on_message_edit(before, after):
    if before.content != after.content:
        em = discord.Embed(
            title="Nachricht bearbeitet",
            description=f"Die Nachricht von {before.author.name} wurde bearbeitet"
                        f"Davor:```{before.content}```"
                        f"Danach:```{after.content}```"
                        f"Nachrichten ID: {before.id}"
                        f"Nachrichten Channel: {before. channel.mention}",
            color = discord.Color.blue(),
            timestamp = datetime.utcnow()
        )
        await bot.get_channel(1036820950580219918).send(embed=em)


@bot.event
async def on_message_delete(message):
    em = discord.Embed(
        title="Nachricht gelöscht",
        description=f"Die Nachricht von **{message.author.name}** wurde gelöscht"
                    f"Nachricht inhalt: ```{message.content}```"
                    f"Nachricht ID: ```{message.id}```"
                    f"Nachricht gesendet am: ```{message.created_at}```"
                    f"Nachricht gelöscht in: {message.channel.mention}",
        color = discord.Color.red(),
        timestamp = datetime.utcnow()
    )
    em.add_field(name="Nachricht", value=message.content, inline=False)
    await bot.get_channel(1036820950580219918).send(embed=em)
############################################################################################################



for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

load_dotenv()
bot.run(os.getenv("TOKEN"))