import requests
from urllib.request import urlopen, urlretrieve
from os import path
import pathlib
import datetime
import random

from set_wallpaper_permanent import set_wallpaper_permanent
from debug import print_download_status
from save_image import save_image
from get_url import get_url

url = 'https://source.unsplash.com/featured/2732x1536'
date = str(datetime.date.today())
date = date + str(random.randint(1,10000000))

def picpath_unsplash(file_url, saveDir, SHOW_DEBUG):
    if SHOW_DEBUG:
        print ("Download from:%s" %file_url)

    #Get Current Date as fileName for the downloaded Picture
    picPath_unsplash = saveDir  + 'unsplash' + date +'.jpg'

    picPath_unsplash = get_url ( file_url, picPath_unsplash, SHOW_DEBUG )
    picPath_unsplash = save_image ( picPath_unsplash, SHOW_DEBUG )

    return picPath_unsplash

def change_wp(wp_unsplash, saveDir, SHOW_DEBUG):
    file_url = url
    picPath_unsplash = picpath_unsplash(file_url, saveDir, SHOW_DEBUG)
    set_wallpaper_permanent(picPath_unsplash, SHOW_DEBUG)
