
import asyncio
import os
import requests
import time

from os.path import dirname, basename, isfile
import glob
from datetime import datetime
from time import sleep
import os,subprocess,sys
from pyrogram import Filters, Message, api
from bfasbot import BOT, LOGS, run_async
from requests_futures.sessions import FuturesSession
from ..helpers import LogMessage, ReplyCheck
MIRROR_ACE_API_KEY = os.environ.get("MIRROR_ACE_API_KEY")
MIRROR_ACE_API_TOKEN = os.environ.get("MIRROR_ACE_API_TOKEN")
def files(fn):
  from os.path import dirname, basename, isfile
  import glob
  # Get a list of all the file paths that ends with .txt from in specified directory
  fileList = glob.glob('/app/.data/*'+fn)
  for filePath in fileList:
    try:
        all_mod = [basename(filePath).split(".")[0] for filePath in fileList if isfile(filePath)] 
        for rem in all_mod:
          os.remove(basename(isfile(filePath)).split("/")[:-1])
    except:
        print("Error while deleting file : ", filePath) 

def response_hook(resp, *args, **kwargs):
    # parse the json storing the result on the response object
    resp.data = resp.json()
@BOT.on_message(Filters.command(["mm"], ".") & Filters.me)
async def _imiro(bot: BOT, message: Message):
    download_location = "{}/.data/".format(os.getcwd())
    mone = await message.edit("Processing ...")
    if MIRROR_ACE_API_KEY is None or MIRROR_ACE_API_TOKEN is None:
        await mone.edit("This module requires API key from https://ouo.io/My1jdU. Aborting!")
        return False
    if not os.path.isdir(download_location):
        os.makedirs(download_location)
    required_file_name = None
    start = datetime.now()
    input_str = " ".join(message.command[1:])
    if message.reply_to_message is not None: 
        reply_message = message.reply_to_message
        
        
        try:
            c_time = time.time()
            downloaded_file_name = await reply_message.download(download_location
        )
        except Exception as e:
            print(e)# pylint:disable=C0103,W0703
            await mone.edit(str(e))
            return False
        else:
            end = datetime.now()
            ms = (end - start).seconds
            required_file_name = downloaded_file_name
            await mone.edit("Downloaded to `{}` in {} seconds.".format(basename(required_file_name), ms))
        
    elif input_str:
        input_str = input_str.strip()
        if os.path.exists(input_str):
            end = datetime.now()
            ms = (end - start).seconds
            required_file_name = input_str
            await mone.edit("Found `{}` in {} seconds.".format(input_str, ms))
        else:
            await mone.edit("File Not found in local server. Give me a file path :((")
            return False
    LOGS.info(required_file_name)
    
    if required_file_name:
        # required_file_name will have the full path
        file_name = os.path.basename(required_file_name)
        file_size = os.stat(required_file_name).st_size
        # /* STEP 1: get upload_key */
        step_one_url = "https://mirrorace.com/api/v1/file/upload"
        step_one_auth_params = {
            "api_key": MIRROR_ACE_API_KEY,
            "api_token": MIRROR_ACE_API_TOKEN
        }
        async with FuturesSession() as session:
            session.hooks['response'] = response_hook
            future = session.post(step_one_url, data=step_one_auth_params)
            
            resp = future.result()  
            LOGS.info(resp.status_code)
            if resp.status_code == 200:
                step_one_response_json = resp.json()
                LOGS.info(step_one_response_json)
                if step_one_response_json["status"] == "success":
                    sleep(5)
                    await mone.edit("Received Upload URL from MirrorAce. ...")
                    start = datetime.now()
                    # /* STEP 2: Upload file */
                    # step one: response vars
                    step_two_upload_url = step_one_response_json["result"]["server_file"]
                    cTracker = step_one_response_json["result"]["cTracker"]
                    upload_key = step_one_response_json["result"]["upload_key"]
                    default_mirrors = step_one_response_json["result"]["default_mirrors"]
                    max_chunk_size = step_one_response_json["result"]["max_chunk_size"]
                    max_file_size = step_one_response_json["result"]["max_file_size"]
                    max_mirrors = step_one_response_json["result"]["max_mirrors"]

                    # check file size limit
                    if int(file_size) >= int(max_file_size):
                        await mone.edit("File exceeds maximum file size allowed: ".format({max_file_size}))
                        return False

                    # step two: setup
                    mirrors = default_mirrors
                    chunk_size = int(max_chunk_size)
                    step_two_params = {
                        "api_key": MIRROR_ACE_API_KEY,
                        "api_token": MIRROR_ACE_API_TOKEN,
                        "cTracker": cTracker,
                        "upload_key": upload_key,
                        "mirrors[]": mirrors,
                        # //these required vars will be added by buildMultiPartRequest function
                        # //'files' => $file,
                        # //'mirrors[1]' => 1,
                        # //'mirrors[2]' => 2,
                    }

                    # //range vars //for multi chunk upload
                    response = False
                    fn = basename(required_file_name).split(".")[0]

                    async with open(required_file_name, "rb") as f_handle:
                        # start chunk upload
                        for chunk in iter((lambda: f_handle.read(chunk_size)), ""):
                            # for chunk in f_handle.read(chunk_size):
                            # print(chunk)
                            # while (i < chunks) and not while_error:
                            # chunk = f_handle.read(chunk_size)
                            if not chunk:
                                break
                            headers = {
                                "Content-Range": str(len(chunk)),
                                "Content-Length": str(len(step_two_params) + len(chunk)),
                                 "Content-Type": "multipart/form-data"
                            }

                            # https://github.com/aio-libs/aiohttp/issues/3571#issuecomment-456528924
                            response = requests.post(
                                step_two_upload_url,
                                files=[("files", (file_name, chunk))],
                                data=step_two_params,
                                # headers=headers
                            )
                            LOGS.info(response.content)

                    LOGS.info(response)
                    final_response = response.json()
                    if final_response["status"] == "success":
                        end = datetime.now()
                        ms = (end - start).seconds
                        final_url = final_response["result"]["url"]
                        mone.edit("`{}` Uploaded to {} in {} seconds".format(input_str, final_url, ms))
                        files(fn)
                    else:
                        mone.edit("MirrorAce returned {} => {}".format(final_response['status'], final_response['result']))
                        files(fn)
                else:
                    mone.edit("MirrorAce returned {} => {}, after STEP TWO".format(step_one_response_json['status'], step_one_response_json['result']))
                    files(fn)
            else:
                mone.edit("MirrorAce returned {} => {}, after STEP ONE".format(resp['status'], resp['result']))
                files(fn)
    else:
        mone.edit("File Not found in local server. Give me a file path :((")
        files(fn)