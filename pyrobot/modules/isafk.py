from datetime import datetime

from pyrogram import Filters, Message
sleeptime = 0
from pyrobot import (AFKREASON, COUNT_MSG, ISAFK, LOGGER, LOGGER_GROUP, USERS, HELPER)
from pyrogram.api import functions
import pickle, sqlite3
from pyrobot import BOT
from time import time, sleep
from ..helpers import SpeedConvert, LogMessage
from pyrobot import cmds
@BOT.on_message(Filters.mentioned & ~Filters.reply)
def isafk_group(bot: BOT, message: Message):
    """ This function takes care of notifying the people who mention you that you are AFK."""
    global COUNT_MSG
    global USERS
    global ISAFK
    with open('isafk', 'wb') as f:
      afk = pickle.load(f)
    if ISAFK:
            if message.from_user.id not in afk:
                message.reply(
                    "Sorry! My boss is AFK due to `{}`."
                    "\nWould ping him to look into the message soon 😉.".format(AFKREASON)
                )
                
                
                COUNT_MSG = COUNT_MSG + 1
                afk[message.chat.id] = afk[message.from_user.id] + 0
                with open('isafk', 'wb') as f:
                  pickle.dump(afk, f)

            elif message.from_user.id not in afk:
                if afk[message.from_user.id] % 5 == 0:
                    message.reply(
                        "Sorry! But my boss is still not here."
                        "\nTry to ping him a little later. I am sorry 😖."
                        "\nHe told me he was busy with `{}`.".format(AFKREASON)
                    )
                    afk[message.from_user.id] = afk[message.from_user.id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                    with open('isafk', 'wb') as f:
                      pickle.dump(afk, f)
                else:
                    afk[message.from_user.id] = afk[message.from_user.id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                    with open('isafk', 'wb') as f:
                      pickle.dump(afk, f)
                    
                    
@BOT.on_message(Filters.private & ~Filters.bot & ~Filters.via_bot)
def afk_on_pm(bot: BOT, message: Message):
    """ Function which informs people that you are AFK in PM """
    global ISAFK
    global USERS
    global COUNT_MSG
    with open('welcome', 'rb') as f:
        afk = pickle.load(f)
        print(afk)
    if ISAFK:
            if message.from_user.id not in afk:
                message.reply(
                    "Sorry! My boss is AFK due to `{}`."
                    "\nWould ping him to look into the message soon 😉.".format(AFKREASON)
                )
                
                COUNT_MSG = COUNT_MSG + 1
                afk[message.from_user.id] = afk[message.from_user.id] + COUNT_MSG
                with open('welcome', 'wb') as f:
                  pickle.dump(USERS, f)
 
            elif message.from_user.id in afk:
                if afk[message.from_user.id] % 5 == 0:
                    message.reply(
                        "Sorry! But my boss is still not here."
                        "\nTry to ping him a little later. I am sorry 😖."
                        "\nHe told me he was busy with `{}`.".format(AFKREASON)
                    )
                    afk[message.from_user.id] = afk[message.from_user.id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                    with open('welcome', 'wb') as f:
                      pickle.dump(afk, f)
                else:
                    afk[message.from_user.id] = afk[message.from_user.id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                    with open('welcome', 'wb') as f:
                      pickle.dump(afk, f)
                    
    
@BOT.on_message(Filters.me & Filters.command('afk', cmds))
def set_afk(client, message):
    global ISAFK
    global AFKREASON
    if sleeptime < time():
        user = message.from_user.id
        welcomes = message.text.replace(str(message.command), '')
        goafk(1, welcomes)
        message.edit('`You went afk.`')
        sleep(3)
        message.delete()
                    

