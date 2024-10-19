import discord
from discord.ext import commands

from secret_data import DISCORD_BOT_API_KEY
from chatgpt_api import use_chatgpt


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents) 

@bot.command()
async def ask(ctx, *, question: str):
    chatgpt_reply = use_chatgpt(question)
    await ctx.reply(chatgpt_reply)

bot.run(DISCORD_BOT_API_KEY)