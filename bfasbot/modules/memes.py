import requests, re

from bfasbot import BOT
from pyrogram import Filters, Message

from ..helpers import ReplyCheck

DOG = r"([^.]*)$"
ok_exts = ["jpg", "jpeg", "png"]

def _get_dog():
    content = requests.get('https://random.dog/woof.json')
    return content.json()['url']

def _prep_dog():
    ext = ''
    while ext not in ok_exts:
        dog_pic = _get_dog()
        ext = re.search(DOG, dog_pic).group(1).lower()
    return dog_pic

@BOT.on_message(Filters.command(["🐶", "🐕", "🐩", "dog"], "") & Filters.me)
def _send_dog(bot: BOT, message: Message):
    BOT.send_photo(
        chat_id = message.chat.id,
        photo = _prep_dog(),
        caption = "doggo",
        reply_to_message_id = ReplyCheck(message)
    )
    if message.from_user.is_self:
        message.delete()
