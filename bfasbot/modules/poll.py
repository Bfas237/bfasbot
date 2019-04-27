from time import sleep

from pyrogram import Filters, Message
from bfasbot import BOT

from ..helpers import LogMessage, ReplyCheck

@BOT.on_message(Filters.command("poll", ".") & Filters.me)
def make_poll(bot: BOT, message: Message):
    cmd = message.command
    if len(cmd) is 1:
        message.edit("I need a question")
        sleep(2)
        message.delete()
    elif len(cmd) > 1:
        poll = message.text[6:].split('\n')
        if len(poll[1:]) < 2:
            message.edit("I need at least two answers")
        elif len(poll[1:]) > 10:
            message.edit("A poll can only have 10 answers")
        else:
            print(poll[0])
            print(poll[1:])
            sent_poll = bot.send_poll(
                chat_id = message.chat.id,
                question = poll[0],
                options = poll[1:],
                reply_to_message_id = ReplyCheck(message))
            message.edit("Poll created")
            LogMessage(
                "Poll \"{}\" send to \"[{}](t.me/c/{}/{})\"".format(
                    sent_poll.poll.question,
                    sent_poll.chat.title or sent_poll.chat.first_name,
                    str(sent_poll.chat.id).replace("-100", ""),
                    sent_poll.message_id
                )
            )
            message.delete()
