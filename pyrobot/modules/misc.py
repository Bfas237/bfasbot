from datetime import datetime

from pyrogram import Filters, Message
from pyrobot import BOT, LOGS, START_TIME

from ..constants import MiscStrings

# Edit the sent message to display the current uptime.
@BOT.on_message(Filters.command(["up","uptime"], ".") & Filters.me)
def uptime(bot: BOT, message: Message):
    now = datetime.now()
    uptime = now - START_TIME
    message.edit(MiscStrings.UPTIME.format(str(uptime).split('.')[0]))
