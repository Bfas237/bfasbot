
import requests, json
import asyncio
from bfasbot.mods import *
import aiohttp
from pyrogram import Filters
from time import sleep, time
import pickle, os, traceback
logger = logging
from bfasbot import BOT, LOGS, cmds, run_async
BASE = "https://del.dog"
from pprint import pprint
from requests_futures.sessions import FuturesSession
cmd = ["haste", "bin", "dog"]
from aiohttp import ClientSession



def response_hook(resp, *args, **kwargs):
    # parse the json storing the result on the response object
    resp.data = resp.json()


@BOT.on_message(Filters.command(cmd, cmds) & Filters.me)
async def haste(client, message):
    reply = message.reply_to_message
    if reply:
        text = reply.text
    else:
        text = " ".join(message.command[1:])

    if not text:
        return
    
    async with ClientSession() as session:
      async with session.post('{}/documents'.format(BASE), data=text.encode('utf-8')) as post:
        LINK = BASE + '/' + (await post.json())['key']
        await message.reply("{}".format(LINK))
      #await message.edit("{}/{}".format(BASE, response.data["key"]))
