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

img_formats = ("jpg", "jpeg", "bmp", "png")

url_root = 'https://apod.nasa.gov/apod/'

def set_url(date):
    date_format = str(datetime.datetime.strftime(date, "%y%m%d"))
    modf = "ap" + date_format + ".html"
    url = url_root + modf
    return url, modf

def picpath_pod(file_url, saveDir, url, modf, date, SHOW_DEBUG):
    file_url = url + file_url
    file_url = file_url.replace(modf,"")
    picPath_pod = saveDir  + 'NASA_PoD' + str(date) + '.jpg'
    if SHOW_DEBUG:
        print ( "Download from: %s" %file_url )

    picPath_pod = get_url ( file_url, picPath_pod, SHOW_DEBUG )
    picPath_pod = save_image ( picPath_pod, SHOW_DEBUG )

    return picPath_pod


def change_wp(wp_pod, saveDir, SHOW_DEBUG, date):
    url, modf = set_url(date)
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
            c += 1
            if c == 2:
                file_url = link.get('href')
                break
        
        # Today's APoD maybe a video
        if not file_url.lower().endswith(img_formats):
            date = date - datetime.timedelta(days=1)
            if SHOW_DEBUG:
                print("Today's PoD is not an image. Checking %s day's content ..." %( str(date) ))
            change_wp(wp_pod, saveDir, SHOW_DEBUG, date)

        else:
            picPath_pod = picpath_pod(file_url, saveDir, url, modf, date, SHOW_DEBUG)
            set_wallpaper_permanent(picPath_pod, SHOW_DEBUG)