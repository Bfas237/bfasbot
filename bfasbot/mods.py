from datetime import datetime, timezone, date, timedelta    
from urllib.parse import unquote, urlparse
from os.path import splitext, basename
import logging, urllib, os, re, sys, sqlite3, json, io, requests, requests, shutil, traceback, os.path, urllib.request, time, fnmatch, glob, asyncio, async_timeout, aiohttp, aiofiles
from os import path
MIRROR_ACE_API_KEY = os.environ.get("MIRROR_ACE_API_KEY")
MIRROR_ACE_API_TOKEN = os.environ.get("MIRROR_ACE_API_TOKEN")
import cgi
import importlib
import os
import tempfile
import shutil
import sys, logging
from bfasbot.helpers import LogMessage, ReplyCheck
logger = logging
from pyrogram.errors import (UserIsBlocked, FloodWait, FileIdInvalid, BadRequest, Flood, InternalServerError, SeeOther, Unauthorized, UnknownError, MessageNotModified, UsernameNotOccupied, MessageEmpty, UserAdminInvalid, ChatAdminRequired, PeerIdInvalid)
try:
    from urllib.parse import quote_plus, urlparse, urljoin
    import urllib.request
    python3 = True
except ImportError:
    from urllib import quote_plus
    import urllib2 
    python3 = False
from itertools import islice
import requests, json
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
from os.path import dirname, basename, isfile
import glob
from datetime import datetime
from time import sleep
import os,subprocess,sys
from pyrogram import Filters, Message, api
from clint.textui import progress
from bfasbot.guess import *
import warnings, random, requests
from random import randint
try:
    from urllib.parse import quote_plus
    import urllib.request
    python3 = True
except ImportError:
    from urllib import quote_plus
    import urllib2 
    python3 = False

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
  
import time, os, math
download_path = "{}/.data/".format(os.getcwd())
if not os.path.isdir(download_path):
  os.makedirs(download_path)
