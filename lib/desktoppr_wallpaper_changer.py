import datetime
import json
import random
import urllib
from urllib.request import urlopen, urlretrieve
from os import path

import requests

from lib.debug import print_download_status
from lib.utils import get_url
from lib.utils import save_image
from lib.utils import set_wallpaper_permanent

date = datetime.date.today()

url = 'https://api.desktoppr.co/1/wallpapers/random'
def getphotourl ():
    source = requests.get(url)
    if source.status_code == 200:
        source_code = source.json()
        photo_url = source_code['response']['image']['url']
        return photo_url
    
def picpath_desktoppr ( saveDir, SHOW_DEBUG ):

    photo_url = getphotourl()
    desktoppr_path = saveDir  + 'Desktoppr' + str(date) + str(random.randint(1,100000)) + '.jpg'
    if SHOW_DEBUG:
        print ( "Download from: " , photo_url )

    desktoppr_path = get_url ( photo_url, desktoppr_path , SHOW_DEBUG )
    savelink = save_image ( desktoppr_path, SHOW_DEBUG )

    return savelink

def change_wp (wp_desktoppr, saveDir, SHOW_DEBUG):
    savelink = picpath_desktoppr( saveDir, SHOW_DEBUG)
    set_wallpaper_permanent(savelink, SHOW_DEBUG)
