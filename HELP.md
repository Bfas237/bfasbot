# BfasBot - A help page

## General Information

This program is a Selfbot for the [Telegram Messenger](https://telegram.org) based on [Pyrogram](https://github.com/pyrogram/pyrogram). A normal bot can also be run but userbot is recommended. 

## Features

- Execute codes
- Welcome new users joing groups
- Send Polls
- Convert an image to ascii and send to current chat
- Query a user or chat and return full info
- Convert html to markdown format
- Query a chat and get admins and member stats
- Change profile pic, first and last name
- Paste long codes to dogbin
- Upload medias and files to transfer.sh



### First Commands (`1start.py`)


| Command | Action |
|---|---|
| `.alive` | Tells you that the bot is running |
| `.help` | Gives out a link to this document |

### Administration (`admin.py`)

These work only in reply to another user.

| Command | Action |
|---|---|
|  `?ban x` |  Bans a replied-to user for time `x`
|  `?unban` |  Unbans a replied-to user
| `?mute x` |  Mutes a replied-to user for time `x`
|  `?unmute` |  Unmutes a replied-to user
|  `?kick` |  Kicks a replied-to user
|  `!mod` |  Promote a user to moderator
| `!unmod` |  Demote a user to initial state

Timed restrictions can be applied in the following scheme:

| Command | Action |
|---|---|
|  `1d` | 1 day
| `2h` | 2 hours
| `3w` | 3 weeks

### Evaluation (`evaluation.py`)

Evaluate and Execute whithin Telegram

| Command | Description |
|---|---|
| `.eval <query>` | Evaluate a string of x (e.g. `message.chat.title` for chat title) |
| `.exec <query>` | Execute a string of x.* |

***Note:** Using `.eval` for `from_user` or `send_*` attributes/methods is NOT recommended as you might expose your phone number unwillingly.

### Information (`get_info.py`)

Get information about your administration and chat

| Command | Description |
|---------|-------------|
| `!admins` | Gives out a list of all admins in a chat. |
| `!members` | Gives out counter of all members, bots and deleted accounts in that group. |
| `.id` | Gives out the File ID of a replied-to media. If there is neither a media nor a reply it will be the Chat ID. |


### Modules (`loads.py`)


| Command | Description |
|---|---|
| `.all` | Sends all loaded modules including active and inactive

### Miscellaneous (`misc.py`)


| Command | Description |
|---|---|
|  `.r` | Text replacement with a *Did you mean* Functionality
| `.i` | Text replacement with a *I meant* Functionality


### Who Is ...? (`whois.py`)


| Command | Description |
|---|---|
|  `.whois` | Gives out information about a user

### External File Upload (`file_transfer.py`)


| Command | Description |
|---|---|
|  `.ft` | Upload any file or media to https://transfer.sh
| `.asc` | Convert and send ascii of the image