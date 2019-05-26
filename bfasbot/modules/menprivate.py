from bfasbot import (LOAD, BOT, cmds, run_async)
from pyrogram import Filters, Message
from bfasbot.spamfilter import SpamFilter
from ..helpers import (bann,
    CheckAdmin, CheckReplyAdmin, LogMessage)
blocker = SpamFilter()
import asyncio
MEN_LOG = (
    "[{0.from_user.first_name}](tg://user?id="
    "{0.from_user.id}) Mentioned you in \"["
    "{0.chat.title}](t.me/c/{1}/{0.message_id})\".\n\n **Saying:** `{0.text}`")   
PV_LOG = (
    "[{0.from_user.first_name}](tg://user?id="
    "{0.from_user.id}) needs to chat with you in Private kindly check..`")  
    
@BOT.on_message(Filters.mentioned & ~Filters.bot)
async def mention(client, message):
    await LogMessage(MEN_LOG.format(
                message,
                str(message.chat.id).replace("-100", ""), message.text))
times = {}
    

@BOT.on_message(Filters.private & Filters.incoming & ~Filters.bot)
async def pv(client, message):
    if message.chat.type == "private":
      await LogMessage(PV_LOG.format(message))
      print("Message from: ", message.from_user.first_name) 
    