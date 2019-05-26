from pyrogram import Client, Filters
from bfasbot import BOT, LOGS, cmds
from time import sleep, time
from pyrogram.api import functions
sleeptime = 0
import shutil

@BOT.on_message(Filters.command('name', cmds) & Filters.me)
async def set_name(client, message):
    if sleeptime < time():
        await client.send(functions.account.UpdateProfile(first_name=' '.join(message.command[1:])))
        await message.edit('`Name changed succesfully`')
        sleep(3)
        await message.delete()


@BOT.on_message(Filters.command('bio', cmds) & Filters.me)
async def set_bio(client, msg):
    if sleeptime < time():
        bio = ' '.join(msg.command[1:])
        if len(bio) > 70:
            await  msg.edit('`Bio too long maximum 70 characters`')
            sleep(3)
            await msg.delete()
        else:
            await  client.send(functions.account.UpdateProfile(about=bio))
            await  msg.edit('`Bio succesfully changed`'.format(bio))
            sleep(3)
            await msg.delete()


@BOT.on_message(Filters.regex('^#pic') & Filters.me)
async def set_profile_pic(client, msg):
    if sleeptime < time():
        if msg.reply_to_message:
            pic = await msg.reply_to_message.download()
        else:
            pic = await msg.download()
        await client.set_user_profile_photo(pic)
        await msg.edit('`profile picture set succesfully`')
        try:
          os.remove(pic)
        except Exception: 
          shutil.rmtree("downloads")
          pass
        await msg.delete()
 
@BOT.on_message(Filters.me & Filters.regex('^#last'))
async def onecharacter(client, msg):
    if sleeptime < time():
      await client.send(functions.account.UpdateProfile(last_name=' '.join(msg.command[1:])))
      await  msg.edit('`Last name set succesfully`')
      sleep(3)
      await msg.delete()

@BOT.on_message(Filters.me & Filters.command('chat', cmds))
async def getchat(client, message):
    if len(message.command) >= 2:
        chat = await client.get_chat(message.command[1])
    else:
        chat = await client.get_chat(message.chat.id)
    text = '''**{}**\n\n
`Pinned Message:` [{}](t.me/c/{}/{})
`Members:` {}
`id`: {}
`type`: {}
`Description:` 
{}'''
    texttoolong = '''**{}**
    `Pinned Message:` [{}](t.me/c/{}/{})
    `Members:` {}
    `id`: {}
    `type`: {}'''
    try:
        try:
            pic = await client.download_media(chat.photo.big_file_id)
            await  client.send_photo(message.chat.id,
                              pic,
                              text.format(chat.title,
                                          (chat.pinned_message.text if chat.pinned_message.text and len(chat.pinned_message.text) < 100 else 'View Here') if chat.pinned_message else 'None',
                                          str(chat.id).replace('-100', ''),
                                          chat.pinned_message.message_id if chat.pinned_message else message.message_id,
                                          chat.members_count,
                                          chat.id,
                                          chat.type,
                                          chat.description))
            await message.delete()
        except MediaCaptionTooLong:
            img = await client.send_photo(message.message.chat.id, pic)
            msg = await img.reply(texttoolong.format(chat.title,
                                  (chat.pinned_message.text if chat.pinned_message.text and len(chat.pinned_message.text) < 100 else 'View Here') if chat.pinned_message else 'None',
                                  str(chat.id).replace('-100', ''),
                                  chat.pinned_message.message_id if chat.pinned_message else message.message_id,
                                  chat.members_count,
                                  chat.id,
                                  chat.type))
            await msg.reply('`Descripion:`\n{}'.format(chat.description))

    except AttributeError:
        try:
            await message.edit(text.format(chat.title,
                                          (chat.pinned_message.text if chat.pinned_message.text and len(chat.pinned_message.text) < 100 else 'View Here') if chat.pinned_message else 'None',
                                          str(chat.id).replace('-100', ''),
                                          chat.pinned_message.message_id if chat.pinned_message else message.message_id,
                                          chat.members_count,
                                          chat.id,
                                          chat.type,
                                          chat.description))
        except MessageTooLong:
            await message.edit(texttoolong.format(chat.title,
                                          (chat.pinned_message.text if chat.pinned_message.text and len(chat.pinned_message.text) < 100 else 'View Here') if chat.pinned_message else 'None',
                                          str(chat.id).replace('-100', ''),
                                          chat.pinned_message.message_id if chat.pinned_message else message.message_id,
                                          chat.members_count,
                                          chat.id,
                                          chat.type))
            await message.reply('`Description:`\n{}'.format(chat.description))

 