from time import sleep, time

from pyrobot import BOT, LOGS
from pyrogram import Filters, Message
from pyrogram.errors import UserAdminInvalid

from ..interval import IntervalHelper
from ..constants import Admin
from ..helpers import (
    CheckAdmin, CheckReplyAdmin, LogMessage,
    Timer, TimerString, RestrictFailed)


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
