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