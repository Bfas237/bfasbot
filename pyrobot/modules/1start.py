
from pyrogram import Filters, Message
from pyrobot import (__pyrogram__, __author__, __version__, __python_version__, __source__, BOT, LOGS, START_TIME, cmds)
from datetime import datetime
from ..constants import MiscStrings, First

 

@BOT.on_message(Filters.command(["up", "uptime", "alive"], ".") & Filters.me)
def _alive(bot: BOT, message: Message):
    now = datetime.now()
    uptime = now - START_TIME
    message.edit(First.ALIVE.format(__pyrogram__,__python_version__, __version__, str(uptime).split('.')[0], __author__, __source__),
                            disable_web_page_preview=True)

@BOT.on_message(Filters.command("help", ".") & Filters.me)
def _help(bot: BOT, message: Message):
    message.edit(First.HELP_TEXT)

"""@BOT.on_message(Filters.command("poll", ".") & Filters.me)
def make_poll(bot, message):
  poll = message.text[6:].split('\n')
  bot.send_poll(
    message.chat.id,
    poll[0],
    poll[1:]
  )"""