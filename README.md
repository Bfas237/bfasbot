# PyroBot 🔥🤖

A Telegram Userbot based on [Pyrogram](https://github.com/pyrogram/pyrogram)

## Features

* `.alive` - Check if your bot is running
* `.help` - Gives out a link to [all commands](HELP.md)

## Installation

1. `git clone https://git.colinshark.de/PyroBot/PyroBot`
2. `cd PyroBot`
3. Create a new `.env` file (as below)
4. Execute with `python -m pyrobot`
5. Send `.alive` in any chat to confirm the userbot is running

```python
API_ID = <your api_id>
API_HASH = <your api_hash>

LOGGER = <True / False>
LOGGER_GROUP = <chat_id of group to log to>
```

Get the `api_id` and `api_hash` from [Telegram](https://my.telegram.org/apps)

## Credits

* [Dan Tès](https://github.com/delivrance) for his [Pyrogram Library](https://github.com/pyrogram/pyrogram)
