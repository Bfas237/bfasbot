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
def getuser(owner):
    conn = sqlite3.connect('userbot.db', check_same_thread=False)
    c = conn.cursor() 
    c.execute('''SELECT Welcome FROM Users WHERE ChatID = ?''', (owner,))
    user = c.fetchone()
    if user is not None: 
      return user[0]
    else:
      return None
def getusers(owner):
    conn = sqlite3.connect('userbot.db', check_same_thread=False)
    c = conn.cursor() 
    c.execute('''SELECT Previous FROM Users WHERE ChatID = ?''', (owner,))
    user = c.fetchone()
    if user is not None: 
      return user[0]
    else:
      return None
    
def addtoDb(wel, user):
  with sqlite3.connect('userbot.db', check_same_thread=False) as conn:
    cur = conn.cursor()
    cur = conn.execute('''SELECT Welcome, ChatID FROM Users WHERE ChatID = ?''', (user,))  
    users = cur.fetchone()
    count = 0 
    cur.execute('''INSERT OR IGNORE INTO Users (Previous, ChatID) VALUES ( ?, ? )''', (users[0], user))
    cur.execute('''UPDATE Users SET Previous = ? WHERE ChatID = ?''', (users[0], user))
    
    cur.execute('''INSERT OR IGNORE INTO Users (Welcome, ChatID) VALUES ( ?, ? )''', (wel, user))
    cur.execute('''UPDATE Users SET Welcome = ? WHERE ChatID = ?''', (wel, user))
    count += 1 
      
    conn.commit() 

    print ("Total news written to database : ", count, users) 
    
    
def goafk(user, wel):
  with sqlite3.connect('userbot.db', check_same_thread=False) as conn:
    cur = conn.cursor()
    cur = conn.execute('''SELECT ISAFK, AFKREASON FROM Users''')  
    users = cur.fetchone()
    count = 0 
    cur.execute('''INSERT OR IGNORE INTO Users (ISAFK, AFKREASON) VALUES ( ?, ? )''', (user, wel))
    cur.execute('''UPDATE Users SET ISAFK=(?), AFKREASON=(?)''', (wel, user))
    
    count += 1 
      
    conn.commit()  

    print ("Total news written to database : ", count, users)     
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
                    


    
@BOT.on_message(Filters.me & Filters.command('set', cmds))
def setwelcome(client, message):
    if sleeptime < time():
        user = message.chat.id
        welcomes = message.text.replace(message.command, '')
        print(welcomes)
        addtoDb(welcomes, user)
        message.edit('`Welcome Message succesfully set.`')
        sleep(3)
        welcomes = getuser(message.chat.id)
        message.edit("**Current welcome message for \"{}\"**\n\n✅ - {}".format(message.chat.title, welcomes))
        sleep(3)
        message.delete()


@BOT.on_message(Filters.chat(["bfas237off", "bfas237group", "PyrogramLounge"]) & Filters.new_chat_members | Filters.command('show', cmds))
def welcome(client, message):
    
    welcomes = getuser(message.chat.id)
    old = getusers(message.chat.id)
    
    if welcomes is not None: 
        if message.command:
            message.edit("**Welcome message for \"{}\"**\n\n✅ **Current**  - {}\n\n🗑 **Previous** - {}".format(message.chat.title, welcomes, old))
            return
        new_members = ", ".join(
            ["[{}](tg://user?id={})".format(i.first_name, i.id) for i in message.new_chat_members])

        text = welcomes.replace('%name', new_members).replace('%title', message.chat.title)

        # Send the welcome message
        client.send_message(message.chat.id,
                            text,
                            reply_to_message_id=message.message_id,
                            disable_web_page_preview=True)
        
    else:
      message.reply("No welcome mesage has been set yet try setting one")