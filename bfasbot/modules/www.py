from datetime import datetime
import speedtest

from pyrogram import Filters, Message
from pyrogram.api import functions

from bfasbot import BOT

from ..helpers import SpeedConvert, LogMessage
from ..constants import www

@BOT.on_message(Filters.command("speed", ".") & Filters.me)
def speed_test(bot: BOT, message: Message):
    new_msg = message.edit(
        "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = message.edit(
        "`{}`\n"
        "`Getting best server based on ping . . .`".format(new_msg.text))
    spd.get_best_server()

    new_msg = message.edit(
        "`{}`\n"
        "`Testing download speed . . .`".format(new_msg.text))
    spd.download()

    new_msg = message.edit(
        "`{}`\n"
        "`Testing upload speed . . .`".format(new_msg.text))
    spd.upload()

    new_msg = new_msg.edit(
        "`{}`\n"
        "`Getting results and preparing formatting . . .`".format(new_msg.text))
    results = spd.results.dict()

    message.edit(
        www.SpeedTest.format(
            start = results['timestamp'],
            ping = results['ping'],
            download = SpeedConvert(results['download']),
            upload = SpeedConvert(results['upload']),
            isp = results['client']['isp']
        ))

@BOT.on_message(Filters.command("dc", ".") & Filters.me)
def neardc(bot: BOT, message: Message):
    dc = BOT.send(
        functions.help.GetNearestDc())
    message.edit(
        www.NearestDC.format(
            dc.country,
            dc.nearest_dc,
            dc.this_dc))

@BOT.on_message(Filters.command("ping", ".") & Filters.me)
def pingme(bot: BOT, message: Message):
    start = datetime.now()
    message.edit('`Pong!`')
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    message.edit("**Pong!**\n`{} ms`".format(ms))
