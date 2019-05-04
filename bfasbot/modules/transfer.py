from time import sleep
import os,subprocess,sys
from pyrogram import Filters, Message, api
from bfasbot import BOT, LOGS

from ..helpers import LogMessage, ReplyCheck



@BOT.on_message(Filters.command(["ft"], ".") & Filters.me)
def _ivess(bot: BOT, message: Message):
    if message.reply_to_message is not None: 
        reply_message = message.reply_to_message
        download_location = download_path = "{}/.data/".format(os.getcwd())
        a = message.edit('Downloading with filetransfer'
        )
        
        after_download_file_name = bot.download_media(
            message=reply_message
        )
        filename_w_ext = os.path.basename(after_download_file_name)
        filename, download_extension = os.path.splitext(filename_w_ext)
        filename = filename.strip('\n').replace(' ','_')
        url = "https://transfer.sh/{}{}".format(str(filename), str(download_extension))
        max_days = "30"
        command_to_exec = [
            "curl",
             "-H", 'Max-Downloads: 5',
            "-H", 'Max-Days: 30', # + max_days + '',
            "--upload-file", after_download_file_name,
            url
        ]
        message.edit("uploading")
        try:
            LOGS.info(command_to_exec)
            t_response = subprocess.check_output(command_to_exec, stderr=subprocess.STDOUT)
            message.edit(t_response)
        except subprocess.CalledProcessError as exc:
            
            LOGS.info("Status : FAIL : REASON : %s %s", exc.returncode, exc.output)
            message.edit(exc.output.decode("UTF-8")
            )
        else:
            t_response_arry = t_response.decode("UTF-8").split("\n")[-1].strip()
            LOGS.info(t_response_arry)
            message.edit("**Upload was successful**: \n\n **Link**: {} \n\n **Valid for:**  {} days".format(t_response_arry, max_days),
                disable_web_page_preview=True
            )
            try:
                os.remove(after_download_file_name)
            except:
                pass
    else:
        message.edit("Invalid command. Reply to a message"
        )
