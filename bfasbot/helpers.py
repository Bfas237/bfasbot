from time import sleep, strftime, time
from datetime import datetime
import requests
import os
import time, os, asyncio, aiofiles
from pyrogram import Message, User
from pyrogram.api import functions

from bfasbot import BOT, LOGGER, LOGGER_GROUP, ACCGEN_API, timedate

from .interval import IntervalHelper

async def CheckAdmin(message: Message):
    """Check if we are admin."""

    admin = 'administrator'
    creator = 'creator'
    ranks = [admin, creator]

    SELF = await BOT.get_chat_member(
        chat_id = message.chat.id,
        user_id = message.from_user.id)

    if SELF.status not in ranks:
        await message.edit("__I'm not Admin!__")
        sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin:
            return True
        elif SELF.permissions.can_restrict_members:
            return True
        else:
            await message.edit("__No Permissions to restrict Members__")
            sleep(2)
            await message.delete()

async def CheckReplyAdmin(message: Message):
    """Check if the message is a reply to another user."""
    if not message.reply_to_message:
        await message.edit("`?{}` needs to be a reply".format(message.command[0]))
        sleep(2)
        message.delete()
    elif message.reply_to_message.from_user.is_self:
        await message.edit("I can't {} myself.".format(message.command[0]))
        sleep(2)
        await message.delete()
    else:
        return True

def Timer(message: Message): 
    import time
    if len(message.command) > 1:
        secs = IntervalHelper(message.command[1])
        return int(str(time.time()).split(".")[0] + str(secs.to_secs()[0]))
    else:
        return 0
def TimerString(message: Message):
    secs = IntervalHelper(message.command[1])
    return "{} {}".format(secs.to_secs()[1], secs.to_secs()[2])

async def RestrictFailed(message: Message):
    await message.edit("I can't {} this user.".format(message.command[0]))
    sleep(2)
    await message.delete()


async def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id

async def LogMessage(logmsg):
    if LOGGER:
        await BOT.send_message(
            chat_id = LOGGER_GROUP,
            text = logmsg
        )

async def DocMessage(logmsg):
    if LOGGER:
        await BOT.send_document(
            chat_id = LOGGER_GROUP,
            document = logmsg
        )

def LastOnline(user: User):
    if user.status.recently:
        return "Recently"
    elif user.status.within_week:
        return "Within the last week"
    elif user.status.within_month:
        return "Within the last month"
    elif user.status.long_time_ago:
        return "A long time ago :("
    elif user.status.online:
        return "Currently Online"
    elif user.status.offline:
        return timedate(user.status.date)

async def GetCommon(get_user):
    common = await BOT.send(
        functions.messages.GetCommonChats(
            user_id = BOT.resolve_peer(get_user),
            max_id = 0,
            limit = 0
        )
    )
    return common

async def SendLong(message: Message, cmdstr: str, result):
    async with aiofiles.open("output.txt", 'w+', encoding = 'utf8') as f:
        f.write(str(result))
    await BOT.send_document(
        chat_id = message.chat.id,
        document = "output.txt",
        caption = "`Output too long, sent as file.`",
        reply_to_message_id = ReplyCheck(message)
    )
    os.remove("output.txt")

def SpeedConvert(size):
    power = 2**10
    zero = 0
    units = {
        0 : '',
        1: 'Kbit/s',
        2: 'Mbit/s',
        3: 'Gbit/s',
        4: 'Tbit/s'}
    while size > power:
        size /= power
        zero += 1
    return "{} {}".format(round(size, 2),units[zero])

  

def FullName(user: User):
    return user.first_name + " " + user.last_name if user.last_name else user.first_name

def ProfilePicUpdate(user_pic):
    return timedate(user_pic.photos[0].date)

async def GetOwnMessages(message):
    all_msgs = await BOT.iter_history(
        chat_id = message.chat.id)

    to_delete = []
    for msg in all_msgs:
        if (
            msg.message_id
            >= (
                message.reply_to_message.message_id
                if message.reply_to_message
                else 0
            )
        ) and message.from_user.is_self:
            await to_delete.append(msg.message_id)

    return to_delete
    
    
    
bann = """fuck
fuck you
ya mami
ya eggs
ya ekk
sex
bop
kiss
smoke
weed
mami
pima
banga
penis
vagina
womb
bitch
gay
lesbian
breast
leak
fu ck
les bian
pe*nis
les bi
wtf
shit
getcryptotab
getcryptotab.com
etu.link
i/?r=
freebitco.in
https://freebitco.in/?r=
birch
nyam
moof
d$$k
d**k
dk
https://dent.app.link/
http://dent.app.link
dent.app.link
dent.app
http://t.cn
t.cn
www.t.cn
inbox
for sale
dents
momopays
momo pays
https://whatsapppay.org
www.whatsapppay.org
whatsapppay
bitmex
https://bitmex-blogs.com/
k28iye2vyiqzrre0butkgg
bitmex-blogs
bitmex-blogs.com
http://www.coinimp.com
coinimp.com
btc bot
buy btc
earn btc
bitmex competition
btc giveaway"""