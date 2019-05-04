
from pyrogram import Filters, Message
from bfasbot import (__pyrogram__, __author__, __version__, __python_version__, __source__, BOT, LOGS, START_TIME, cmds, timedate, MAINTENANCE, DOWN, UP, run_async)
from datetime import datetime
from ..constants import MiscStrings, First, rog
import os, subprocess, sys
now = datetime.now()
y = int(now.strftime("%Y"))
mm = int(now.strftime("%m")) 
d = int(now.strftime("%d"))
h = int(now.strftime("%H"))
m = int(now.strftime("%M"))
s = int(now.strftime("%S")) 
ds = datetime(y, mm, d, h, m, s )
@BOT.on_message(Filters.command(["up", "uptime", "alive"], ".") & Filters.me)
@run_async
def _alive(bot: BOT, message: Message):
    global MAINTENANCE
    global UP
    now = datetime.now()
    uptime = now - START_TIME
    MAINTENANCE = "Off" 
    now = datetime.now()
    uptime = now - START_TIME
    message.edit(First.ALIVE.format(UP, __pyrogram__,__python_version__, MAINTENANCE, __version__, timedate(ds), str(uptime).split('.')[0], __author__, __source__),
                            disable_web_page_preview=True)
    
    
    
@BOT.on_message(Filters.command(["off"], ".") & Filters.me)
def _alive(bot: BOT, message: Message):
    global MAINTENANCE
    global DOWN
    now = datetime.now()
    uptime = now - START_TIME
    MAINTENANCE = "On" 
    message.edit(First.SLEEP.format(DOWN, MAINTENANCE, timedate(ds), str(uptime).split('.')[0]),
                            disable_web_page_preview=True)

@BOT.on_message(Filters.command("help", ".") & Filters.me)
def _help(bot: BOT, message: Message):
    message.edit(rog.PYRO,disable_web_page_preview=True)

"""@BOT.on_message(Filters.command("poll", ".") & Filters.me)
def make_poll(bot, message):
  poll = message.text[6:].split('\n')
  bot.send_poll(
    message.chat.id,
    poll[0],
    poll[1:]
  )"""
