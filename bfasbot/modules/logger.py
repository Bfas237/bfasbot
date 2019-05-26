from bfasbot import BOT, LOGS, ck, cmds
from datetime import datetime
import os, subprocess, sys, time, glob, logging
import bfasbot.duallog
from pyrogram import Filters, Message
from threading import Thread
fileList = glob.glob('bfasbot/logtest/*')
import bfasbot.duallog
import asyncio

logging.debug('Silently Initializing.')

async def stops():
        await BOT.restart()
      
        os.execl(sys.executable, sys.executable, *sys.argv)
        
        
newest_folder = max(fileList, key=os.path.getmtime)


@BOT.on_message(Filters.command("log", ".") & Filters.me)
async def _logs(bot: BOT, message: Message):
      try:
      
        latest_file = max(fileList, key=os.path.getctime)
        
        for fname in fileList:
          if fname != newest_folder:
            print('removing -> %s', fname)
            os.remove(fname)
          else:
            logging.warning("New logged File: "+newest_folder)
            await message.reply_document(newest_folder)
            await Thread(target=stops).start()
      except FileNotFoundError as e: 
        logging.debug(e)
        pass
        