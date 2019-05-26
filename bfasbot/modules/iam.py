from bfasbot import (LOAD, BOT, cmds, run_async)
from pyrogram import Filters, Message
from ..helpers import LastOnline, GetCommon
from pyrogram.api import functions
cmdf = ["whois","who", "me"]
import time, os, sys, logging
from ..helpers import DocMessage
from pyrogram.errors import PeerIdInvalid
from ..constants import WhoIs
from ..helpers import LastOnline, GetCommon, FullName, ReplyCheck, ProfilePicUpdate
from pyrogram.errors import (UserIsBlocked, FloodWait, FileIdInvalid, BadRequest, Flood, InternalServerError, SeeOther, Unauthorized, UnknownError, MessageNotModified, UsernameNotOccupied, MessageEmpty, UserAdminInvalid, ChatAdminRequired, PeerIdInvalid)
import bfasbot.duallog
import asyncio
logging.debug('Silently Initializing.')

@BOT.on_message(Filters.command(cmdf, cmds) & Filters.me)
async def vpro(bot: BOT, message: Message):
    cmd = " ".join(message.command[1:])
    get_user = ""
    forward_from = None
    if not message.reply_to_message:
        if len(cmd) > 1 and not cmd.isdigit():
          try:
            get_user = await bot.get_chat(cmd).id
          except Exception as e:
            logging.warning(e)
        elif cmd.isdigit():
          try:
            get_user = await BOT.get_chat(int(cmd)).id 
          except Exception as e:
            logging.warning(e)
        else:
          get_user = message.from_user.id
    elif message.reply_to_message:
      if message.reply_to_message.forward_from:
        get_user = message.reply_to_message.forward_from.id
        forward_from = message.reply_to_message.forward_from.id
      elif len(cmd) > 1 and not cmd.isdigit():
          try:
            get_user = await bot.get_chat(cmd).id
          except Exception as e:
            logging.warning(e)
      elif cmd.isdigit():
          try:
            get_user = await BOT.get_chat(int(cmd)).id 
          except Exception as e:
            logging.warning(e)
      else:
        get_user = message.reply_to_message.from_user.id
    user = await BOT.get_users(get_user if forward_from is not None else get_user)
    desc = await BOT.get_chat(get_user).description
    user_pic = await BOT.get_user_profile_photos(user.id)
    common = await GetCommon(user.id)

    if not user.photo:
        await message.edit(
            WhoIs.WHOIS.format(
                full_name = FullName(user),
                user_id = user.id,
                first_name = user.first_name if user.first_name else "",
                last_name = user.last_name if user.last_name else "",
                username = user.username if user.username else "",
                last_online = LastOnline(user),
                common_groups = len(common.chats),
                bio = desc if desc else "`No bio set up.`"),
            disable_web_page_preview = True)
    elif user.photo:
        await BOT.send_photo(
            message.chat.id,
            user_pic.photos[0].sizes[-1].file_id,
            WhoIs.WHOIS_PIC.format(
                full_name = FullName(user),
                user_id = user.id,
                first_name = user.first_name,
                last_name = user.last_name if user.last_name else "",
                username = user.username if user.username else "",
                last_online = LastOnline(user),
                profile_pics = "**Profile Picture**: "+ "`{}`".format(str(user_pic.total_count)),
                common_groups = "**Common Group:** " + "`{}`".format(str(len(common.chats))) if len(common.chats) <=1 else "**Common Groups:** "+ "`{}`".format(str(len(common.chats))),
              
                bio = desc if desc else "`No bio set up.`",
                profile_pic_update = await ProfilePicUpdate(user_pic)),
            reply_to_message_id = await ReplyCheck(message)
        )
        await message.delete()
    
          
  