from threading import Thread

from pyrogram import Filters, Message
from bfasbot import (__pyrogram__, __author__, __version__, __python_version__, __source__, BOT, LOGS, START_TIME, cmds, timedate, MAINTENANCE, DOWN, UP)
from datetime import datetime
from ..constants import MiscStrings, First, rog
import os, subprocess, sys, time, glob, logging, asyncio
import bfasbot.duallog
     

now = datetime.now()
y = int(now.strftime("%Y"))
mm = int(now.strftime("%m")) 
d = int(now.strftime("%d"))
h = int(now.strftime("%H"))
m = int(now.strftime("%M"))
s = int(now.strftime("%S")) 
ds = datetime(y, mm, d, h, m, s )
from time import sleep, time 

  
@BOT.on_message(Filters.command(["up", "uptime", "alive"], ".") & Filters.me)
async def _alive(bot: BOT, message: Message):
    global MAINTENANCE
    global UP
    global DOWN
    now = datetime.now()
    uptime = now - START_TIME
    LOGS.info(uptime)
    now = datetime.now()
    uptime = now - START_TIME
    await message.edit(First.ALIVE.format(UP if MAINTENANCE == "off" else DOWN, __pyrogram__,__python_version__, MAINTENANCE, __version__, timedate(ds), str(uptime).split('.')[0], __author__, __source__),
                            disable_web_page_preview=True)
    LOGS.info(uptime)
    
HELP = ("Full list and Helpful docs.\n"
        "https://git.io/fjcGU")    
     
@BOT.on_message(Filters.command(["off"], ".") & Filters.me)
async def _dead(bot: BOT, message: Message):
    global MAINTENANCE
    global DOWN
    global UP
    now = datetime.now()
    uptime = now - START_TIME
    if MAINTENANCE == "off":
      MAINTENANCE = "on"
    elif MAINTENANCE == "on":
      MAINTENANCE = "off"
      
    await message.edit(First.SLEEP.format(DOWN if MAINTENANCE == "on" else UP, MAINTENANCE, timedate(ds), str(uptime).split('.')[0]),
                            disable_web_page_preview=True)
    MAINTENANCE = MAINTENANCE
    
 
    
@BOT.on_message(Filters.command("pyro", ".") & Filters.me)
async def _pyro(bot: BOT, message: Message):
    await message.edit(rog.PYRO,disable_web_page_preview=True)
