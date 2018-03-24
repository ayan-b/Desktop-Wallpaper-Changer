import requests
from urllib.request import urlopen, urlretrieve
from xml.dom import minidom
from PIL import Image
from os import walk, getenv, system, getlogin, path
from shutil import copyfile
import pathlib
import datetime
import win32gui
from sys import stdin, stdout
from bs4 import BeautifulSoup

from set_wallpaper_permanent import set_wallpaper_permanent
from debug import *

def picpath_pod(file_url, SHOW_DEBUG):
    if SHOW_DEBUG:
        print ("Download from:%s" %file_url)
    file_url = url + file_url
    #Get Current Date as fileName for the downloaded Picture
    picPath_pod = saveDir  + 'NASA_PoD' + date +'.jpg'
    if SHOW_DEBUG:
        urlretrieve(file_url, picPath_pod, print_download_status)
    else:
        urlretrieve(file_url, picPath_pod)
    if SHOW_DEBUG:
        print ('URL retrieved')
    #Convert Image
    picData = Image.open(picPath_pod)
    if SHOW_DEBUG:
        print ('Image opened')
    picData.save(picPath_pod)
    if SHOW_DEBUG:
        print ('Saving ...')
    picData.save(picPath_pod.replace('jpg','bmp'))
    picPath_pod = picPath_pod.replace('jpg','bmp')
    return picPath_pod

def change_wp(wp_pod, SHOW_DEBUG):
    if path.isfile(wp_pod)==True:
        if SHOW_DEBUG:
            print ('PoD Picture already found, updating that only')
        set_wallpaper_permanent(wp_pod, SHOW_DEBUG)
    else:
        url = 'https://apod.nasa.gov/apod/'
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
        picPath_pod = picpath_pod(file_url, SHOW_DEBUG)
        set_wallpaper_permanent(picPath_pod, SHOW_DEBUG)