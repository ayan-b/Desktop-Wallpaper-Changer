import requests
from urllib.request import urlopen, urlretrieve
from os import path
import pathlib
import datetime
from bs4 import BeautifulSoup

from set_wallpaper_permanent import set_wallpaper_permanent
from debug import print_download_status
from save_image import save_image
from get_url import get_url

url = 'https://apod.nasa.gov/apod/'
date = str(datetime.date.today())

def picpath_pod(file_url, saveDir, SHOW_DEBUG):
    temp = file_url
    file_url = url + file_url
    picPath_pod = saveDir  + 'NASA_PoD' + temp.replace('/','-') +'.jpg'
    if SHOW_DEBUG:
        print ( "Download from: %s" %file_url )

    picPath_pod = get_url ( file_url, picPath_pod, SHOW_DEBUG )
    picPath_pod = save_image ( picPath_pod, SHOW_DEBUG )
    picPath_pod = save_image ( picPath_pod, SHOW_DEBUG )

    return picPath_pod


def change_wp(wp_pod, saveDir, SHOW_DEBUG):
    if path.isfile(wp_pod)==True:
        if SHOW_DEBUG:
            print ('PoD Picture already found, updating that only')
        set_wallpaper_permanent(wp_pod, SHOW_DEBUG)
    else:
        source_code = BeautifulSoup(urlopen(url).read(), "html.parser")
        link = source_code.find_all('a')
        if SHOW_DEBUG:
            print ('Getting URL for PoD')
        c = 0
        for link in source_code.findAll('a'):
            c+=1
            if c==2:
                file_url = link.get('href')
                break
        picPath_pod = picpath_pod(file_url, saveDir, SHOW_DEBUG)
        set_wallpaper_permanent(picPath_pod, SHOW_DEBUG)
