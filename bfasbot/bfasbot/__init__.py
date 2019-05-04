import sys
import os
import logging, threading, signal 
from datetime import datetime
# We need logging this early for our Version Check
logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO)

from pyrogram import Client, Filters, MessageHandler
from concurrent.futures import Future
import asyncio

class AwaitableFuture(Future):
    def __await__(self):
        return (yield from asyncio.wrap_future(self))

class Conversation:
    def __init__(self, client: Client, peer):
        self.peer = peer
        self.client = client
        self.handlers = []
        self.msgs = []
        self.message_handler = MessageHandler(self.handle_message,Filters.chat(self.peer))
        self.last_sent_id = 0
    def handle_message(self, _, message):
        if not self.check(message):
            self.msgs.append(message)
        message.stop_propagation()
    def add_awaiter(self, filters):
        fut = AwaitableFuture()
        self.handlers.append((filters,fut))
        return fut
    def check(self,message):
        for filters,fut in self.handlers:
            if fut.cancelled():
                self.handlers.remove((filters,fut))
            elif filters(message):
                self.handlers.remove((filters,fut))
                fut.set_result(message)
                return True
        return False
    def send_message(self,*args, **kwargs):
        msg = self.client.send_message(self.peer, *args, **kwargs)
        self.last_sent_id = msg.message_id
        return msg
    def get_response(self,filters=Filters.create('empty',lambda *_:True)):
        for msg in self.msgs:
            if msg.message_id < self.last_sent_id:
                self.msgs.remove(msg)
            elif filters(msg):
                fut = AwaitableFuture()
                fut.set_result(msg)
                self.messages.remove()
                return fut
        return self.add_awaiter(filters)
    async def __aenter__(self):
        return self.__enter__()
    def __enter__(self):
        self.client.add_handler(self.message_handler, -1)
        return self
    async def __aexit__(self):
        self.__exit__()
    def __exit__(self, *args):
        self.client.remove_handler(self.message_handler, -1)

class AwaitableClient(Client):
    def conversation(self, peer):
        return Conversation(self, peer)
import dotenv
from pyrogram.errors import UserIsBlocked, FloodWait, FileIdInvalid, UsernameNotOccupied, MessageEmpty
from pyrogram import __version__ as Version
class ProgramKilled(Exception):
    pass
def signal_handler(signum, frame):
    raise ProgramKilled
    
class Job(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs
        
    def stop(self):
                self.stopped.set()
                self.join()
    def run(self):
            while not self.stopped.wait(self.interval.total_seconds()):
                self.execute(*self.args, **self.kwargs)
            

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)
def run_async(func):
	
	from threading import Thread
	from functools import wraps

	@wraps(func)
	def async_func(*args, **kwargs):
		func_hl = Thread(target = func, args = args, kwargs = kwargs)
		func_hl.start()
		return func_hl

	return async_func

logging.getLogger("pyrogram").setLevel(logging.WARN)
LOGS = logging.getLogger(__name__)
import re
def ck(s):
    return re.match(r"[-+]?\d+$", s) is not None
# Check for Python 3.6 or newer
if sys.version_info[0] < 3 or sys.version_info[1] < 5:
    LOGS.error("You MUST use at least Python 3.6. Bot Quitting")
    quit(1)

# Now for the rest
__version__ = '0.4.1'
__author__  = 'Bfasbot Ultra'
__source__      = 'https://github.com/Bfas237/pyrobot'
__copyright__   = 'Copyright (c) 2019 ' + __author__
__copystring__  = "BfasBot v{} | {}".format(__version__, __copyright__)
__python_version__ = "Python v{}".format(str(sys.version_info[0])+"."+str(sys.version_info[1]))
__pyrogram__ = "Pyrogram v{}".format(Version)
cmds = ["#","!","."]
# Load our .env file
dotenv.load_dotenv()

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

import pickle
with open('wel', 'wb') as f:
  pickle.dump({}, f)
with open('warn', 'wb') as f:
   pickle.dump({}, f)
with open('plugins', 'wb') as f:
   pickle.dump({}, f)
                 
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

