from bfasbot import (LOGS, LOAD, BOT, cmds, __source__, __author__, response_hook, run_async, BASE)
from pyrogram import Filters, Message
from ..constants import rog
from requests_futures.sessions import FuturesSession
import re, logging
from time import sleep
BASEs = "https://hastebin.com"
from os.path import dirname, basename, isfile
import glob
import bfasbot.duallog
repw = ["repo","file", "m"]

def read_file(fn, o):
    from os.path import dirname, basename, isfile
    import glob
    mod_ = glob.glob(dirname(__file__) + "/*.py")
    all_mod = []
    fileList = glob.glob('bfasbot/*')
    if o == "r":
      all_mod = [basename(filePath).split(".")[0] for filePath in fileList if isfile(filePath) and filePath.endswith(".py")]
    elif o == "m":
      all_mod = [
        basename(f)[:-3]
        for f in mod_
        if isfile(f) and f.endswith(".py")
    ]
    ALL_MODULE = sorted(all_mod)
    print(ALL_MODULE)
    r = re.compile(".*{}".format(fn))
    match = list(filter(r.match, ALL_MODULE))
    if match:
      for fd in match:
        mod = glob.glob(dirname(__file__) + "/{}.py".format(fd)) if o == "m" else glob.glob("bfasbot/{}.py".format(fd))
        with open(mod[0]) as f:
          return[f.read(), fd]
    else:
      return None
    
    
import bfasbot.duallog
 
@BOT.on_message(Filters.command(repw, cmds))
async def _files(bot: BOT, message: Message):
    if len(message.command) > 1:
        if message.command[1] == "init":
          text = await read_file("__init__", message.command[2])
        elif message.command[1] == "main":
          text = await read_file("__main__", message.command[2])
        elif message.command[2] is None:
            await  message.reply("invalid args:")
            return
        text = await read_file(message.command[1], message.command[2])
        if text is not None:
          async with ClientSession() as session:
            async with session.post('{}/documents'.format(BASE), data=content.encode('utf-8')) as response:
              code = '{0}'.format(response.status)
              print(code)
              if int(code) <= 300:
                LINK = str(BASE) + "/" + code
                await message.edit('Take a look at the source code of `{}` [HERE]({}'
                     '/{})'.format(text[1] if text != "__init__" else "`__init__`", BASE, response.data["key"]))
                return
              else:
                await message.edit('OPPS!!! `{}` appears to be down'.format(BASE))
                sleep(5)
                await message.edit('Pasting to `{}` in progress'.format(BASEs))
                sleep(5)
                async with ClientSession() as session:
                    async with session.post('{}/documents'.format(BASE), data=content.encode('utf-8')) as response:
                        code = '{0}'.format(response.status)
                        print(code)
                        if int(code) <= 300:
                          LINK = str(BASEs) + "/" + code
                          await message.edit('Take a look at the source code of `{}` [HERE]({}'
                     '/{})'.format(text[1] if text != "__init__" else "`__init__`", BASEs, response.data["key"]))
                          return
            
                        
                        else:
              
                          message.edit('Sorry but `{}` and `{}` appears to be down'.format(BASE, BASEs))
                          return
        
        else:
          message.edit('Sorry but `{}` was not found in my directory'.format(message.command[1]))
          return

    message.edit('**Github Repo:**   [{}]({})'.format(__author__,__source__))
    
    
