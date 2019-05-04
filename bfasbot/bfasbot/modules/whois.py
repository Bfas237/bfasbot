from time import sleep
from pyrogram.api import functions
from pyrogram import Filters, Message
from bfasbot import BOT, cmds
import shutil, os, shutil
from ..constants import WhoIs
from ..helpers import LastOnline, GetCommon
from pyrogram.api import functions
cmd = ["whois","who"]
import time, img2pdf, inflect, os
p = inflect.engine()
from ..constants import WhoIs
from ..helpers import LastOnline, GetCommon, FullName, ReplyCheck, ProfilePicUpdate

@BOT.on_message(Filters.command("me", ".") & Filters.me)
def who_is(bot: BOT, message: Message):
    cmd = message.command
    if not message.reply_to_message and len(cmd) is 1:
        get_user = message.from_user.id
    elif message.reply_to_message and len(cmd) is 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    user = BOT.get_users(get_user)
    fdesc = BOT.get_users(get_user)
    print(fdesc)
    desc = BOT.get_chat(get_user).description
    user_pic = BOT.get_user_profile_photos(user.id)
    common = GetCommon(user.id)

    if not user.photo:
        message.edit(
            WhoIs.WHOIS.format(
                full_name = FullName(user),
                user_id = user.id,
                first_name = user.first_name if user.first_name else "",
                last_name = user.last_name if user.last_name else "",
                username = user.username if user.username else "",
                last_online = LastOnline(user),
                common_groups = len(common.chats),
                bio = desc if desc else "`No bio set up.`"),
            disable_web_page_preview = True)
    elif user.photo:
        BOT.send_photo(
            message.chat.id,
            user_pic.photos[0].sizes[-1].file_id,
            WhoIs.WHOIS_PIC.format(
                full_name = FullName(user),
                user_id = user.id,
                first_name = user.first_name,
                last_name = user.last_name if user.last_name else "",
                username = user.username if user.username else "",
                last_online = LastOnline(user),
                profile_pics = p.plural("**Profile Picture**", user_pic.total_count)+": "+ "`{}`".format(str(user_pic.total_count)),
                common_groups = "**Common Group:** " + "`{}`".format(str(len(common.chats))) if len(common.chats) <=1 else "**Common Groups:** "+ "`{}`".format(str(len(common.chats))),
              
                bio = desc if desc else "`No bio set up.`",
                profile_pic_update = ProfilePicUpdate(user_pic)),
            reply_to_message_id = ReplyCheck(message)
        )
        message.delete()
        
        
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