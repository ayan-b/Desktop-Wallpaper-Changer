import requests
from urllib.request import urlopen, urlretrieve
from PIL import Image
from os import path
import pathlib
import datetime

from set_wallpaper_permanent import set_wallpaper_permanent
from debug import print_download_status

url = 'https://source.unsplash.com/random/2732x1536'
date = str(datetime.date.today())

def picpath_unsplash(file_url, saveDir, SHOW_DEBUG):
    if SHOW_DEBUG:
        print ("Download from:%s" %file_url)
    #Get Current Date as fileName for the downloaded Picture
    picPath_unsplash = saveDir  + 'unsplash' + date +'.jpg'
    if SHOW_DEBUG:
        urlretrieve(file_url, picPath_unsplash, print_download_status)
    else:
        urlretrieve(file_url, picPath_unsplash)
    if SHOW_DEBUG:
        print ('URL retrieved')
    #Convert Image
    picData = Image.open(picPath_unsplash)
    if SHOW_DEBUG:
        print ('Image opened')
    picData.save(picPath_unsplash)
    if SHOW_DEBUG:
        print ('Saving ...')
    return picPath_unsplash

def change_wp(wp_unsplash, saveDir, SHOW_DEBUG):
    file_url = url
    picPath_unsplash = picpath_unsplash(file_url, saveDir, SHOW_DEBUG)
    set_wallpaper_permanent(picPath_unsplash, SHOW_DEBUG)
