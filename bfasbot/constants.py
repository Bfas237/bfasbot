
    
    
class rog:
    ###
    #
    # Pyrogram inn
    #
    ###
    PYRO =  (
      "╔═════\n"
      "║🔥 Welcome to **Pyrogram's community!**\n"
      "╠═════\n"
      "║Before asking further questions and going off\n" \
      "║ the line kindly check use one or more of these\n" \
      "║ links to help yourself out\n" \
      "╠═════\n"
      "║📜 [Global Rules](http://t.me/PyrogramChat/51110)\n"
      "╠═════\n"
      "║🌐 [Community Groups](http://t.me/PyrogramChat/44625)\n"
      "╠═════\n"
      "║📖 [Docs & How To's](http://docs.pyrogram.ml)\n"
      "╠═════\n"
      "║🗂 [GitHub Repo & Examples](http://github.com/pyrogram)\n"
      "╠═════\n"
      "║🎉 [0ff_topic & Python Talks](http://t.me/PyrogramLounge)\n"
      "╠═════\n"
      "║📢 [News & Updates Channel](http://t.me/Pyrogram)\n" 
      "╚═════\n"
    )  

class First:
    ###
    #
    # 1start.py
    #
    ###
    ALIVE = (
        "╔═════\n"
        "║ **\U0001F916 BOT STATUS:**  {}\n"
        "╠═════\n"
        "║**Library:**   `{}` \n"
        "╠\n"
        "║**System Info:**   `{}` \n"
        "╠\n"
        "║**Maintenance Mode:**   `{}`\n"
        "╠\n"
        "║**Bot Version:**   `{}`\n"
        "╠\n"
        "║**Last Reboot:**   `{}`\n"
        "╠\n"
        "║**Current Uptime:**   `{}`\n"
        "╠\n"
        "║**Github Repo:**   [{}]({})\n"
        "╠═════\n"
    )
    SLEEP = (
        "╔═════\n"
        "║ **\U0001F916 BOT STATUS:**  {}\n"
        "╠═════\n"
        "║**Maintenance Mode:**   `{}`\n"
        "╠\n"
        "║**Last Reboot:**   `{}`\n"
        "╠\n"
        "║**Current Uptime:**   `{}`\n"
        "╠═════\n"
    )

    HELP_TEXT = (
        "[\u200b](https://git.colinshark.de/PyroBot/PyroBot/src/branch/master"
        "/HELP.md)\n"
        "**Short Overview - PyroBot\U0001f525\U0001F916**\n"
        "This Userbot is made with [Pyrogram]"
        "(https://github.com/Pyrogram/Pyrogram).\n"
        "It runs on [Python 3.6](https://python.org) and above.\n\n"

        "All Commands are listed [here](https://git.colinshark.de/PyroBot/"
        "PyroBot/src/branch/master/HELP.md)"
    )


class Admin:
    ###
    #
    # admin.py
    #
    ###
    BANNED = "{0.reply_to_message.from_user.first_name} has been banned."
    BANNED_TIME = (
    "{0.reply_to_message.from_user.first_name} has been banned for {1}.")
    BANNED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been banned from \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\".")

    UNBANNED = "{0.message.reply_to_message.from_user.first_name} has been unbanned"
    UNBANNED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id="
    "{0.reply_to_message.from_user.id}) has been unbanned in \"["
    "{0.chat.title}](t.me/c/{1}/{0.message_id})\".")

    MUTED = "{0.reply_to_message.from_user.first_name} has been muted."
    MUTED_TIME = "{0.reply_to_message.from_user.first_name} has been muted for {1}."
    MUTED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been muted in \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\".")

    UNMUTED = "{0.reply_to_message.from_user.first_name} has been unmuted."
    UNMUTED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been unmuted in \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\".")

    KICKED = "{0.reply_to_message.from_user.first_name} has been kicked."
    KICKED_LOG = (
    "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been kicked from \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\".")


    PROMOTED = "{0.reply_to_message.from_user.first_name} has been promoted to **Moderator.**"
    PROMOTED_LOG = (
        "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    "has been Promoted to Moderator In \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\"."
    )
    UNPROMOTED = "{0.reply_to_message.from_user.first_name} is no longer a **Moderator.**"
    UNPROMOTED_LOG = (
        "[{0.reply_to_message.from_user.first_name}](tg://user?id={0.reply_to_message.from_user.id}) "
    " is no longer a **Moderator.** In \"[{0.chat.title}](t.me/c/{1}/{0.message_id})\"."
    )

