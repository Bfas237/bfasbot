from time import sleep, time
import pickle
from bfasbot import BOT, LOGS, ck, cmds
from pyrogram import Filters, Message
from pyrogram.errors import UserAdminInvalid, ChatAdminRequired
from datetime import datetime
from ..interval import IntervalHelper
from ..constants import Admin
from time import mktime
from ..helpers import (
    CheckAdmin, CheckReplyAdmin, LogMessage,
    Timer, TimerString, RestrictFailed)
spamcount = 0
spamlimit = 3
sleeptime = 0
spamtime = 0
spamwait = 10
wait = 0
style_chats = {}
help_message = ''

@BOT.on_message(Filters.command("ban", "?") & Filters.me)
def ban_hammer(bot: BOT, message: Message):
    if CheckReplyAdmin(message) is True:
        if CheckAdmin(message) is True:
            try:
                BOT.kick_chat_member(
                    chat_id = message.chat.id,
                    user_id = message.reply_to_message.from_user.id,
                    until_date = Timer(message)
                )
                if len(message.command) > 1:
                    message.edit(
                        Admin.BANNED_TIME.format(
                            message.reply_to_message.from_user.first_name,
                            TimerString(message)))
                else:
                    message.edit(Admin.BANNED.format(
                        message.reply_to_message.from_user.first_name))
                LogMessage(Admin.BANNED_LOG.format(
                    message.reply_to_message.from_user.first_name,
                    message.reply_to_message.from_user.id,
                    message.chat.title,
                    str(message.chat.id).replace("-100", ""),
                    str(message.reply_to_message.message_id)))

            except UserAdminInvalid:
                RestrictFailed(message)

@BOT.on_message(Filters.command("unban", "?") & Filters.me)
def unban(bot: BOT, message: Message):
    if CheckReplyAdmin(message) is True:
        if CheckAdmin(message) is True:
            try:
                BOT.unban_chat_member(
                    chat_id = message.chat.id,
                    user_id = message.reply_to_message.from_user.id
                )
                message.edit(Admin.UNBANNED.format(
                    message.reply_to_message.from_user.first_name))
                LogMessage(Admin.UNBANNED_LOG.format(
                    message.reply_to_message.from_user.first_name,
                    message.reply_to_message.from_user.id,
                    message.chat.title,
                    str(message.chat.id).replace("-100", ""),
                    str(message.message_id)))

            except UserAdminInvalid:
                message.edit("I can't unban this user")

@BOT.on_message(Filters.command("mute", "?") & Filters.me)
def mute_hammer(bot: BOT, message: Message):
    if CheckReplyAdmin(message) is True:
        if CheckAdmin(message) is True:
            try:
                BOT.restrict_chat_member(
                    chat_id = message.chat.id,
                    user_id = message.reply_to_message.from_user.id,
                    until_date = Timer(message),
                    can_send_messages = False,
                )
                if len(message.command) > 1:
                    message.edit(Admin.MUTED_TIME.format(
                        message.reply_to_message.from_user.first_name,
                        TimerString(message)))
                else:
                    message.edit(Admin.MUTED.format(
                        message.reply_to_message.from_user.first_name))
                LogMessage(Admin.MUTED_LOG.format(
                    message.reply_to_message.from_user.first_name,
                    message.reply_to_message.from_user.id,
                    message.chat.title,
                    str(message.chat.id).replace("-100", ""),
                    str(message.reply_to_message.message_id)))

            except UserAdminInvalid:
                RestrictFailed(message)

            except ChatAdminRequired:
                RestrictFailed(message)

@BOT.on_message(Filters.command("unmute", "?") & Filters.me)
def unmute(bot: BOT, message: Message):
    if CheckReplyAdmin(message) is True:
        if CheckAdmin(message) is True:
            try:
                BOT.restrict_chat_member(
                    chat_id = message.chat.id,
                    user_id = message.reply_to_message.from_user.id,
                    until_date = 0,
                    can_send_messages = True,
                    can_send_media_messages = True,
                    can_send_other_messages = True,
                    can_add_web_page_previews = True,
                    can_send_polls = True,
                    can_change_info = True,
                    can_invite_users = True,
                    can_pin_messages = True
                )
                message.edit(Admin.UNMUTED.format(
                    message.reply_to_message.from_user.first_name))
                LogMessage(Admin.UNMUTED_LOG.format(
                    message.reply_to_message.from_user.first_name,
                    message.reply_to_message.from_user.id,
                    message.chat.title,
                    str(message.chat.id).replace("-100", ""),
                    str(message.message_id)))

            except UserAdminInvalid:
                RestrictFailed(message)

            except ChatAdminRequired:
                RestrictFailed(message)

@BOT.on_message(Filters.command("kick", "?")  & Filters.me)
def kick_user(bot: BOT, message: Message):
    if CheckReplyAdmin(message) is True:
        if CheckAdmin(message) is True:
            try:
                BOT.kick_chat_member(
                    chat_id = message.chat.id,
                    user_id = message.reply_to_message.from_user.id,
                    until_date = 0
                )
                BOT.unban_chat_member(
                    chat_id = message.chat.id,
                    user_id = message.reply_to_message.from_user.id
                )
                message.edit(Admin.KICKED.format(
                    message.reply_to_message.from_user.first_name))
                LogMessage(Admin.KICKED_LOG.format(
                    message.reply_to_message.from_user.first_name,
                    message.reply_to_message.from_user.id,
                    message.chat.title,
                    str(message.chat.id).replace("-100", ""),
                    str(message.reply_to_message.message_id)))

            except UserAdminInvalid:
                RestrictFailed(message)

            except ChatAdminRequired:
                RestrictFailed(message)



