import sys, pickle
import importlib
import time, datetime, os, re, sys, sqlite3, json, io 
from pyrobot import __copystring__, __version__, __python_version__
from pyrobot import BOT, LOGS
from pyrobot.modules import ALL_MODULES
import sqlite3 as lite
 
from datetime import date, datetime
for module_name in ALL_MODULES:
    imported_module = importlib.import_module("pyrobot.modules." + module_name)
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
 

import pickle
with open('trigger', 'wb') as f:
    pickle.dump({}, f)
with open('correction', 'wb') as f:
    pickle.dump({}, f)
with open('welcome', 'wb') as f:
   pickle.dump({}, f)
with open('warn', 'wb') as f:
    pickle.dump({}, f)

def delid(fid): 
  with sqlite3.connect('userbot.db', check_same_thread=False) as conn:
    c = conn.cursor()
    c.execute("DELETE FROM Users WHERE COUNT_MSG= (?) AND UserID= (?)", (1, fid, ))
    row = c.fetchone()
    if row is None:
      news = 0
      valid = c.rowcount
    else: 
      news = row[3]
      valid = c.rowcount
    conn.commit()
    return[news, valid]
class DBHelper:
       def __init__(self, dbname="userbot.db"):
            self.dbname = dbname
            self.conn = sqlite3.connect(dbname, check_same_thread=False)
            self.c = self.conn.cursor()
            self.setup()
    
       
       def __enter__(self):
       
            return self
       
       def setup(self):
            self.conn.text_factory = str
            self.c.executescript('''CREATE TABLE IF NOT EXISTS Users
    (
    id INTEGER NOT NULL PRIMARY KEY UNIQUE, 
    ChatID INTEGER, 
    LastMsg INTEGER,
    UserID TEXT,
    Previous TEXT,
    Welcome TEXT,
    ISAFK INTEGER DEFAULT 1, 
    COUNT_PM INTEGER,
    AFKREASON TEXT DEFAULT "No Reason",
    SPAM_CHAT_ID TEXT,
    COUNT_MSG INTEGER);''' 
    )
            #self.c.executescript('''DROP TABLE IF EXISTS Users;''') 
            self.conn.commit()
       def __exit__(self, exc_class, exc, traceback):
        
            self.conn.commit()
        
            self.conn.close()

db = DBHelper()
"""
with sqlite3.connect('userbot.db', check_same_thread=False) as conn:
    cur = conn.cursor()
    cur = conn.execute('''SELECT ISAFK,COUNT_PM, AFKREASON, COUNT_MSG FROM Users''')  
    row = cur.fetchone()
    count = 0 
    if row is None:
        cur.execute('''INSERT INTO Users (ISAFK,COUNT_PM, AFKREASON, COUNT_MSG) VALUES ( ?, ?, ?, ? )''', (1, 0, "No Reason", 0 ))
        count += 1 
    conn.commit() 

    print ("Total news written to database : ", count, row)  """

if len(sys.argv) not in (1, 3, 4):
    quit(1)
else:
    BOT.start()
    print(__copystring__)
    LOGS.info("Your bot is running! Test it by typing .alive in any chat.")
    LOGS.info("Your bot is Version {}\n".format(__version__))
    
if __name__ == "__main__":
  BOT.idle()
