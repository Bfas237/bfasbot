import sqlite3
from time import sleep
from html import escape, unescape

from pyrogram import Filters, Message
from bfasbot import BOT, LOGS, cmds, run_async, PYRO_DB, LOGGER_GROUP

from ..helpers import LogMessage, bann
olds = bann.splitlines( )
test = "this is a btc test and i have it for sale so wuna pv or inbox"
a = olds
b = test
matches=[]
for item_a in a:
    for item_b in b:
        if item_b.lower() in item_a.lower() and item_b.lower() not in matches:
            matches.append(item_a.lower())
#print(matches)

@BOT.on_message(Filters.command("allb", cmds) & Filters.me)
def all_welcome(bot: BOT, message: Message):
    res = " ".join(message.command[1:])
    if not res:
        welcome = res.split( )
        welcome_messages = "**All Blacklisted Words:**\n"
        welcome_messages += "\n {}\n".format(unescape(bann))
        BOT.send_message(message.chat.id, welcome_messages, disable_web_page_preview=True)
        message.edit("Welcome messages sent in Saved Messages.")
        sleep(2)
        message.delete()
    else:
        message.edit("__There is no welcome message for this chat.__")
        sleep(3)
        message.delete()
