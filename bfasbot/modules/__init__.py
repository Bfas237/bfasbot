from bfasbot import (LOGS, LOAD, BOT, cmds, __source__, __author__, response_hook, run_async, BASE)
from pyrogram import Filters, Message
from ..constants import rog
from requests_futures.sessions import FuturesSession
import re
def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob
    global LOAD

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    
    return all_modules

ALL_MODULES = sorted(__list_all_modules())
LOGS.info("Modules to load:\n{}\n".format(", ".join(ALL_MODULES)))
__all__ = ALL_MODULES + ["ALL_MODULES"]
