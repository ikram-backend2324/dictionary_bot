"""
This is  echo bot.
It echoes any incoming text messages.
"""

import logging

from difflib import get_close_matches
from Load_Words import load_words
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5912123911:AAHGF7vR10pBcrwu1rI_ptPubcLOt8VzLgs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalawma aleykin Botimizga hush kelipsiz\n"
                        "Botti tekserip koriw ushin ingliz tilinde Soz kiritin...")



@dp.message_handler()
async def echo(message: types.Message):
    msg = message.text
    chat_id = message.chat.id
    english_words = load_words()
    if msg in english_words:
        await bot.send_message(chat_id, f"✅{msg}")
    else:
        res = (get_close_matches(msg, english_words, n=5))
        updated_res = "\n✅".join(res)
        await bot.send_message(chat_id, f"❌{msg}\n✅{updated_res}")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
