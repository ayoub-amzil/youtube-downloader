import os
import datetime as dt
import termcolor as tm
import platform
import getpass
import pytube as pt
from urllib.parse import urlparse

app_name = 'Youtube Downloader'
app_logo = tm.colored(' ► ', 'white', 'on_red')+tm.colored(app_name, 'red', 'on_white')
path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+'\\'+app_name
valid = tm.colored(' ✔ ', 'white', 'on_green')
not_valid = tm.colored(' ✘ ', 'white', 'on_red')


# Creating a folder to hold the downloader videos (windows)
def download_folder():
    if os.path.exists(path):
        print(f'Folder [{tm.colored(app_name, "yellow")}] already exist in your desktop. It will be used to save your youtube video.\n')
    else:
        os.mkdir(path)
        print(f'A folder [{tm.colored(app_name, "yellow")}] was created in your desktop.\n')


print(f'Welcome to {app_logo} v1')
print(f'{getpass.getuser().upper()}({platform.system()}{platform.version()}) :: {dt.datetime.now().replace(microsecond=0)}')
