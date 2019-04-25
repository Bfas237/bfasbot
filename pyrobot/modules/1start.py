from pyrobot import BOT
from pyrogram import Filters, Message

from ..constants import First

@BOT.on_message(Filters.command("alive", ".") & Filters.me)
def _alive(bot: BOT, message: Message):
    message.edit(First.ALIVE)

@BOT.on_message(Filters.command("help", ".") & Filters.me)
def _help(bot: BOT, message: Message):
    message.edit(First.HELP_TEXT)
