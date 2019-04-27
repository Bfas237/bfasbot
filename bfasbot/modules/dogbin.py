
import requests

from pyrogram import Filters
from time import sleep, time
import pickle
from bfasbot import BOT, LOGS, cmds
BASE = "https://del.dog"
text = "do some other stuff, send some more requests while this one works"
from pprint import pprint
from requests_futures.sessions import FuturesSession
cmd = ["haste", "paste", "dogbin"]
def response_hook(resp, *args, **kwargs):
    # parse the json storing the result on the response object
    resp.data = resp.json()

@BOT.on_message(Filters.command(cmd, cmds) & Filters.me)
def haste(client, message):
    reply = message.reply_to_message
    if reply:
        text = reply.text
    else:
        text = " ".join(message.command[1:])

    if not text:
        return
    
    with FuturesSession() as session:
      session.hooks['response'] = response_hook
      future = session.post("{}/documents".format(BASE), data=text.encode("UTF-8"))
      response = future.result()  
      code = '{0}'.format(response.status_code)
      LINK = str(BASE) + "/" + code
      message.edit("{}/{}".format(BASE, response.data["key"]))
