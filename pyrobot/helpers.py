from time import sleep, strftime, time
from datetime import datetime
import requests
import os

from pyrogram import Message, User
from pyrogram.api import functions

from pyrobot import BOT, LOGGER, LOGGER_GROUP, ACCGEN_API

from .interval import IntervalHelper

def CheckAdmin(message: Message):
    """Check if we are admin."""

    admin = 'administrator'
    creator = 'creator'
    ranks = [admin, creator]

    SELF = BOT.get_chat_member(
        chat_id = message.chat.id,
        user_id = message.from_user.id)

    if SELF.status not in ranks:
        message.edit("__I'm not Admin!__")
        sleep(2)
        message.delete()

    else:
        if SELF.status is not admin:
            return True
        elif SELF.permissions.can_restrict_members:
            return True
        else:
            message.edit("__No Permissions to restrict Members__")
            sleep(2)
            message.delete()

def CheckReplyAdmin(message: Message):
    """Check if the message is a reply to another user."""
    if not message.reply_to_message:
        message.edit("`?{}` needs to be a reply".format(message.command[0]))
        sleep(2)
        message.delete()
    elif message.reply_to_message.from_user.is_self:
        message.edit("I can't {} myself.".format(message.command[0]))
        sleep(2)
        message.delete()
    else:
        return True

def Timer(message: Message):
    if len(message.command) > 1:
        secs = IntervalHelper(message.command[1])
        return int(str(time()).split(".")[0] + secs.to_secs()[0])
    else:
        return 0
def TimerString(message: Message):
    secs = IntervalHelper(message.command[1])
    return "{} {}".format(secs.to_secs()[1], secs.to_secs()[2])

def RestrictFailed(message: Message):
    message.edit("I can't {} this user.".format(message.command[1]))
    sleep(2)
    message.delete()


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id

def LogMessage(logmsg):
    if LOGGER:
        BOT.send_message(
            chat_id = LOGGER_GROUP,
            text = logmsg
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
        return datetime.fromtimestamp(user.status.date).strftime("%a, %d %b %Y, %H:%M:%S")

def GetCommon(get_user):
    common = BOT.send(
        functions.messages.GetCommonChats(
            user_id = BOT.resolve_peer(get_user),
            max_id = 0,
            limit = 0
        )
    )
    return common

def SendLong(message: Message, cmdstr: str, result):
    with open("output.txt", 'w+', encoding = 'utf8') as f:
        f.write(str(result))
    BOT.send_document(
        chat_id = message.chat.id,
        document = "output.txt",
        caption = "`Output too long, sent as file.`",
        reply_to_message_id = ReplyCheck(message)
    )
    os.remove("output.txt")

def GetAccount():
    API = "https://accgen.cathook.club/api/v1/account/" + ACCGEN_API
    r = requests.get(API)
    return r.json()

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
