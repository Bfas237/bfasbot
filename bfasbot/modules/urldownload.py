import cgi
import importlib
import os, asyncio
import tempfile
import shutil, logging
import sys
from bfasbot.helpers import LogMessage, ReplyCheck
logger = logging
import bfasbot.mods
from clint.textui import progress
try:
    from urllib.parse import quote_plus, urlparse, urljoin
    import urllib.request
    python3 = True
except ImportError:
    from urllib import quote_plus
    import urllib2 
    python3 = False
from itertools import islice
import requests, json
import asyncio
from bfasbot.mods import *
import aiohttp
from pyrogram import Filters
from time import sleep, time
import pickle, os, traceback

from pyrogram.errors import (UserIsBlocked, FloodWait, FileIdInvalid, BadRequest, Flood, InternalServerError, SeeOther, Unauthorized, UnknownError, MessageNotModified, UsernameNotOccupied, MessageEmpty, UserAdminInvalid, ChatAdminRequired, PeerIdInvalid)
from bfasbot import BOT, LOGS, cmds, run_async
download_path = "{}/.data/".format(os.getcwd())
if not os.path.isdir(download_path):
  os.makedirs(download_path)
options={}
base_headers = {
        'User-Agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
headers = dict(base_headers, **options)
def files(fn):
  from os.path import dirname, basename, isfile
  import glob
  # Get a list of all the file paths that ends with .txt from in specified directory
  fileList = glob.glob('/app/.data/*'+fn)
  for filePath in fileList:
    try:
        all_mod = [basename(filePath).split(".")[0] for filePath in fileList if isfile(filePath)] 
        for rem in all_mod:
          os.remove(basename(isfile(filePath)).split("/")[:-1])
    except:
        print("Error while deleting file : ", filePath) 
  
@BOT.on_message(Filters.command("get", cmds) & Filters.me)
async def dl(client, message, **current):
    try:
      url = " ".join(message.command[1:])
      logging.info(message.from_user)
      required_file_name = ""
      media = ""
      file_name = ""
      file_size = ""
      extension = ""
      fnames = ""
      download_path = "{}/.data".format(os.getcwd())
      m = message
      if not "http" in message.text:
        sent = await message.edit("That is not a valid link. Use /help for more info")
        sleep(3)
        await sent.delete()
      else: 
        ctype = get_filename(url)
        if ctype:
            if ctype[0] is None:
              err = "`The link you submitted is invalid.`\n\ Kindly check your link and try again for  I am in no mood to tell you the exact reason 😒"
              await message.edit(str(err), quote=True)
              logger.warning(str(err))
              return
            sent = await message.edit("downloading")
            required_file_name = ctype[0]
            fnames = ctype[1]
            downl = await DownLoadFile(url, required_file_name, fnames, client, sent, message.chat.id)
            sleep(3)

            if downl:
                if (downl[0] != 0):
                  start = time()
                  await sent.edit("Done ✅.. Now uploading..")
                  sleep(3)
                  chat_id = message.from_user.id
                  required_file_name = download_path+"/"+required_file_name
                  logger.warning('"%s" Just downloaded:  "%s"', message.from_user.id, required_file_name)
                  mediaq = check_media(required_file_name)
                  fn = basename(required_file_name).split(".")[0]
                  file = ""
                  if mediaq == 'Pictures':
                    file = await client.send_photo(message.chat.id, required_file_name, progress = DFromUToTelegramProgress, progress_args = (sent, message.chat.id, start, "**📤 Uploading:**"), caption=downl[1] if downl[1] else "❤️ @Bfas237blog")
                  elif mediaq == 'Video':
                    file = await client.send_video(message.chat.id, required_file_name, progress = DFromUToTelegramProgress, progress_args = (sent, message.chat.id, start, "**📤 Uploading:**"), caption=downl[1] if downl[1] else "❤️ @Bfas237blog")
                  elif mediaq == 'Music':
                    file = await client.send_audio(message.chat.id, required_file_name, progress = DFromUToTelegramProgress, progress_args = (sent, message.chat.id, start, "**📤 Uploading:**"), caption=downl[1] if downl[1] else "❤️ @Bfas237blog")
                  else:
                    file = await client.send_document(message.chat.id, required_file_name, progress = DFromUToTelegramProgress, progress_args = (sent, message.chat.id, start, "**📤 Uploading:**"), caption=downl[1] if downl[1] else "❤️ @Bfas237blog")
                  logs = -1001249303594
                  await sent.delete()
                  #client.send_message(chat_id="bfaslogs", text="**Download Logs**\n\n{}".format(log), disable_web_page_preview=True)
                  
                  files(fn)
            else:
                try:
                  files(basename(download_path+"/"+required_file_name).split(".")[0])
                except Exception:
                  pass
                er = "An error occured while downloading...."
                sent.edit(er)
                logger.info(er)

        else:
          err = "`Your link doesn't look like a downloadable link...... Kindly try again`"
          message.edit(str(err), quote=True)
          logger.debug(str(err))

    except:
      traceback.print_exc()
