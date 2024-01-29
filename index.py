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

def download_folder():
    if os.path.exists(path):
        print(f'Folder [{tm.colored(app_name, "yellow")}] already exist in your desktop. It will be used to save your youtube video.\n')
    else:
        os.mkdir(path)
        print(f'A folder [{tm.colored(app_name, "yellow")}] was created in your desktop.\n')


print(f'Welcome to {app_logo} v1')
print(f'{getpass.getuser().upper()}({platform.system()}{platform.version()}) :: {dt.datetime.now().replace(microsecond=0)}')

start = 1
while start == 1:
    target_url = input('Entre a youtube URL: ')
    parsed_url = urlparse(target_url.strip())
    if parsed_url.netloc != 'www.youtube.com':  # check the component(netloc)
        print(f'Invalid youtube URL {not_valid}')
        continue
    else:
        print(f'A valid youtube URL {valid}')
        ytv = pt.YouTube(target_url)  # use_oauth=True, allow_oauth_cache=False
        download_folder()
        print(f'{tm.colored('│ Title      : ',  'cyan')} {ytv.title}')
        print(tm.colored('├──────────', 'cyan'))
        print(f'{tm.colored('│ Author     : ', 'cyan')} {ytv.author}')
        print(tm.colored('├──────────', 'cyan'))
        print(f'{tm.colored('│ Duration   : ', 'cyan')} {str(dt.timedelta(seconds=ytv.length))}')
        print(tm.colored('├──────────', 'cyan'))
        print(f'{tm.colored('│ Views      : ', 'cyan')} {ytv.views}\n')
        print('\nProcessing...')
        streams = ytv.streams.filter(adaptive=True, file_extension='mp4')
        print(f"Resolutions available : ", end=" ")
        res_list = []
        index = 0
        for stream in streams:
            if stream.resolution:
                resolution = tm.colored('['+stream.resolution+']', 'magenta')
                print(resolution, end=" ")
                res_list.append(stream.resolution)
        selected_rs = input(f'\nSelect the resolution you want : ')
        selected_rs_res = True
        while selected_rs_res:
            if selected_rs in res_list:
                stream = ytv.streams.filter(adaptive=True, res=selected_rs).first()
                stream.download(output_path=path, filename_prefix=selected_rs+' - ')
                selected_rs_res = False
            else:
                selected_rs = input('Unavailable resolution. Try again: ')
    req = input('Do you want to download another video[y/n]?: ')
    while req.strip() != 'n' and req.strip() != 'y':
        print('Error')
        req = input('[y/n]?: ')
    else:
        if req.split() == ['n']:
            print(f'Thank you for using this app')
            start = 0
        else:
            print('Another video will be downloaded')
