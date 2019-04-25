import requests
from time import sleep

from pyrogram import Filters, Message
from pyrobot import BOT, ACCGEN_API

from ..constants import Steam
from ..helpers import GetAccount


@BOT.on_message(Filters.command("acc", "?") & Filters.me)
def steam_accgen(bot: BOT, message: Message):
    if ACCGEN_API is None or "":
        message.edit("You need to set an API Key.\n"
                     "Get one from @sag_stats_bot")
        sleep(3)
        message.delete()
        return
    acc = GetAccount()
    # Uncomment if you want to save to console output
    # LOGS.info(acc)
    message.edit(
        Steam.ACC_MSG.format(
            login = acc['login'],
            password = acc['password'],
            steamid = acc['steamid']
        ),
        disable_web_page_preview = True
    )
