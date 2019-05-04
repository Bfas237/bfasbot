from datetime import datetime

from pyrogram import Filters, Message
from bfasbot import BOT, LOGS, START_TIME, cmds, ascii, asc, LOAD
from os.path import splitext
from ..constants import MiscStrings, Comp
import time, img2pdf, inflect, os
p = inflect.engine()
from os.path import dirname, basename, isfile
import glob
def pdf():
  # Get a list of all the file paths that ends with .txt from in specified directory
  fileList = glob.glob('/app/*.pdf')
  for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath) 

def jpg():
  # Get a list of all the file paths that ends with .txt from in specified directory
  fileList = glob.glob('/app/*.jpg')
  for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath) 
def png():
  # Get a list of all the file paths that ends with .txt from in specified directory
  fileList = glob.glob('/app/*.png')
  for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath) 
#print("Did you want ", p.a(p.plural("boy")), " or ", p.an("idea"))
#print("There", p.num(2,''), p.plural_verb("was"), p.no(" error"))
# Edit the sent message to display the current uptime.


@BOT.on_message(Filters.command(["asc"], "."))
def get_link(bot, update):
    
    if update.reply_to_message is not None:
        reply_message = update.reply_to_message
        start = datetime.now()
        a = bot.send_message(
            chat_id=update.chat.id,
            text="Sending Ascii image...",
            reply_to_message_id=update.message_id
        )
        c_time = time.time()
        after_download_file_name = bot.download_media(
            message=reply_message,
        )
        download_extension = splitext(after_download_file_name[15:])
        
        with open("temp","wb") as f:
          #f.write(img2pdf.convert(after_download_file_name))
          #update.reply_document(download_extension[0]+".pdf")
          run = ascii.runner(after_download_file_name)
          
          asc.main(run)
          update.reply_photo("img.png")
          #png()
          #jpg()
          #pdf()
          os.remove(after_download_file_name)

# Edit the sent message to display the current uptime.
@BOT.on_message(Filters.command(["learn","py"], ".") & Filters.me)
def learn(bot: BOT, message: Message):
  
  
    f1 = "(https://wiki.python.org/moin/BeginnersGuide/NonProgrammers)"
    f2 = "(https://wiki.python.org/moin/BeginnersGuide/Programmers)"
    f3 = "(https://docs.python.org/3/tutorial/)"
    f4 = "(http://www.diveintopython3.net/)"
    f5 = "(https://www.learnpython.org/)"
    f6 = "(https://cscircles.cemc.uwaterloo.ca/)"
    f7 = "(https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)"
    f8 = "(https://docs.python-guide.org/)"

    f9 = "(https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7)"
    f10 = "(https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)"
    f11 = "(http://projectpython.net/chapter00/)"
    message.edit(Comp.HELP.format(f1,f2, f3, f4,f5,f6,f7,f8,f9,f10,f11))
    
    
@BOT.on_message(Filters.command("r", cmds))
def replace(client, message):
    text = " ".join(message.command[1:])
    fr, to = text.split('.')
    result = "**You mean:**\n{}".format(message.reply_to_message.text.replace(fr, to))
    message.edit(result)

  
@BOT.on_message(Filters.command("i", cmds))
def replace(client, message):
    text = " ".join(message.command[1:])
    fr, to = text.split('.')
    result = "**I meant:**\n{}".format(message.reply_to_message.text.replace(fr, to))
    message.edit(result)



