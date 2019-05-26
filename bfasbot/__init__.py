import sys
import os, sqlite3
import logging, threading, signal 
from datetime import datetime
import logging, glob
 

def exception_hook(exc_type, exc_value, exc_traceback):
    logging.error(
        "Uncaught exception",
        exc_info=(exc_type, exc_value, exc_traceback)
    )  
 
sys.excepthook = exception_hook  

from pathlib import Path
from pyrogram import Client, Filters, MessageHandler
from bfasbot.pyrawait import AwaitableClient

from pyrogram.errors import (UserIsBlocked, FloodWait, FileIdInvalid, BadRequest, Flood, InternalServerError, SeeOther, Unauthorized, UnknownError, MessageNotModified, UsernameNotOccupied, MessageEmpty, UserAdminInvalid, ChatAdminRequired, PeerIdInvalid)
from pyrogram import __version__ as Version
import logging
from logging.handlers import RotatingFileHandler
from logging import handlers
import sys
# Import the duallog package to set up simultaneous logging to screen and console.
import bfasbot.duallog


logging.debug('Silently Initializing.')
logging.getLogger("pyrogram").setLevel(logging.WARN)
LOGS = logging.getLogger(__name__)
known_sessions_file = os.path.join(os.path.dirname(__file__), 'logtest')
# Set up dual logging and tell duallog where to store the logfiles.
duallog.setup(known_sessions_file)

# Generate some log messages.
 

import re
def ck(s):
    return re.match(r"[-+]?\d+$", s) is not None
# Check for Python 3.6 or newer
if sys.version_info[0] < 3 or sys.version_info[1] < 5:
    LOGS.error("You MUST use at least Python 3.6. Bot Quitting")
    quit(1)

# Now for the rest
__version__ = '0.5.0'
__author__  = 'Bfasbot Ultra'
__source__      = 'https://github.com/Bfas237/bfasbot'
__copyright__   = 'Copyright (c) 2019 ' + __author__
__copystring__  = "BfasBot v{} | {}".format(__version__, __copyright__)
__python_version__ = "Python v{}".format(str(sys.version_info[0])+"."+str(sys.version_info[1]))
__pyrogram__ = "Pyrogram v{}".format(Version)
cmds = ["#","!",".", "-"]
# Load our .env file

# Get the Values from our .env
API_ID = os.environ.get("api_id")
API_HASH = os.environ.get("api_hash")
BASE = "https://del.dog"
LOGGER = os.environ.get("LOGGER")
LOGGER_GROUP = int(os.environ.get("LOGGER_GROUP"))
ACCGEN_API = os.environ.get("ACCGEN_API")
def timedate(dat):
    import timeago, datetime
    now = datetime.datetime.now() + datetime.timedelta(seconds = 1)
    date = datetime.datetime.now()
    return timeago.format(dat, now)

def response_hook(resp, *args, **kwargs):
    # parse the json storing the result on the response object
    resp.data = resp.json()


def run_async(func):
	
	from threading import Thread
	from functools import wraps

	@wraps(func)
	def async_func(*args, **kwargs):
		func_hl = Thread(target = func, args = args, kwargs = kwargs)
		func_hl.start()
		return func_hl

	return async_func


import pickle
with open('wel', 'wb') as f:
  pickle.dump({}, f)
with open('warn', 'wb') as f:
   pickle.dump({}, f)
with open('plugins', 'wb') as f:
   pickle.dump({}, f)
                 
PYRO_DB = str(Path(__file__).parent.parent / 'bfasbot.db')

LOGS.warning("Checking Databased...")
db = sqlite3.connect(PYRO_DB)
c = db.cursor()
#c.executescript('''DROP TABLE IF EXISTS blacklist;''')
c.executescript(
    "CREATE TABLE IF NOT EXISTS welcome "
    "(chat_id INT UNIQUE ON CONFLICT FAIL, greet TEXT, chat_title TEXT);"
    "CREATE TABLE IF NOT EXISTS blacklist "
    "(chat_id INT, greet TEXT, chat_title TEXT);"
    )
db.commit()
db.close()
LOGS.warning("Check done.")


    
# Prepare the bot
BOT = AwaitableClient(
    session_name = "Bfschat",
    api_id=API_ID,
  api_hash=API_HASH,
    app_version = "Bfasbot \U0001f525\U0001F916 v{}".format(__version__)
)

# Global Variables
MAINTENANCE = "off"
DOWN = "⛔️"
UP = "\U0001f525"
ISAFK = True
AFKREASON = "Busy with studies"
START_TIME = datetime.now()
USERS = {}
SPAM = False
WIDE_MAP = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F))
WIDE_MAP[0x20] = 0x3000
COUNT_PM = {}
MUTING_USERS = {}
MUTED_USERS = {}
HELPER = {}
SPAM_ALLOWANCE = 3
SPAM_CHAT_ID = []
COUNT_MSG = 0
HELPER = {}
DEACT = False
ACT = True
LOAD = ""

