from datetime import datetime

from pyrogram import Filters, Message
from bfasbot import BOT, LOGS, START_TIME, cmds

from ..constants import MiscStrings, Comp

# Edit the sent message to display the current uptime.
@BOT.on_message(Filters.command(["up","uptime"], ".") & Filters.me)
def uptime(bot: BOT, message: Message):
    now = datetime.now()
    uptime = now - START_TIME
    message.edit(MiscStrings.UPTIME.format(str(uptime).split('.')[0]))
    
    
# Edit the sent message to display the current uptime.
@BOT.on_message(Filters.command(["learn","py"], ".") & Filters.me)
def learn(bot: BOT, message: Message):
  
  
    f1 = "(https://wiki.python.org/moin/BeginnersGuide/NonProgrammers)"
    f2 = "(https://wiki.python.org/moin/BeginnersGuide/Programmers)"
    f3 = "(https://docs.python.org/3/tutorial/)"
    f4 = "(http://www.diveintopython3.net/)"
    f5 = "(https://www.learnpython.org/)"
    f6 = "(https://cscircles.cemc.uwaterloo.ca/)"
    f7 = "(https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)"
    f8 = "(https://docs.python-guide.org/)"

    f9 = "(https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7)"
    f10 = "(https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)"
    f11 = "(http://projectpython.net/chapter00/)"
    message.edit(Comp.HELP.format(f1,f2, f3, f4,f5,f6,f7,f8,f9,f10,f11))
    
    
@BOT.on_message(Filters.command("r", cmds))
def replace(client, message):
    text = " ".join(message.command[1:])
    fr, to = text.split('.')
    result = "**You mean:**\n{}".format(message.reply_to_message.text.replace(fr, to))
    message.edit(result)
