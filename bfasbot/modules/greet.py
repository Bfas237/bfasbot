import sqlite3
from time import sleep
from html import escape, unescape
import asyncio
from pyrogram import Filters, Message
from bfasbot import BOT, LOGS, cmds, run_async, PYRO_DB, LOGGER_GROUP

from ..helpers import LogMessage

# -- Constants -- #

SET_WELCOME = """INSERT OR FAIL INTO welcome VALUES ('{}', "{}", "{}")"""
GET_WELCOME = "SELECT greet FROM welcome WHERE chat_id='{}'"
ALL_WELCOME = "SELECT chat_title, greet FROM welcome"
REMOVE_WELCOME = "DELETE FROM welcome WHERE chat_id='{}'"

# -- Constants End -- #

# -- Helpers -- #


async def PrivateCheck(message: Message):
    if message.chat.type == 'private':
        await message.edit("Welcome messages are not supported in Private Chats.")
        sleep(2)
        await message.delete()
        return None
    return True

# -- Helpers End -- #

        
@BOT.on_message(Filters.command("set", cmds) & Filters.me)
async def sets_welcome(bot: BOT, message: Message):
    if PrivateCheck(message):
        cmd = message.command
        if len(cmd) == 1:
            if not message.reply_to_message:
                await message.edit("Sorry but that was an invalid action.\n\n `Syntax: [.|!|#]<cmd> <message>`.")
            elif message.reply_to_message:
                welcome_text = message.reply_to_message.text
        elif len(cmd) > 1:
            welcome_text = message.text.markdown[5:]
        db = sqlite3.connect(PYRO_DB)
        c = db.cursor()
        try:
            c.execute(SET_WELCOME.format(message.chat.id, escape(welcome_text), message.chat.title))
            await message.edit(
                "__I will now welcome all new users with:__\n\n" + welcome_text,
                disable_web_page_preview=True)
            sleep(5)
            await message.delete()
        except sqlite3.IntegrityError:
            c.execute(GET_WELCOME.format(message.chat.id))
            res = c.fetchone()
            c.execute(REMOVE_WELCOME.format(message.chat.id))
            c.execute(SET_WELCOME.format(message.chat.id, escape(welcome_text), message.chat.title))
            await message.edit(
                "🗑 **Previous:** \n\n"
                + unescape(res[0])
                + "\n\n✅ **Current:**\n\n"
                + welcome_text,
                disable_web_page_preview=True)
            sleep(5)
            await message.delete()
        db.commit()


@BOT.on_message(Filters.command("unset", cmds) & Filters.me)
async def remove_welcome(bot: BOT, message: Message):
    if PrivateCheck(message):
        db = sqlite3.connect(PYRO_DB)
        c = db.cursor()
        c.execute(GET_WELCOME.format(message.chat.id))
        res = c.fetchone()
        if res:
            c.execute(REMOVE_WELCOME.format(message.chat.id))
            db.commit()
            await message.edit(
                "🗑 **Deleted Welcome Message:** \n\n" + unescape(res[0]),
                disable_web_page_preview=True)
        else:
            await message.edit("🤷🏻‍♂️ There was no welcome message.")
        sleep(3)
        await message.delete()


@BOT.on_message(Filters.command("show", cmds) & Filters.me)
async def get_welcome(bot: BOT, message: Message):
    if PrivateCheck(message):
        db = sqlite3.connect(PYRO_DB)
        c = db.cursor()
        c.execute(GET_WELCOME.format(message.chat.id))
        res = c.fetchone()
        if res:
            await message.edit(
                "🧿 **This chats welcome message:**\n\n" + unescape(res[0]),
                disable_web_page_preview=True)
        else:
            await message.edit("🤷🏻‍♂️ __There is no welcome message for this chat.__")
        sleep(3)
        await message.delete()



@BOT.on_message(Filters.command("wels", cmds) & Filters.me)
async def all_welcome(bot: BOT, message: Message):
    db = sqlite3.connect(PYRO_DB)
    c = db.cursor()
    c.execute(ALL_WELCOME)
    res = c.fetchall()
    if res:
        welcome_messages = "**All Welcome Messages:**\n"
        for welcome in res:
            welcome_messages += "\n👉 **{}**\n\n{}\n".format(welcome[0], unescape(welcome[1]))
        await BOT.send_message(LOGGER_GROUP, welcome_messages, disable_web_page_preview=True)
        await message.edit("Welcome messages sent in Saved Messages.")
        sleep(2)
        await message.delete()
    else:
        await message.edit("__There is no welcome message for this chat.__")
        sleep(3)
        await message.delete()


# Actually greet new people
@BOT.on_message(Filters.new_chat_members)
async def greet_new_users(bot: BOT, message: Message):
    new = message.new_chat_members
    db = sqlite3.connect(PYRO_DB)
    c = db.cursor()
    c.execute(GET_WELCOME.format(message.chat.id))
    res = c.fetchone()
    if res:
        welcome_text = res[0].replace(
            "{name}",
            ", ".join("{}".format(
                usr.first_name) for usr in new)
        ).replace(
            "{namelink}",
            ", ".join("[{}](tg://user?id={})".format(
                usr.first_name, usr.id) for usr in new)
        ).replace(
            "{title}",
            "{message.chat.title}"
        )
        greet = await message.reply(
            unescape(welcome_text),
            disable_web_page_preview=True,
            disable_notification=True)
        await LogMessage(
            "Greeted new users in \"[{}](t.me/c/{}/{})\":\n{}".format(
                message.chat.title,
                str(greet.chat.id).replace("-100", ""),
                str(greet.message_id),
                ", ".join(usr.first_name for usr in new)))