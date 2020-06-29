from discord.ext import commands
import os
import traceback
import requests
import json

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_message(message):
    # メッセージ送信者がbotは無視
    if message.author.bot:
        return
    # 「/vacushistory」は「」
    if message.content == '/vh':
        vacushistory = https://xchain.io/api/history/vacus
        await message.channel.request(vacushistory)


bot.run(token)
