import discord
from discord.ext import commands

from secret_data import DISCORD_BOT_API_KEY
from chatgpt_api import use_chatgpt
from text_function import separare_text


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents) 

@bot.command()
async def ask(ctx, *, question: str):
    chatgpt_reply = use_chatgpt(question)

    if len(chatgpt_reply) <= 2000:
        await ctx.reply(chatgpt_reply)

    else:
        for part in separare_text(chatgpt_reply):
            await ctx.reply(part)

bot.run(DISCORD_BOT_API_KEY)