@BOT.on_message(Filters.command("mod", "?") & Filters.me)
def unmute(bot: BOT, message: Message):
    if CheckReplyAdmin(message) is True:
        if CheckAdmin(message) is True:
            try:
                BOT.promote_chat_member(
                    chat_id = message.chat.id,
                    user_id = message.reply_to_message.from_user.id,
                    can_edit_messages = True,
                    can_delete_messages = True,
                    can_restrict_members = True,
                    can_invite_users = True
                )
                message.edit(Admin.PROMOTED.format(
                    message.reply_to_message.from_user.first_name))
                LogMessage(Admin.PROMOTED_LOG.format(
                    message.reply_to_message.from_user.first_name,
                    message.reply_to_message.from_user.id,
                    message.chat.title,
                    str(message.chat.id).replace("-100", ""),
                    str(message.message_id)))

            except UserAdminInvalid:
                RestrictFailed(message)

            except ChatAdminRequired:
                RestrictFailed(message)

                                


@BOT.on_message(Filters.command("unmod", "?") & Filters.me)
def unmute(bot: BOT, message: Message):
    if CheckAdmin(message) is True:
            from_user=""
            cmd = " ".join(message.command[1:])
            
            if cmd:
              if ck(cmd):
                from_user = BOT.resolve_peer(cmd).user_id
              else:
                  from_user = BOT.get_users(cmd)
              print(from_user)
            else:
              from_user = message.reply_to_message
            rep = message.reply_to_message
            try:
                BOT.promote_chat_member(
                    chat_id = message.chat.id,
                    user_id = from_user.id,
                    can_edit_messages = False,
                    can_delete_messages = False,
                    can_restrict_members = False,
                    can_invite_users = False,
                    can_promote_members = False,
                    can_pin_messages = False,
                    can_change_info = False
                  
                  
                )
                message.edit(Admin.UNPROMOTED.format(
                    rep.from_user.first_name if rep else from_user.first_name))
                LogMessage(Admin.UNPROMOTED_LOG.format(
                    rep.from_user.first_name if rep else from_user.first_name,
                    rep.from_user.id if rep else from_user.id,
                    message.chat.title,
                    str(message.chat.id).replace("-100", ""),
                    str(message.message_id)))

            except UserAdminInvalid:
                RestrictFailed(message)

            except ChatAdminRequired:
                RestrictFailed(message)

                
                
@BOT.on_message(Filters.me & Filters.command('rwarn', cmds))
def warn(client, message):
    with open('warn', 'rb') as f:
        warnings = pickle.load(f)
    if sleeptime < time():
        rpl_user = message.reply_to_message.from_user
        if message.chat.id in warnings:
            if message.reply_to_message.from_user.id in warnings[message.chat.id]:
                warnings[message.chat.id][message.reply_to_message.from_user.id] += 1
            else:
                warnings[message.chat.id][message.reply_to_message.from_user.id] = 1
        else:
            warnings[message.chat.id] = {message.reply_to_message.from_user.id: 1}
        with open('warn', 'wb') as f:
            pickle.dump(warnings, f)
        warns = warnings[message.chat.id][message.reply_to_message.from_user.id]
        if warns == 2:
            now = datetime.now()
            until = datetime(now.year, now.month, now.day, now.hour + 1)
            client.restrict_chat_member(message.chat.id,
                                        rpl_user.id,
                                        until_date=int(mktime(until.timetuple()) + 1e-6 * until.microsecond),
                                        can_send_messages=False,
                                        can_change_info=False,
                                        can_invite_users=False,
                                        can_pin_messages=False)
        elif warnings[message.chat.id][message.reply_to_message.from_user.id] == 3:
            client.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            client.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            message.reply('[{}]({}) is #kicked for {}'.format(message.reply_to_message.from_user.first_name,
                                                              'tg://user?id={}'.format(
                                                                  message.reply_to_message.from_user.id),
                                                              'Having 3 Warns'))
        message.edit('[{}]({}) is #warned for {} `{}`'.format(message.reply_to_message.from_user.first_name,
                                                              'tg://user?id={}'.format(
                                                                  message.reply_to_message.from_user.id),
                                                              " ".join(message.command[1:]),
                                                              warnings[message.chat.id][
                                                                  message.reply_to_message.from_user.id]))


    
    

@BOT.on_message(Filters.me & Filters.command('nowarn', '?'))
def warn(client, message):
    with open('warn', 'rb') as f:
        warnings = pickle.load(f)
    rpl_user = message.reply_to_message.from_user
    
    
    if message.chat.id in warnings:
        if message.reply_to_message.from_user.id in warnings[message.chat.id]:
            warnings[message.chat.id][message.reply_to_message.from_user.id] += 1
        else:
            warnings[message.chat.id][message.reply_to_message.from_user.id] = 1
    else:
        warnings[message.chat.id] = {message.reply_to_message.from_user.id: 1}
    with open('warn', 'wb') as f:
        pickle.dump(warnings, f)
    warns = warnings[message.chat.id][message.reply_to_message.from_user.id]

    message.reply(warns)