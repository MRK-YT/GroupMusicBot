import requests
from pyrogram import Client as Bot

from VCsMusicBot.config import API_HASH
from VCsMusicBot.config import API_ID
from VCsMusicBot.config import BG_IMAGE
from VCsMusicBot.config import BOT_TOKEN
from VCsMusicBot.services.callsmusic import run

response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)
bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="VCsMusicBot.modules"),
)

bot.start()
run()
