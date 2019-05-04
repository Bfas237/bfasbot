from bfasbot import BOT as app
from pyrogram import Filters, Message

prefixes = '.:!'
@app.on_message((Filters.me | Filters.channel) & Filters.command('del', prefixes))
def purge_msgs(client, message):

    # if cmd has an int argument
    if len(message.command) > 1 and message.command[1].isdigit():
        n = int(message.command[1])
        if message.reply_to_message:
            message.delete()
            msgs = client.get_history(
                message.chat.id,
                limit=n,
                offset_id=message.reply_to_message.message_id,
                reverse=True) # this reverse gets messages after offset_id, rather than before it
            msgs = reversed(msgs.messages) # this reverses the order of the messages to delete

        else: # if cmd has int, but is not a reply
            msgs = client.get_history(message.chat.id, limit=n+1).messages

    else: # if cmd doesn't have an int
        if not message.reply_to_message:
            return

        # if it is a reply
        msgs = reversed(list(client.iter_history(
            message.chat.id,
            offset_id=message.reply_to_message.message_id,
            reverse=True)))

    # finally
    for msg in msgs:
        msg.delete()