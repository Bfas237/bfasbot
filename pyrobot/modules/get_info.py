from time import sleep
from html import escape, unescape

from pyrobot import cmds
from pyrogram import Filters, Message
from pyrobot import BOT
from ..constants import GetInfo
from ..helpers import LogMessage

@BOT.on_message(Filters.command("admins", cmds) & Filters.me)
def get_admins(bot: BOT, message: Message):
    if message.chat.type == 'private':
        message.edit("There are no admins in private chats...")
        sleep(2)
        message.delete()

    else:
        all_admins = BOT.iter_chat_members(
            chat_id = message.chat.id,
            filter = 'administrators')
        creator = None
        admins = []

        for admin in all_admins:
            if admin.status is 'creator':
                creator = admin
            elif admin.status is 'administrator':
                admins.append(admin)
        sorted_admins = sorted(admins, key = lambda usid: usid.user.id)

        AdminList = GetInfo.ADMINTITLE.format(message.chat.title)

        if creator:
            AdminList += GetInfo.ADMINCREATOR.format(
                str(creator.user.id).rjust(10),
                creator.user.first_name,
                creator.user.id)

        AdminList += "╔ **Admins**\n"
        for admin in sorted_admins:
            if admin is sorted_admins[-1]:
                if admin.user.is_bot:
                    AdminList += GetInfo.ADMINLISTLASTBOT.format(
                        str(admin.user.id).rjust(10),
                        admin.user.first_name,
                        admin.user.id)
                else:
                    AdminList += GetInfo.ADMINLISTLAST.format(
                        str(admin.user.id).rjust(10),
                        admin.user.first_name,
                        admin.user.id)
            else:
                if admin.user.is_bot:
                    AdminList += GetInfo.ADMINLISTBOT.format(
                        str(admin.user.id).rjust(10),
                        admin.user.first_name,
                        admin.user.id)
                else:
                    AdminList += GetInfo.ADMINLIST.format(
                        str(admin.user.id).rjust(10),
                        admin.user.first_name,
                        admin.user.id)

        message.edit(AdminList)
        LogMessage(AdminList)

@BOT.on_message(Filters.command("members", cmds) & Filters.me)
def get_members(bot: BOT, message: Message):
    if message.chat.type is 'private':
        message.delete()

    else:
        total   = 0
        admins  = 0
        members = 0
        bots    = 0
        deleted = 0

        for member in BOT.iter_chat_members(message.chat.id):
            total += 1
            if member.user.is_bot:
                bots += 1
            elif member.user.is_deleted:
                deleted += 1
            elif member.status in ['creator', 'administrator']:
                admins += 1
            elif not member.user.is_deleted and not member.user.is_bot:
                members += 1

        member_count_text = GetInfo.MEMBER_INFO.format(
            message.chat.title,
            total,
            admins,
            members,
            bots,
            deleted
        )

        message.edit(member_count_text)
        LogMessage(member_count_text)
