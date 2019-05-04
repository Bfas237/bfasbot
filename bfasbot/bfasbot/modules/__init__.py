from bfasbot import (LOGS, LOAD, BOT, cmds, __source__, __author__, response_hook, run_async, BASE)
from pyrogram import Filters, Message
from ..constants import rog
from requests_futures.sessions import FuturesSession
import re
def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob
    global LOAD

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    
    return all_modules

ALL_MODULES = sorted(__list_all_modules())
LOGS.info("Modules to load:\n{}\n".format(", ".join(ALL_MODULES)))
__all__ = ALL_MODULES + ["ALL_MODULES"]
LOADs = "🧿 **Modules Loaded**: {}\n\n**Active:** {}\n".format(len(ALL_MODULES), ", ".join(ALL_MODULES))
LOAD += LOADs


def read_file(fn):
    from os.path import dirname, basename, isfile
    import glob
    

    mod_ = glob.glob(dirname(__file__) + "/*.py")
    all_mod = [
        basename(f)[:-3]
        for f in mod_
        if isfile(f) and f.endswith(".py")
    ]
    ALL_MODULE = sorted(all_mod)
    r = re.compile(".*{}".format(fn))
    match = list(filter(r.match, ALL_MODULE))
    for fd in match:
      mod = glob.glob(dirname(__file__) + "/{}.py".format(fd))
      with open(mod[0]) as f:
        return f.read()
 
@BOT.on_message(Filters.command("all", ".") & Filters.outgoing)
def _all(bot: BOT, message: Message):
    global LOAD
    message.edit(LOADs,disable_web_page_preview=True)


@BOT.on_message(Filters.me & Filters.command('repo', cmds))
def repo(client, message):
    global LOAD
    if len(message.command) > 1:
        if message.command[1] == "init":
          text = read_file("__init__")
        else:
          text = read_file(message.command[1])
    
        with FuturesSession() as session:
          session.hooks['response'] = response_hook
          future = session.post("{}/documents".format(BASE), data=text.encode("UTF-8"))
          response = future.result()  
          code = '{0}'.format(response.status_code)
          LINK = str(BASE) + "/" + code

          message.edit('Take a look at the source code of `{}` [HERE]({}'
                     '/{})'.format(message.command[1], BASE, response.data["key"]))
        return

    message.edit('**Github Repo:**   [{}]({})'.format(__author__,__source__))
    
    