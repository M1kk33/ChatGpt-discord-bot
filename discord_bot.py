import discord
import requests
from discord.ext import commands

from secret_data import DISCORD_BOT_API_KEY
from chatgpt_api import use_chatgpt
from text_function import separate_text


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents) 

url = 'https://discord.com/api/v10/applications/1297182107679985664/commands'

json = {
    'name': 'ask',
    'type': 1,
    "description": "Ask me a question and I'll answer",
}

headers = {
    'Authorization': f'Bot {DISCORD_BOT_API_KEY}'
}

r = requests.post(url, headers=headers, json=json)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'The bot {bot.user} is running and ready to work')


@bot.tree.command(name='ask', description='Ask a question')
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.defer()

    chatgpt_reply = use_chatgpt(question)

    if len(chatgpt_reply) <= 2000:
        await interaction.followup.send(chatgpt_reply)

    else:
        for part in separate_text(chatgpt_reply):
            await interaction.followup.send(part)

bot.run(DISCORD_BOT_API_KEY)