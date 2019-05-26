
import pickle, sys, asyncio
from bfasbot import BOT, LOGS, ck, cmds

from time import mktime
from pyrogram.errors import (UserIsBlocked, FloodWait, FileIdInvalid, BadRequest, Flood, InternalServerError, SeeOther, Unauthorized, UnknownError, MessageNotModified, UsernameNotOccupied, MessageEmpty, UserAdminInvalid, ChatAdminRequired, PeerIdInvalid)
spamcount = 0
spamlimit = 3
sleeptime = 0
spamtime = 0
spamwait = 10
wait = 0
style_chats = {}
help_message = ''
from time import sleep, time

from bfasbot import BOT
from pyrogram import Filters, Message
from pyrogram.errors import UserAdminInvalid, FloodWait

from ..interval import IntervalHelper
from ..helpers import LogMessage

# -- Constants -- #
def exception_hook(exc_type, exc_value, exc_traceback):
    logging.error(
        "BFASBOT - Uncaught exception",
        exc_info=(exc_type, exc_value, exc_traceback)
    )  
 
sys.excepthook = exception_hook

def error_handler(bot, update, e):
        try:
            raise e
            LOGS.warning('Update "%s" caused error "%s"', update, e)
            
        except UnknownError:
            pass
        # remove update.message.chat_id from conversation list
        except BadRequest:
            pass
        # handle malformed requests - read more below!
        except Flood:
            pass
        
        except ChatAdminRequired:
          pass
          
        except FileIdInvalid:
            pass
          
        except UserIsBlocked:
            pass
          
        except UserAdminInvalid:
            pass
          
        except UserIsBlocked:
            pass
          
        except FloodWait:
            pass
        # handle slow connection problems
        except Unauthorized:
            pass
        # handle other connection problems
        except SeeOther:
            pass
        # the chat_id of a group has changed, use e.new_chat_id instead
        except InternalServerError:
            pass
          
        except PeerIdInvalid:
          pass
        # handle all other telegram related errors

admin = 'administrator'
creator = 'creator'
ranks = [admin, creator]

BANNED = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been banned.")
BANNED_TIME = (
    "{0.reply_to_message.from_user.first_name} has been banned for {1}.")
BANNED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been banned from \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\".")

UNBANNED = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been unbanned")
UNBANNED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id="
    "{0.reply_to_message.from_user.id}) has been unbanned in \"["
    "{0.chat.title}](t.me/c/{1}/{0.message_id})\".")

MUTED = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been muted.")
MUTED_TIME = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been muted for {1}")
MUTED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been muted in \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\".")

UNMUTED = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been unmuted.")
UNMUTED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been unmuted in \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\".")

KICKED = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been kicked.")
KICKED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been kicked from \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\".")

# -- Constants End -- #

# -- Helpers -- #


async def ReplyCheck(message):
    if not message.reply_to_message:
        await message.edit("`{}` needs to be a reply.".format(message.command[0]))
        sleep(2)
        await message.delete()
    elif message.reply_to_message.from_user.is_self:
        await message.edit("I can't {} myself.".format(message.command[0]))
        sleep(2)
        await message.delete()
    else:
        return True


async def AdminCheck(message):
    SELF = BOT.get_chat_member(
        chat_id=message.chat.id,
        user_id=message.from_user.id)

    if SELF.status not in ranks:
        await message.edit("__I'm not Admin!__")
        sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin:
            return True
        elif SELF.permissions.can_restrict_members:
            return True
        else:
            await message.edit("__No permissions to restrict Members__")


async def RestrictFailed(message):
    await message.edit("I can't {} this user.".format(message.command[0]))
    sleep(2)
    await message.delete()


def Timer(message: Message):
    if len(message.command) > 1:
        secs = IntervalHelper(message.command[1])
        return int(str(time()).split(".")[0]) + secs.to_secs()[0]
    else:
        return 0


def TimerString(message: Message):
    secs = IntervalHelper(message.command[1])
    return "{} {}".format(secs.to_secs()[1], secs.to_secs()[2])

# -- Helpers End -- #


