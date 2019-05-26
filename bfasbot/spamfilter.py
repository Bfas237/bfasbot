from bfasbot import BOT, LOGS, cmds
from pyrogram import Client, Filters
from collections import deque
from functools import wraps
from difflib import SequenceMatcher
from bfasbot.helpers import LogMessage, ReplyCheck
import logging, urllib, os, re, sys, sqlite3, json, io, requests, requests, shutil, traceback, os.path, urllib.request, time, fnmatch, glob, asyncio, async_timeout, aiohttp, aiofiles
def restricted(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.from_user.id
        user = is_admin(user_id)
        LOGS.warning("%s has been authorized", user_id) 
        return func(bot, update, *args, **kwargs)
    return wrapped
 
import time   
class SpamFilter:
    def __init__(self):
        self.limits = {3:2, 8:7, 16:15} # max: 3 updates in 1 second, 7 updates in 5 seconds, 10 updates in 10 seconds
        self.timeout_start = 5
        self.severity = 10
        self.timeouts = {}
        self.times = {}
        self.violations = {}
    async def new_message(self, chat_id, from_user):
        update_time = time.time() 
        if chat_id not in self.timeouts:
            self.timeouts.update({chat_id: 0})
            self.times.update({chat_id : deque(maxlen=3)})
            self.violations.update({chat_id: 0})
        else:
            if self.timeouts[chat_id] > update_time:
                return 1
            for limit in self.limits:
                amount = 1
                for upd_time in self.times[chat_id]:
                    if update_time - upd_time < limit:
                        amount += 1
                    else:
                        break
                if amount > self.limits[limit]:
                    delta = int(self.timeout_start * self.severity ** self.violations[chat_id])
                    self.timeouts[chat_id] = update_time + delta
                    self.violations[chat_id] += 1
                    LOGS.warning("User %s - %s is sending too many requests, broke %s limit", from_user, chat_id, limit)
                    
                    await LogMessage("[{}](tg://user?id={}) is sending too many requests, broke `{}` limit".format(from_user, chat_id, limit)
            )
                    
                    return await "⚠️ **Warning**:. [{0}](tg://user?id={1}), You are **Flooding**. Try again in `{2}` Seconds. \n\nWhile your account is muted, i won't be able to see your mesages.".format(from_user, chat_id, delta) 
        self.times[chat_id].appendleft(update_time)
        return False


    async def wrapper(self, func):  # only works on functions, not on instancemethods
        # Only works for messages (+Commands) and callback_queries (Inline Buttons)
        async def func_wrapper(bot, update):
            if update:
                chat_id = update.from_user.id
                timeout = await self.new_message(chat_id, update.from_user.first_name)
            if not timeout:
                return await func(bot, update) # return is required by ConversationHandler
            elif timeout != 1:
                await bot.send_chat_action(chat_id,'TYPING')
                await bot.send_message(update.chat.id, timeout, parse_mode="Markdown")
        return await func_wrapper
