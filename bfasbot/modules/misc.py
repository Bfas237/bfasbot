from datetime import datetime
from pyrogram import Filters, Message
import logging
import logging.handlers
import time
from functools import partial
import asyncio
from pyrogram import Client, Filters
from pyrogram.errors.exceptions.flood_420 import FloodWait
from time import sleep
from bfasbot import (BOT, LOGS, START_TIME, cmds, LOAD)
from os.path import splitext
from pyrogram.errors import (UserIsBlocked, FloodWait, FileIdInvalid, BadRequest, Flood, InternalServerError, SeeOther, Unauthorized, UnknownError, MessageNotModified, UsernameNotOccupied, MessageEmpty, UserAdminInvalid, ChatAdminRequired, PeerIdInvalid)
from ..constants import MiscStrings, Comp
from ..helpers import (bann,
    CheckAdmin, CheckReplyAdmin, LogMessage)
import concurrent.futures
import logging
import time, os, sys
from os.path import dirname, basename, isfile
import glob, shutil
def exception_hook(exc_type, exc_value, exc_traceback):
    logging.error(
        "BFASBOT - Uncaught exception",
        exc_info=(exc_type, exc_value, exc_traceback)
    )  
 
sys.excepthook = exception_hook

def error_handler(bot, update, e):
        try:
            raise e
            LOGS.warning('Update "%s" caused error "%s"', update, e)
            
        except UnknownError:
            pass
        # remove update.message.chat_id from conversation list
        except BadRequest:
            pass
        # handle malformed requests - read more below!
        except Flood:
            pass
        
        except ChatAdminRequired:
          pass
          
        except FileIdInvalid:
            pass
          
        except UserIsBlocked:
            pass
          
        except UserAdminInvalid:
            pass
          
        except UserIsBlocked:
            pass
          
        except FloodWait:
            pass
        # handle slow connection problems
        except Unauthorized:
            pass
        # handle other connection problems
        except SeeOther:
            pass
        # the chat_id of a group has changed, use e.new_chat_id instead
        except InternalServerError:
            pass
          
        except PeerIdInvalid:
          pass
        # handle all other telegram related errors

def pdf():
  # Get a list of all the file paths that ends with .txt from in specified directory
  fileList = glob.glob('/app/*.pdf')
  for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath) 


"""fileList = glob.glob('/app/subbrute/*')
for filePath in fileList:
    try:
        shutil.rmtree(filePath) 
    except Exception as e:
        print("Error while deleting file : ", e, filePath) """
def jpg():
  # Get a list of all the file paths that ends with .txt from in specified directory
  fileList = glob.glob('/app/*.jpg')
  for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath) 
def png():
  # Get a list of all the file paths that ends with .txt from in specified directory
  fileList = glob.glob('/app/*.png')
  for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath) 



# Edit the sent message to display the current uptime.
@BOT.on_message(Filters.command(["learn","py"], ".") & Filters.me)
async def learn(bot: BOT, message: Message):
  
  
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
    logging.info(Comp.HELP.format(f1,f2, f3, f4,f5,f6,f7,f8,f9,f10,f11))
    await message.edit(Comp.HELP.format(f1,f2, f3, f4,f5,f6,f7,f8,f9,f10,f11))
    
    
@BOT.on_message(Filters.command("r", cmds) & Filters.me)
async def replace(client, message):
    text = " ".join(message.command[1:])
    fr, to = text.split('?')
    result = "**You mean:**\n{}".format(message.reply_to_message.text.replace(fr, to))
    await message.edit(result)
    
import threading

from functools import wraps
from math import factorial


DIC = {}

def limit(number):
    ''' This decorator limits the number of simultaneous Threads
    '''
    sem = threading.Semaphore(number)
    def wrapper(func):
        @wraps(func)
        def wrapped(*args):
            with sem:
                return func(*args)
        return wrapped
    return wrapper
  
def asyn(f):
    ''' This decorator executes a function in a Thread'''
    @wraps(f)
    def wrapper(*args, **kwargs):
        thr = threading.Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper

@limit(10)     # Always use @limit as the outter decorator
@asyn
def calcula_fatorial(number):
    DIC.update({number: factorial(number)})

@limit(10)
def main(lista):
    for elem in lista:
        calcula_fatorial(elem)

from threading import Thread
from queue import Queue


def threaded(fn):
  def wrap(queue, *args, **kwargs):
    queue.put(fn(*args, **kwargs))

  def call(*args, **kwargs):
    queue = Queue()
    job = Thread(target=wrap, args=(queue,) + args,
                 kwargs=kwargs)
    job.start()
    return queue

  return call
from time import sleep

@threaded
def f(x, y):
  #print('ran job #{}'.format(x))
  return 2 ** y

jobs = [job.get() for job in [f(i, i) for i in range(10)]]

#print(jobs)
@BOT.on_message(Filters.command("ask", cmds) & Filters.me)
async def ask(client, message):
    await message.reply(MiscStrings.ASK)
##

from pprint import pprint
@BOT.on_message(Filters.command("fo", cmds) & Filters.me)
async def _asfk(client, message):
    main(range(10))
    await message.reply(DIC)

 

@BOT.on_message(Filters.command("code", cmds) & Filters.me)
async def code(client, message):
    await message.reply(MiscStrings.PASTE)
import re

import os
from PIL import Image, ImageColor,ImageDraw, ImageFont

location = (100, 50)
text_color = (100, 100, 200)
@BOT.on_message(Filters.command("col", cmds) & Filters.me)
async def col(client, event):
    input_str = " ".join(event.command[1:])                 
    message_id = event.message_id
    if event.reply_to_message:
        message_id = event.reply_to_message.id
    if len(input_str) > 1:
        try:
            usercolor = ImageColor.getrgb(input_str)
        except Exception as e:
            await event.edit(str(e))
            return False
        else:
            im = Image.new(mode="RGB", size=(1280, 720), color=usercolor)
            d = ImageDraw.Draw(im)
            d.text(location, "Kite", fill=text_color)
            im.save("UniBorg.png", "PNG")
            input_str = input_str.replace(" ", "#COLOR_")
            BOT.send_photo(
                event.chat.id,
                "UniBorg.png",
                caption="#COLOR_"+input_str
            )
            os.remove("UniBorg.png")
            event.delete()
    else:
        event.edit("Syntax: `.color <color_code>`")

@BOT.on_message(Filters.regex(r'off.?topic', flags=re.IGNORECASE) & Filters.chat("Bfas237group"))
async def move(client, message):
      if message.reply_to_message:
        if message.media:
          await client.forward_messages(chat_id="bfas237off", from_chat_id=message.chat.id, message_ids=message.reply_to_message.message_id)
        else:
          await client.send_message("bfas237off", "[{0.from_user.reply_to_message.first_name}](tg://user?id={0.reply_to_message.from_user.id}) wrote:\n\n{0.text}".format(message))
      else:
         await client.send_message("bfas237off", "[{0.from_user.first_name}](tg://user?id={0.from_user.id}) wrote:\n\n{0.text}".format(message))
        
@BOT.on_message(Filters.command("i", cmds) & Filters.me)
async def replace(client, message):
    text = " ".join(message.command[1:])
    fr, to = text.split('.')
    result = "**I meant:**\n{}".format(message.reply_to_message.text.replace(fr, to))
    await message.edit(result)
 