@BOT.on_message(Filters.command("ban", "?") & Filters.me)
async def ban_hammer(bot: BOT, message: Message):
    if ReplyCheck(message) is True and AdminCheck(message) is True:
        try:
            await BOT.kick_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                until_date=Timer(message))
            if len(message.command) > 1:
                await message.edit(BANNED_TIME.format(
                    message,
                    TimerString(message)))
            else:
                await message.edit(BANNED.format(message))
            await LogMessage(BANNED_LOG.format(
                message,
                str(message.chat.id).replace("-100", "")))
        except UserAdminInvalid:
            await RestrictFailed(message)


@BOT.on_message(Filters.command("unban", "?") & Filters.me)
async def unban(bot: BOT, message: Message):
    if ReplyCheck(message) is True and AdminCheck(message) is True:
        try:
            await BOT.unban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id)
            await message.edit(UNBANNED.format(message))
            await LogMessage(UNBANNED_LOG.format(
                message,
                str(message.chat.id).replace("-100", "")))
        except UserAdminInvalid:
            await message.edit("I can't unban this user")


@BOT.on_message(Filters.command("mute", "?") & Filters.me)
async def mute_hammer(bot: BOT, message: Message):
    if ReplyCheck(message) is True and AdminCheck(message) is True:
        try:
            await BOT.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                until_date=Timer(message),
                can_send_messages=False,)
            if len(message.command) > 1:
                await message.edit(MUTED_TIME.format(
                    message,
                    TimerString(message)))
            else:
                await message.edit(MUTED.format(message))
            await LogMessage(MUTED_LOG.format(
                message,
                str(message.chat.id).replace("-100", "")))
        except UserAdminInvalid:
            await RestrictFailed(message)


@BOT.on_message(Filters.command("unmute", "?") & Filters.me)
def unmute(bot: BOT, message: Message):
    if ReplyCheck(message) is True and AdminCheck(message) is True:
        try:
            BOT.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                until_date=0,
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
                can_send_polls=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True)
            message.edit(UNMUTED.format(message))
            LogMessage(UNMUTED_LOG.format(
                message,
                str(message.chat.id).replace("-100", "")))
        except UserAdminInvalid:
            RestrictFailed(message)


@BOT.on_message(Filters.command("kick", "?") & Filters.me)
def kick_user(bot: BOT, message: Message):
    if ReplyCheck(message) is True and AdminCheck(message) is True:
        try:
            BOT.kick_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                until_date=0)
            BOT.unban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id)
            message.edit(KICKED.format(message))
            LogMessage(KICKED_LOG.format(
                message,
                str(message.chat.id).replace("-100", "")))
        except UserAdminInvalid:
            RestrictFailed(message)


@BOT.on_message(Filters.command("cclean", "!") & Filters.me)
def clean_deleted(bot: BOT, message: Message):
    if AdminCheck(message) is True:
        message.edit("`Iterating through memberlist...`")
        all_members = BOT.iter_chat_members(message.chat.id)
        to_remove = []
        removed = []

        for member in all_members:
            if member.user.is_deleted:
                to_remove.append(member.user.id)

        message.edit("`{} deleted accounts found.`".format(len(to_remove)))

        for usr in to_remove:
            try:
                BOT.kick_chat_member(
                    chat_id=message.chat.id,
                    user_id=usr)
                removed.append(usr)
            except UserAdminInvalid:
                pass
            except FloodWait as e:
                sleep(e.x)

        message.edit("Removed {} deleted accounts.".format(len(to_remove)))


@BOT.on_message(Filters.command("mod", "?") & Filters.me)
def unmute(bot: BOT, message: Message):
    if CheckReplyAdmin(message) is True:
        if CheckAdmin(message) is True:
            try:
                BOT.promote_chat_member(
                    chat_id = message.chat.id,
                    user_id = message.reply_to_message.from_user.id,
                    can_edit_messages = True,
                    can_delete_messages = True,
                    can_restrict_members = True,
                    can_invite_users = True
                )
                message.edit(Admin.PROMOTED.format(
                    message.reply_to_message.from_user.first_name))
                LogMessage(Admin.PROMOTED_LOG.format(
                    message.reply_to_message.from_user.first_name,
                    message.reply_to_message.from_user.id,
                    message.chat.title,
                    str(message.chat.id).replace("-100", ""),
                    str(message.message_id)))

            except UserAdminInvalid:
                RestrictFailed(message)

            except ChatAdminRequired:
                RestrictFailed(message)

                                


