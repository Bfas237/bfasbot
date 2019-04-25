import sys
import os
import logging
from datetime import datetime
from pyrogram import Client
import dotenv
from pyrogram.errors import UserIsBlocked, FloodWait, FileIdInvalid, UsernameNotOccupied

# We need logging this early for our Version Check
logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARN)
LOGS = logging.getLogger(__name__)

# Check for Python 3.6 or newer
if sys.version_info[0] < 3 or sys.version_info[1] < 5:
    LOGS.error("You MUST use at least Python 3.6. Bot Quitting")
    quit(1)

# Now for the rest

__version__ = '0.0.1'
__author__  = 'Ningmua Bruno'
__source__      = 'None'
__copyright__   = 'Copyright (c) 2019 ' + __author__
__copystring__  = "BfasBot v{} | {}".format(__version__, __copyright__)
cmds = ["#","!","."]
# Load our .env file
dotenv.load_dotenv()

# Get the Values from our .env
API_ID = os.environ.get("api_id")
API_HASH = os.environ.get("api_hash")

LOGGER = os.environ.get("LOGGER")
LOGGER_GROUP = int(os.environ.get("LOGGER_GROUP"))
ACCGEN_API = os.environ.get("ACCGEN_API")

import pickle
with open('wel', 'wb') as f:
  pickle.dump({}, f)
 
# Prepare the bot
BOT = Client(
    session_name = "install",
    api_id=API_ID,
  api_hash=API_HASH,
    app_version = "Bfasbot \U0001f525\U0001F916 v{}".format(__version__)
)

# Global Variables
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