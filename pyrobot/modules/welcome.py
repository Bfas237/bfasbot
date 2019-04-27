from pyrogram import Filters, Message
sleeptime = 0
from pyrobot import (AFKREASON, COUNT_MSG, ISAFK, LOGGER, LOGGER_GROUP, USERS, HELPER)
from pyrogram.api import functions
import pickle, sqlite3
from pyrobot import BOT
from time import time, sleep
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
    cur.execute('''INSERT OR IGNORE INTO Users (Previous, ChatID) VALUES ( ?, ? )''', (users[0] if users is not None else "None", user))
    cur.execute('''UPDATE Users SET Previous = ? WHERE ChatID = ?''', (users[0] if users is not None else "None", user))
    
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
    
@BOT.on_message(Filters.me & Filters.command('set', cmds))
def setwelcome(client, message):
    if sleeptime < time():
        user = message.chat.id
        welcomes = " ".join(message.command[1:])
        print(welcomes)
        addtoDb(welcomes, user)
        message.edit('`Welcome Message succesfully set.`')
        sleep(3)
        welcomes = getuser(message.chat.id)
        message.edit("**Current welcome message for \"{}\"**\n\n✅ - {}".format(message.chat.title, welcomes))
        sleep(3)
        message.delete()

  
@BOT.on_message(Filters.new_chat_members | Filters.command('show', cmds))
def welcome(client, message):
    
    welcomes = getuser(message.chat.id)
    old = getusers(message.chat.id)
    
    if welcomes is not None: 
        if message.command:
            message.edit("**Welcome message for \"{}\"**\n\n✅ **Current**  - {}\n\n🗑 **Previous** - {}".format(message.chat.title, welcomes, old))
            sleep(5)
            message.delete()
            return
        new_members = ", ".join(
            ["[{}](tg://user?id={})".format(i.first_name, i.id) for i in message.new_chat_members])

        text = welcomes.replace('%name', new_members).replace('%title', "**"+message.chat.title+"**")

        # Send the welcome message
        wel = client.send_message(message.chat.id,
                            text,
                            reply_to_message_id=message.message_id,
                            disable_web_page_preview=True)
        sleep(120)
        wel.delete()
    else: 
        if message.command:
          message.reply("No welcome mesage has been set yet try setting one")