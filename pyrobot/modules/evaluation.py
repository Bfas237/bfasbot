import os
from time import sleep

from pyrogram import Filters, Message
from pyrogram.api import functions, types

from pyrobot import BOT, LOGS

from ..constants import Eval
from ..helpers import ReplyCheck, SendLong, LogMessage

@BOT.on_message(Filters.command("eval", ".") & Filters.me)
def evaluation(bot: BOT, message: Message):
    try:
        cmdstr = " ".join(message.command[1:])
    except IndexError:
        message.edit("__I can't evaluate nothing...__")
        sleep(2)
        message.delete()
        return

    if cmdstr:
        expr = message.reply(Eval.RUNNING.format(cmdstr))

        try:
            result = eval(cmdstr)
        except Exception as err:
            expr.edit(Eval.ERROR.format(cmdstr, err))
            LogMessage(Eval.ERROR_LOG.format(
                    cmdstr,
                    message.chat.title or message.chat.first_name,
                    str(message.chat.id).replace("-100", ""),
                    str(expr.message_id),
                    err
                ))

        else:

            if result is None:
                expr.edit(Eval.SUCCESS.format(cmdstr))
                LogMessage(Eval.SUCCESS_LOG.format(
                    cmdstr,
                    message.chat.title or message.chat.first_name,
                    str(message.chat.id).replace("-100", ""),
                    str(expr.message_id)))

            elif len(Eval.RESULT.format(cmdstr, result)) > 4096:
                expr.edit(Eval.RESULT_FILE.format(cmdstr))
                BOT.send_chat_action(message.chat.id, "upload_document")
                SendLong(expr, cmdstr, result)

            else:
                expr.edit(Eval.RESULT.format(cmdstr, result))

            LogMessage(Eval.RESULT_LOG.format(
                cmdstr,
                message.chat.title or message.chat.first_name,
                str(message.chat.id).replace("-100", ""),
                str(expr.message_id)))
 
@BOT.on_message(Filters.command("exec", ".") & Filters.me)
def execution(bot: BOT, message: Message):
    try:
        cmdstr = message.text[6:]
    except IndexError:
        message.edit("__I can't execute nothing...__")
        sleep(2)
        message.delete()
        return

    if cmdstr:
        expr = message.reply(Eval.RUNNING.format(cmdstr))

        try:
            exec(
                'def __ex(bot, message): '
                + ''.join(
                    '\n '
                    + l for l in cmdstr.split('\n')))
            result = locals()['__ex'](bot, message)

        except Exception as err:
            expr.edit(Eval.ERROR.format(cmdstr, err))
            LogMessage(Eval.ERROR_LOG.format(
                cmdstr,
                message.chat.title or message.chat.first_name,
                str(message.chat.id).replace("-100", ""),
                str(expr.message_id),
                err))

        else:
            if result:
                expr.edit(Eval.RESULT.format(cmdstr, result))
                LogMessage(Eval.RESULT.format(
                    cmdstr,
                    message.chat.title or message.chat.first_name,
                    str(message.chat.id).replace("-100", ""),
                    str(expr.message_id)))
            else:
                expr.edit(Eval.SUCCESS.format(cmdstr))
                LogMessage(Eval.SUCCESS_LOG.format(
                    cmdstr,
                    message.chat.title or message.chat.first_name,
                    str(message.chat.id).replace("-100", ""),
                    str(expr.message_id)))
