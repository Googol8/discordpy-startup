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
    # 「/vh」で「vacusのhistory」
    if message.content == '/vh':
        vacushistory = 	https://xchain.io/api/market/vacus/history
            result = request.get(vacushistory)
            
bot.run(token)
