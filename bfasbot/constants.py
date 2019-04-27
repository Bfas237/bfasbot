

class First:
    ###
    #
    # 1start.py
    #
    ###
    ALIVE = (
        "╔═════\n"
        "║ **\U0001F916 BOT STATUS:**  \U0001f525\n"
        "╠═════\n"
        "║**Library:**   `{}` \n"
        "╠\n"
        "║**System Info:**   `{}` \n"
        "╠\n"
        "║**Bot Version:**   `{}`\n"
        "╠\n"
        "║**Current Uptime:**   `{}`\n"
        "╠\n"
        "║**Github Repo:**   [{}]({})\n"
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
    BANNED = "{} has been banned."
    BANNED_TIME = "{} has been banned for {}."
    BANNED_LOG = (
        "[{}](tg://user?id={}) has been banned from \"[{}](t.me/c/{}/{})\""
    )

    UNBANNED = "{} has been unbanned."
    UNBANNED_LOG = (
        "[{}](tg://user?id={}) has been unbanned from \"[{}](t.me/c/{}/{})\""
    )

    PROMOTED = "{} has been promoted to **Moderator.**"
    PROMOTED_LOG = (
        "[{}](tg://user?id={}) has been promoted to Moderator in \"[{}](t.me/c/{}/{})\""
    )
    UNPROMOTED = "{} has been Demoted back to **Normal user.**"
    UNPROMOTED_LOG = (
        "[{}](tg://user?id={}) has been Demoted back to Normal user in \"[{}](t.me/c/{}/{})\""
    )
    MUTED = "{} has been muted."
    MUTED_TIME = "{} has been muted for {}."
    MUTED_LOG = (
        "[{}](tg://user?id={}) has been muted in \"[{}](t.me/c/{}/{})\""
    )

    UNMUTED = "{} has been unmuted."
    UNMUTED_LOG = (
        "[{}](tg://user?id={}) has been unmuted in \"[{}](t.me/c/{}/{})\""
    )

    KICKED = "{} has been kicked."
    KICKED_LOG = (
        "[{}](tg://user?id={}) has been kicked from \"[{}](t.me/c/{}/{})\""
    )


class MiscStrings:
    ###
    #
    # misc.py
    #
    ###
    UPTIME = "Current Uptime\n{}"

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
        "**WHO IS \"{}\"?**\n"
        "════════════════\n"
        "UserID: `{}`\n"
        "First Name: {}\n"
        "Last Name: {}\n"
        "Username: {}\n"
        "Last Online: {}\n"
        "Common Groups: {}\n"
        "════════════════\n"
        "Bio: {}"
    )
    WHOIS_PIC = (
        "**WHO IS \"{}\"?**\n"
        "════════════════\n"
        "UserID: `{}`\n"
        "First Name: {}\n"
        "Last Name: {}\n"
        "Username: {}\n"
        "Last Online:   `{}`\n"
        "Profile Pics: {}\n"
        "Common Groups: {}\n"
        "════════════════\n"
        "Bio: {}"
    )


class Steam:
    ###
    #
    # steam.py
    #
    ###
    ACC_MSG = (
        "╔═════\n"
        "║ **Steam Account**\n"
        "╠═════\n"
        "║ Login\n"
        "║ `{login}`\n"
        "╠═════\n"
        "║ Password\n"
        "║ `{password}`\n"
        "╠═════\n"
        "║ SteamID\n"
        "║ `{steamid}`\n"
        "╠═════\n"
        "║ URL\n"
        "║ steam.pm/{steamid}\n"
        "╚═════"
    )

class www:
    ###
    #
    # www.py
    #
    ###
    SpeedTest = (
        "Speedtest started at `{start}`\n\n"
        "Ping:\n{ping} ms\n\n"
        "Download:\n{download}\n\n"
        "Upload:\n{upload}\n\n"
        "ISP:\n__{isp}__"
    )

    NearestDC = (
        "Country: `{}`\n"
        "Nearest Datacenter: `{}`\n"
        "This Datacenter: `{}`"
    )
