from bfasbot import (LOAD, BOT, cmds, run_async)
from pyrogram import Filters, Message

def load():
    from os.path import dirname, basename, isfile
    import glob
    global LOAD

    mod_ = glob.glob(dirname(__file__) + "/*.py")
    all_mod = [
        basename(f)[:-3]
        for f in mod_
        if isfile(f) and f.endswith(".py")
    ]
    ALL_MODULES = sorted(all_mod)
    LOAD = "🧿 **Modules Loaded**: {}\n\n**Active:** {}\n".format(len(ALL_MODULES), ", ".join(ALL_MODULES))
    return LOAD
 
@BOT.on_message(Filters.command("all", cmds) & Filters.outgoing)
async def _loads(bot: BOT, message: Message):
    global LOAD
    LOADS = load()
    await message.edit(LOAD, disable_web_page_preview=True)
