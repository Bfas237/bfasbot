import sys, pickle, subprocess
import importlib
import time, datetime, os, re, sys, sqlite3, json, io 
from bfasbot import __copystring__, __version__, __python_version__
from bfasbot import BOT, LOGS
from bfasbot.modules import ALL_MODULES
import sqlite3 as lite
import glob, asyncio
from pyrogram import Filters, Client
from datetime import date, datetime
for module_name in ALL_MODULES:
    imported_module = importlib.import_module("bfasbot.modules." + module_name)


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

def rem(file):
  # Get a list of all the file paths that ends with .txt from in specified directory
  fileList = glob.glob('/app/*'+file)
  for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath) 
  

import pickle
with open('trigger', 'wb') as f:
    pickle.dump({}, f)
with open('correction', 'wb') as f:
    pickle.dump({}, f)
with open('welcome', 'wb') as f:
   pickle.dump({}, f)
with open('warn', 'wb') as f:
    pickle.dump({}, f)
    
    
async def main():
        await BOT.start()
        print(__copystring__)
        LOGS.info(f"Test it by typing .up in any chat.")
        LOGS.info(f"Your bot is Version {__version__}\n")
        await BOT.idle()
        print("\nUserbot Stopped\n")
        await BOT.stop()






if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
