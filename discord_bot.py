import discord
from discord.ext import commands

from secret_data import DISCORD_BOT_API_KEY


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents) 

@bot.command()
async def ask(ctx):
    await ctx.reply("I'm listening")

bot.run(DISCORD_BOT_API_KEY)