class MiscStrings:
    ###
    #
    # misc.py
    #
    ###
    ASK = ("**Have a Question?**\n\n"
           "Don't ask to ask, just ask away :) You're more likely to get a response if you just ask the question, rather than asking if you can ask.")
    
    PASTE = ("Please use one of these to paste your code then send the link here so we can check whats wrong.:\n\n"
    "➡️ del.dog\n"
    "➡️ hastebin.com")

class Comp:
    
    HELP = ("Oh, hey! Check out These from the community of Python developers: ❤️ A Compiled list of learning resources just for you:\n\n"
            "• [As Beginner]{}\n"
            "• [As Programmer]{}\n"
            "• [Official Tutorial]{}\n"
            "• [Dive into Python ]{}\n"
            "• [Learn Python]{}"
            "• [Computer Science Circles]{}\n"
            "• [MIT OpenCourse]{}"
            "• [Hitchhiker’s Guide to Python]{}\n"
            "• The @PythonRes Telegram Channel\n"
            "• Corey Schafer videos for [beginners]{} and in [general]{}\n"
            "• [Project Python]{}\n"
            "")

class Eval:
    ###
    #
    # evaluation.py
    #
    ###
    RUNNING     = "**Expression:**\n```{}```\n\n**Running...**"
    ERROR       = "**Expression:**\n```{}```\n\n**Error:**\n```{}```"
    SUCCESS     = "**Expression:**\n```{}```\n\n**Success** | `None`"
    RESULT      = "**Expression:**\n```{}```\n\n**Result:**\n```{}```"
    RESULT_FILE = "**Expression:**\n```{}```\n\n**Result:**\nView `output.txt` below ⤵"

    ERROR_LOG   = (
        "**Evaluation Query**\n"
        "```{}```\n"
        "erred in chat \"[{}](t.me/c/{}/{})\" with error\n"
        "```{}```"
    )

    SUCCESS_LOG = (
        "Evaluation Query\n"
        "```{}```\n"
        "succeeded in \"[{}](t.me/c/{}/{})\""
    )

    RESULT_LOG  = (
        "Evaluation Query\n"
        "```{}```\n"
        "executed in chat \"[{}](t.me/c/{}/{})\"."
    )


class GetInfo:
    ###
    #
    # get_info.py
    #
    ###
    ADMINTITLE = "**Admins in \"{}\"**\n\n"
    ADMINCREATOR = (
        '╔ **Creator**\n'
        '╚ `{} `[{}](tg://user?id={})\n\n')
    ADMINLISTLASTBOT = '╚ `{} `[{}](tg://user?id={}) `ᴮᴼᵀ`\n'
    ADMINLISTLAST = '╚ `{} `[{}](tg://user?id={})\n'
    ADMINLISTBOT = '╠ `{} `[{}](tg://user?id={}) `ᴮᴼᵀ`\n'
    ADMINLIST = '╠ `{} `[{}](tg://user?id={})\n'

    MEMBER_INFO = (
        "╔═════════\n"
        "╠ **{}**\n"
        "╠ Member Count\n"
        "╠═════════\n"
        "╠ Total: `{}`\n"
        "╠═════════\n"
        "╠ Admins: `{}`\n"
        "╠ Members: `{}`\n"
        "╠ Bots: `{}`\n"
        "╠═════════\n"
        "╠ Deleted Accounts: `{}`\n"
        "╚═════════"
    )


class WhoIs:
    ###
    #
    # whois.py
    #
    ###
    WHOIS = (
        "**WHO IS \"{full_name}\"?**\n"
        "[Link to profile](tg://user?id={user_id})\n"
        "════════════════\n"
        "UserID: `{user_id}`\n"
        "First Name: `{first_name}`\n"
        "Last Name: `{last_name}`\n"
        "Username: `{username}`\n"
        "Last Online: `{last_online}`\n"
        "Common Groups: `{common_groups}`\n"
        "════════════════\n"
        "Bio:\n{bio}"
    )
    WHOIS_PIC = (
        "**WHO IS \"{full_name}\"?**\n"
        "[Link to profile](tg://user?id={user_id})\n"
        "════════════════\n"
        "╠\n"
        "║**UserID**:   `{user_id}`\n"
        "╠\n"
        "║**First Name:**   `{first_name}`\n"
        "╠\n"
        "║**Last Name:**   `{last_name}`\n"
        "╠\n"
        "║**Username:**   `{username}`\n"
        "╠\n"
        "║**Last Online:**   `{last_online}`\n"
        "╠\n"
        "║{common_groups}\n"
        "════════════════\n"
        "╠\n"
        "║{profile_pics}\n"
        "╠\n"
        "║**Last Updated:**   `{profile_pic_update}`\n"
        "╠\n"
        "════════════════\n"
        "╠\n"
        "║**Bio:**   {bio}\n"
        "╠\n"
        "════════════════\n"
    )


    