@BOT.on_message(Filters.command("unmod", "?") & Filters.me)
def unmute(bot: BOT, message: Message):
    if CheckAdmin(message) is True:
            from_user=""
            cmd = " ".join(message.command[1:])
            
            if cmd:
              if ck(cmd):
                from_user = BOT.resolve_peer(cmd).user_id
              else:
                  from_user = BOT.get_users(cmd)
              print(from_user)
            else:
              from_user = message.reply_to_message
            rep = message.reply_to_message
            try:
                BOT.promote_chat_member(
                    chat_id = message.chat.id,
                    user_id = from_user.id,
                    can_edit_messages = False,
                    can_delete_messages = False,
                    can_restrict_members = False,
                    can_invite_users = False,
                    can_promote_members = False,
                    can_pin_messages = False,
                    can_change_info = False
                  
                  
                )
                message.edit(Admin.UNPROMOTED.format(
                    rep.from_user.first_name if rep else from_user.first_name))
                LogMessage(Admin.UNPROMOTED_LOG.format(
                    rep.from_user.first_name if rep else from_user.first_name,
                    rep.from_user.id if rep else from_user.id,
                    message.chat.title,
                    str(message.chat.id).replace("-100", ""),
                    str(message.message_id)))

            except UserAdminInvalid:
                RestrictFailed(message)

            except ChatAdminRequired:
                RestrictFailed(message)

                
                
@BOT.on_message(Filters.me & Filters.command('rwarn', cmds))
def warn(client, message):
    with open('warn', 'rb') as f:
        warnings = pickle.load(f)
    if sleeptime < time():
        rpl_user = message.reply_to_message.from_user
        if message.chat.id in warnings:
            if message.reply_to_message.from_user.id in warnings[message.chat.id]:
                warnings[message.chat.id][message.reply_to_message.from_user.id] += 1
            else:
                warnings[message.chat.id][message.reply_to_message.from_user.id] = 1
        else:
            warnings[message.chat.id] = {message.reply_to_message.from_user.id: 1}
        with open('warn', 'wb') as f:
            pickle.dump(warnings, f)
        warns = warnings[message.chat.id][message.reply_to_message.from_user.id]
        if warns == 2:
            now = datetime.now()
            until = datetime(now.year, now.month, now.day, now.hour + 1)
            client.restrict_chat_member(message.chat.id,
                                        rpl_user.id,
                                        until_date=int(mktime(until.timetuple()) + 1e-6 * until.microsecond),
                                        can_send_messages=False,
                                        can_change_info=False,
                                        can_invite_users=False,
                                        can_pin_messages=False)
        elif warnings[message.chat.id][message.reply_to_message.from_user.id] == 3:
            client.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            client.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            message.reply('[{}]({}) is #kicked for {}'.format(message.reply_to_message.from_user.first_name,
                                                              'tg://user?id={}'.format(
                                                                  message.reply_to_message.from_user.id),
                                                              'Having 3 Warns'))
        message.edit('[{}]({}) is #warned for {} `{}`'.format(message.reply_to_message.from_user.first_name,
                                                              'tg://user?id={}'.format(
                                                                  message.reply_to_message.from_user.id),
                                                              " ".join(message.command[1:]),
                                                              warnings[message.chat.id][
                                                                  message.reply_to_message.from_user.id]))


    
    

@BOT.on_message(Filters.me & Filters.command('nowarn', '?'))
def warn(client, message):
    with open('warn', 'rb') as f:
        warnings = pickle.load(f)
    rpl_user = message.reply_to_message.from_user
    
    
    if message.chat.id in warnings:
        if message.reply_to_message.from_user.id in warnings[message.chat.id]:
            warnings[message.chat.id][message.reply_to_message.from_user.id] += 1
        else:
            warnings[message.chat.id][message.reply_to_message.from_user.id] = 1
    else:
        warnings[message.chat.id] = {message.reply_to_message.from_user.id: 1}
    with open('warn', 'wb') as f:
        pickle.dump(warnings, f)
    warns = warnings[message.chat.id][message.reply_to_message.from_user.id]

    message.reply(warns)