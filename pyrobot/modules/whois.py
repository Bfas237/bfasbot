from time import sleep
from pyrogram.api import functions
from pyrogram import Filters, Message
from pyrobot import BOT
from pyrobot import cmds
import shutil, os, shutil
from ..constants import WhoIs
from ..helpers import LastOnline, GetCommon
from pyrogram.api import functions
cmd = ["whois","who"]

@BOT.on_message(Filters.command("hhh", ".") & Filters.me)
def who_is(bot: BOT, message: Message):
    cmd = message.command
    if not len(cmd) > 1 and not message.reply_to_message:
        message.edit("I can't check __nobody__")
        sleep(2)
        message.delete()
    else:
        if message.reply_to_message:
            get_user = message.reply_to_message.from_user
        else:
            get_user = BOT.get_chat(" ".join(message.command[1:]))
            try:
                get_user = int(get_user.id)
            except ValueError:
                pass
        print(BOT.get_users(get_user)) 
            
        message.edit("ok its good") 
@BOT.on_message(Filters.command(cmd, cmds))
def who(client, message):
    cmd = message.command
    if not len(cmd) > 1 and not message.reply_to_message:
        message.edit("I can't check __nobody__")
        sleep(5)
        message.delete()
        return
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        full_name = user.first_name + " " + user.last_name if user.last_name else user.first_name
    else:
        chat = client.get_chat(" ".join(message.command[1:]))
        print(chat)
        user = client.get_users(chat.id)
        
        full_name = user.first_name + " " + user.last_name if user.last_name else user.first_name
    
    
    common = GetCommon(user.id)
    text = WhoIs.WHOIS_PIC.format(full_name, user.id,
                                       user.first_name,
                                       user.last_name,
                                       "😂😂😂" if user.id == 197005208 else user.username,
                                       LastOnline(user) if user.status else 'None',
                                       client.get_user_profile_photos(user.id).total_count,
                                       len(common.chats),
                                       client.get_chat(user.id).description)

    fo = message.edit('`sending #whois`')
    
    try:
        pic = client.download_media(user.photo.big_file_id)
        client.send_photo(message.chat.id,
                          pic,
                          caption=text,
                          parse_mode='markdown')
        fo.delete()
        os.remove(pic)
        try:
          os.unlink(pic)
        except FileNotFoundError:
          pass
    except AttributeError:
        message.edit(text, parse_mode='markdown')
        shutil.rmtree("downloads")