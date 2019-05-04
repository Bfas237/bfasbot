
import requests

from pyrogram import Filters
from time import sleep, time
import pickle
from bfasbot import BOT, LOGS, cmds
BASE = "https://del.dog"
text = "do some other stuff, send some more requests while this one works"
from pprint import pprint
from bfasbot import html2text
from requests_futures.sessions import FuturesSession
cmd = ["mark"]
def response_hook(resp, *args, **kwargs):
    # parse the json storing the result on the response object
    resp.data = resp.json()

@BOT.on_message(Filters.command(cmd, cmds) & Filters.me)
def markdown(client, message):
    reply = message.reply_to_message
    if reply:
        text = reply.text
    else:
        text = " ".join(message.command[1:])

    if not text:
        return
    err = "Pyro gram error -ç-"
    response = html2text.Tomd(text).markdown
    message.edit(response if response else err)