options={}
base_headers = {
        'User-Agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
headers = dict(base_headers, **options)
known_sessions_file = os.path.join(os.path.dirname(__file__), 'known_sessions')
def timedate(dat):
    import timeago, datetime
    now = datetime.datetime.now() + datetime.timedelta(seconds = 1)
    date = datetime.datetime.now()
    return timeago.format(dat, now)


options={}
base_headers = {
        'User-Agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
headers = dict(base_headers, **options)
from requests_futures.sessions import FuturesSession

def read_known_sessions():
    if not os.path.isfile(known_sessions_file):
        return set()
    with open(known_sessions_file, 'rb') as f:
        return set(int(s.strip()) for s in f.readlines())

def write_known_sessions(data):
    with open(known_sessions_file, 'wb') as f:
        f.write('\n'.join(str(s) for s in sorted(data)))
def get_extension(media):
    """Gets the corresponding extension for any Telegram media"""

    # Photos are always compressed as .jpg by Telegram
    if isinstance(media, (UserProfilePhoto, ChatPhoto, MessageMediaPhoto)):
        return '.jpg'

    # Documents will come with a mime type
    if isinstance(media, MessageMediaDocument):
        if isinstance(media.document, Document):
            if media.document.mime_type == 'application/octet-stream':
                # Octet stream are just bytes, which have no default extension
                return ''
            else:
                extension = guess_extension(media.document.mime_type)
                return extension if extension else ''

    return ''
def check_media(chk):   
    extensionsToCheck  = ['.exe', '.msi', '.Exe','.Msi', '.mp3', '.AAC','.M4A', '.doc', '.docx','.txt','.pdf','.epub','.bat','.py','.js','.html','.css','.go','.xlb','.xls', '.zip', '.rar','.7z','.gz', '.avi', '.mkv','.webm', '.mp4', '.m1v', '.movie', '.mpeg', '.mov', '.png']
    hou = [extension for extension in extensionsToCheck if(extension in chk.lower())]
    media = ""
    if hou is not None:
      if chk.lower().endswith(('.apk', '.xapk', '.jar', '.jav')):
        media = "Apps"
      elif chk.lower().endswith(('.exe', '.msi')):
        media = "Software"
      elif chk.lower().endswith(('.png', '.jpg', '.jpeg', '.jpe')):
        media = "Pictures"
      elif chk.lower().endswith(('.doc', '.docx','.txt','.pdf','.epub','.bat','.py','.js','.html','.css','.go','.xlb','.xls')):
        media = "Documents"
      elif chk.lower().endswith(('.zip', '.rar','.7z','.gz','.bin')):
        media = "Archives"
      else:
        media = "Misc"
      return media
    
    else:
      return False
from base64 import b64decode
from struct import unpack

def parse_inline_message_id(inline_message_id):
    inline_message_id += "=" * ((4 - len(inline_message_id) % 4) % 4) 
    dc_id, _id, access_hash = unpack("<iqq",b64decode(inline_message_id,"-_"))
    return api.types.InputBotInlineMessageID(dc_id=dc_id,id=_id,access_hash=access_hash)
    
def SizeFormatter(b: int,
                  human_readable: bool = False) -> str:
    """
    Adjust the size from bits to the right measure.

    b (``int``): Number of bits.


    SUCCESS Returns the adjusted measure (``str``).
    """
    if human_readable:
        B = float(b / 8)
        KB = float(1024)
        MB = float(pow(KB, 2))
        GB = float(pow(KB, 3))
        TB = float(pow(KB, 4))

        if B < KB:
            return "{0} B".format(B)
        elif KB <= B < MB:
            return "{0:.2f} KB".format(B/KB)
        elif MB <= B < GB:
            return "{0:.2f} MB".format(B/MB)
        elif GB <= B < TB:
            return "{0:.2f} GB".format(B/GB)
        elif TB <= B:
            return "{0:.2f} TB".format(B/TB)
    else:
        B, b = divmod(int(b), 8)
        KB, B = divmod(B, 1024)
        MB, KB = divmod(KB, 1024)
        GB, MB = divmod(MB, 1024)
        TB, GB = divmod(GB, 1024)
        tmp = ((str(TB) + "TB, ") if TB else "") + \
            ((str(GB) + "GB, ") if GB else "") + \
            ((str(MB) + "MB, ") if MB else "") + \
            ((str(KB) + "KB, ") if KB else "") + \
            ((str(B) + "B, ") if B else "") + \
            ((str(b) + "b, ") if b else "")
        return tmp[:-2]


def TimeFormatter(milliseconds: int) -> str:
    """
    Adjust the time from milliseconds to the right measure.

    milliseconds (``int``): Number of milliseconds.


    SUCCESS Returns the adjusted measure (``str``).
    """
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]



async def DFromUToTelegramProgress(client,
                             current,
                             total,
                             msg,
                             chat_id,
                             start, text) -> None:
   
    # 1048576 is 1 MB in bytes
    import time
    now = time.time()
    diff = now - start
    if round(diff % 4.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)
        # 0% = [░░░░░░░░░░░░░░░░░░░░]
        # 100% = [████████████████████]
        progress = "[{0}{1}] {2}%\n".format(''.join(["█" for i in range(math.floor(percentage / 5))]),
                                            ''.join(
            ["░" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2))
        tmp = progress + "\n**Running:** {0}/{1}\n\n**Speed:** {2}/s \n\n**Estimated Time:** {3}/{4}\n".format(SizeFormatter(b=current * 8,
                                                                         human_readable=True),
                                                           SizeFormatter(b=total * 8,
                                                                         human_readable=True),
                                                           SizeFormatter(b=speed * 8,
                                                                         human_readable=True),
                                                           elapsed_time if elapsed_time != '' else "0 s",
                                                           estimated_total_time if estimated_total_time != '' else "0 s")
        try:
          await msg.edit(text=text + tmp)
          sleep(0.5)
        except FloodWait as e:
          await msg.edit(str(e) + ' FloodWaiting for ' + str(e.x * 2) + ' secs')
          await LogMessage(str(e) + ' FloodWaiting for ' + str(e.x * 2) + ' secs')
          logging.warning('FloodWaiting: {} secs'.format(e.x))
          sleep(e.x * 2)

        
        
        
        
        
common_words = frozenset(("if", "but", "and", "the", "when", "use", "to", "for"))
title = "When to use Python for web applications"
title_words = set(title.lower().split())
keywords = title_words.difference(common_words)




def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def dynamic_data(data):
    return Filters.create(
        name="DynamicData",
        func=lambda filter, callback_query: filter.data == callback_query.data,
        data=data  # "data" kwarg is accessed with "filter.data"
    )

def fileExt(url):
    """
    Check if file extention exist then

    """
    # compile regular expressions
    reQuery = re.compile(r'\?.*$', re.IGNORECASE)
    rePort = re.compile(r':[0-9]+', re.IGNORECASE)
    reExt = re.compile(r'(\.[A-Za-z0-9]+$)', re.IGNORECASE)

    # remove query string
    url = reQuery.sub("", url)

    # remove port
    url = rePort.sub("", url)

    # extract extension
    matches = reExt.search(url)
    if None != matches:
        return matches.group(1)
    return None

def get_filename(url):
    """
    Get an authentique filename from content-dispostion
    """
    options={}
    base_headers = {
        'User-Agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    headers = dict(base_headers, **options)
    result = requests.get(url, allow_redirects=True, stream=True, headers=headers)
    fname = None
    cd = result.headers.get("content-disposition")
    if cd:
        value, params = cgi.parse_header(cd)
        fname = params.get("filename")
    content_type = ""  
    filenams = "" 
    filenam = ""
    su = []
    code = result.status_code
    headers = result.headers
    content_type = headers['content-type'] 
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    else:
      pass
    if code < 400:
      token = '[-!#-\'*+.\dA-Z^-z|~]+'
      qdtext='[]-~\t !#-[]'
      mimeCharset='[-!#-&+\dA-Z^-z]+'
      language='(?:[A-Za-z]{2,3}(?:-[A-Za-z]{3}(?:-[A-Za-z]{3}){,2})?|[A-Za-z]{4,8})(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|\d{3}))(?:-(?:[\dA-Za-z]{5,8}|\d[\dA-Za-z]{3}))*(?:-[\dA-WY-Za-wy-z](?:-[\dA-Za-z]{2,8})+)*(?:-[Xx](?:-[\dA-Za-z]{1,8})+)?|[Xx](?:-[\dA-Za-z]{1,8})+|[Ee][Nn]-[Gg][Bb]-[Oo][Ee][Dd]|[Ii]-[Aa][Mm][Ii]|[Ii]-[Bb][Nn][Nn]|[Ii]-[Dd][Ee][Ff][Aa][Uu][Ll][Tt]|[Ii]-[Ee][Nn][Oo][Cc][Hh][Ii][Aa][Nn]|[Ii]-[Hh][Aa][Kk]|[Ii]-[Kk][Ll][Ii][Nn][Gg][Oo][Nn]|[Ii]-[Ll][Uu][Xx]|[Ii]-[Mm][Ii][Nn][Gg][Oo]|[Ii]-[Nn][Aa][Vv][Aa][Jj][Oo]|[Ii]-[Pp][Ww][Nn]|[Ii]-[Tt][Aa][Oo]|[Ii]-[Tt][Aa][Yy]|[Ii]-[Tt][Ss][Uu]|[Ss][Gg][Nn]-[Bb][Ee]-[Ff][Rr]|[Ss][Gg][Nn]-[Bb][Ee]-[Nn][Ll]|[Ss][Gg][Nn]-[Cc][Hh]-[Dd][Ee]'
      valueChars = '(?:%[\dA-F][\dA-F]|[-!#$&+.\dA-Z^-z|~])*'
      dispositionParm = '[Ff][Ii][Ll][Ee][Nn][Aa][Mm][Ee]\s*=\s*(?:({token})|"((?:{qdtext}|\\\\[\t !-~])*)")|[Ff][Ii][Ll][Ee][Nn][Aa][Mm][Ee]\*\s*=\s*({mimeCharset})\'(?:{language})?\'({valueChars})|{token}\s*=\s*(?:{token}|"(?:{qdtext}|\\\\[\t !-~])*")|{token}\*\s*=\s*{mimeCharset}\'(?:{language})?\'{valueChars}'.format(**locals())

      try:
        m = re.match('(?:{token}\s*;\s*)?(?:{dispositionParm})(?:\s*;\s*(?:{dispositionParm}))*|{token}'.format(**locals()), result.headers['Content-Disposition'])

      except KeyError:
        name = path.basename(unquote(urlparse(url).path))

      else:
        if not m:
          name = path.basename(unquote(urlparse(url).path))

  # Many user agent implementations predating this specification do not
  # understand the "filename*" parameter.  Therefore, when both "filename"
  # and "filename*" are present in a single header field value, recipients
  # SHOULD pick "filename*" and ignore "filename"

        elif m.group(8) is not None:
          name = urllib.unquote(m.group(8)).decode(m.group(7))

        elif m.group(4) is not None:
          name = urllib.unquote(m.group(4)).decode(m.group(3))

        elif m.group(6) is not None:
          name = re.sub('\\\\(.)', '\1', m.group(6))

        elif m.group(5) is not None:
          name = m.group(5)

        elif m.group(2) is not None:
          name = re.sub('\\\\(.)', '\1', m.group(2))

        else:
          name = m.group(1)

  # Recipients MUST NOT be able to write into any location other than one to
  # which they are specifically entitled

        if name:
          name = path.basename(name)

        else:
          name = path.basename(unquote(urlparse(url).path))

        name = unquote(name).strip('\n').strip('\*').replace('UTF-8', "").strip('\=').replace('\"','').replace('\'','').replace('?','').replace(" ", "_")

      filenam, ext = splitext(basename(name))
      if ext:
        ext = fileExt(url)
      if ext == None:
        logger.warning("No filetype could be determined for '%s', skipping.",
            filenam
        )
      if ext in common_types.keys() or ext in types_map.keys():
        ext = '{}'.format(ext)
        mime_typ = '{}'.format(types_map[ext])
        filenams = filenam+ext
        

      elif content_type == 'image/jpeg' or content_type == 'image/jpg' or content_type == 'image/jpe':
            ext = '.jpeg'

      elif content_type == 'image/x-icon' or content_type == 'image/vnd.microsoft.icon':
            ext = '.ico'

      elif content_type == 'application/x-7z-compressed':
            ext = '.7z'
      elif content_type == 'image/png':
            ext = '.png'
      ent = ext
      if ent in common_types or ent in types_map:
        print ('File Extenstion: {} has MIME Type: {}.'.format(ent, types_map[ent]))
      for k, v in types_map.items():
        if content_type in v:
          su.append(k)
        
    return[filenams,filenam, content_type, su, fname]
  
def generate_uuid():
        random_string = ''
        random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        uuid_format = [8]
        for n in uuid_format:
            for i in range(0,n):
                random_string += str(random_str_seq[r.randint(0, len(random_str_seq) - 1)])
            if n != 8:
                random_string += '-'
        return random_string.strip('\n').replace('\"','').replace('\'','').replace('?','').replace(" ", "_")





def human_readable_bytes(bytes):
        KB = 1024
        MB = 1024 * 1024
        GB = MB * 1024

        if bytes >= KB and bytes < MB:
            result = bytes / KB
            converted = 'KB'
        elif bytes >= MB and bytes < GB:
            result = bytes / MB
            converted = 'MB'
        elif bytes >= GB:
            result = bytes / GB
            converted = 'GB'
        else:
            result = bytes
            converted = 'byte'

        result = "%.1f" % result
        results = (
            str(result) + ' ' + converted,
            result,
            converted
        )

        return results


def pretty_size(sizes):
    units = ['B', 'KB', 'MB', 'GB']
    unit = 0
    while sizes >= 1024:
        sizes /= 1024
        unit += 1
    return '%0.2f %s' % (sizes, units[unit])
def dosomething(buf):
    """Do something with the content of a file"""
    sleep(0.01)
    pass
from requests.exceptions import RequestException




def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]



nowq = datetime.now()
current_date_time = str(nowq).split(" ")[0] + " " + str(nowq.hour) + ":" + str(nowq.minute) + ":" + str(nowq.second)

def DownL(url):
    fname, ext = get_filename(url)
    file_name = fname+ext
    r = requests.get(url, stream=True, allow_redirects=True, headers=headers)
    with open(file_name, 'wb') as file:
      total_length = r.headers.get('content-length')
      if total_length is None:  # no content length header
        file.write(r.content)
      else:
        dl = 0
        total_length = int(total_length)
        for chunk in progress.bar(r.iter_content(chunk_size=8192*1024), expected_size=(total_length / 1024) + 1):
          if chunk:
            dl += len(chunk)
            done = int(100 * dl / total_length)
            file.write(chunk)
            file.flush()
            os.fsync(file.fileno())


  
  
LOGS = logging
async def DownLoadFile(url, file_name, fnames, client, message_id, chat_id):
    options={}
    base_headers = {
        'User-Agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    headers = dict(base_headers, **options)
    Glo = "@Bfas237bots"
    async with aiohttp.ClientSession() as session: 
      async with async_timeout.timeout(120):
        async with session.get(url) as r:
          File_name = file_name
          async with aiofiles.open(download_path+file_name, 'wb') as file:
            total_length = int(r.headers.get('content-length', 0)) or None
            downloaded_size = 0
            start = time.time()
            chunk_size=8192*1024
            if total_length is None:  # no content length header
              await file.write(r.content)
            else:
              
              dl = 0
              total_length = int(total_length)
              async for chunk in r.content.iter_chunked(chunk_size):
                if chunk:
                  dl += len(chunk)
                  await file.write(chunk)
                  done = int(100 * dl / total_length)
                  await DFromUToTelegramProgress(client, dl, total_length, message_id, chat_id, start, "**📥 Downloading:**")
                  downloaded_size += chunk_size
                  await file.flush()
                  os.fsync(file.fileno())
    return[file_name, Glo]

     
