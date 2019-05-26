from threading import Thread
from ..helpers import LogMessage

from pyrogram import Filters, Message
from bfasbot import (__pyrogram__, __author__, __version__, __python_version__, __source__, BOT, LOGS, START_TIME, cmds, timedate, MAINTENANCE, DOWN, UP, run_async)
from datetime import datetime
from ..constants import MiscStrings, First, rog
import os, subprocess, sys, time, logging
now = datetime.now()
y = int(now.strftime("%Y"))
mm = int(now.strftime("%m")) 
d = int(now.strftime("%d"))
h = int(now.strftime("%H"))
m = int(now.strftime("%M"))
s = int(now.strftime("%S")) 
ds = datetime(y, mm, d, h, m, s )
import bfasbot.duallog




async def restarts():
  
        await BOT.restart()
        os.execl(sys.executable, sys.executable, *sys.argv)


@BOT.on_message(Filters.command("rb", ".") & Filters.me)
async def _reboot(bot: BOT, message: Message):
    global MAINTENANCE
    global DOWN
    global UP
    now = datetime.now()
    uptime = now - START_TIME
    
    LOGS.info("Your bot is restarting......")
    
    MAINTENANCE = "on"
    Thread(target=restarts).start()
    
    MAINTENANCE = "off"

    LOGS.info("Your bot is Running again whooooooo!......")

    time.sleep(5)
    await message.edit(First.ALIVE.format(UP if MAINTENANCE == "off" else DOWN, __pyrogram__,__python_version__, MAINTENANCE, __version__, timedate(ds), str(uptime).split('.')[0], __author__, __source__),
                            disable_web_page_preview=True)
    await LogMessage("**Bot was rebooted:** "+timedate(ds))