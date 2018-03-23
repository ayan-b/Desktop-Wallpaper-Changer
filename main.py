#! /usr/bin/python3

import ctypes
from urllib.request import urlopen, urlretrieve
from xml.dom import minidom
from PIL import Image
from os import walk, getenv, system, getlogin, path
from shutil import copyfile
import pathlib
import datetime
import win32gui

#get today's date
date = str(datetime.date.today())

SHOW_DEBUG = False
#Directory to save images
saveDir = 'F:\WallPaper\\'

#link=https://stackoverflow.com/questions/4438020/how-to-start-a-python-file-while-windows-starts
def add_to_startup(file_path=""):
    USER_NAME = getlogin()
    if file_path == "":
        file_path = path.dirname(path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

def set_wallpaper_permanent(picPath):
    if SHOW_DEBUG:
        print ('Setting the wallpaper')
    win32gui.SystemParametersInfo(0x0014, picPath, 1+2)

def directoryCheck ():
    #create the directory directory if it does not exist
    pathlib.Path(saveDir).mkdir(parents=True, exist_ok=True)


BING_MARKETS = [u'ar-XA',
                u'bg-BG',
                u'cs-CZ',
                u'da-DK',
                u'de-AT',
                u'de-CH',
                u'de-DE',
                u'el-GR',
                u'en-AU',
                u'en-CA',
                u'en-GB',
                u'en-ID',
                u'en-IE',
                u'en-IN',
                u'en-MY',
                u'en-NZ',
                u'en-PH',
                u'en-SG',
                u'en-US',
                u'en-XA',
                u'en-ZA',
                u'es-AR',
                u'es-CL',
                u'es-ES',
                u'es-MX',
                u'es-US',
                u'es-XL',
                u'et-EE',
                u'fi-FI',
                u'fr-BE',
                u'fr-CA',
                u'fr-CH',
                u'fr-FR',
                u'he-IL',
                u'hr-HR',
                u'hu-HU',
                u'it-IT',
                u'ja-JP',
                u'ko-KR',
                u'lt-LT',
                u'lv-LV',
                u'nb-NO',
                u'nl-BE',
                u'nl-NL',
                u'pl-PL',
                u'pt-BR',
                u'pt-PT',
                u'ro-RO',
                u'ru-RU',
                u'sk-SK',
                u'sl-SL',
                u'sv-SE',
                u'th-TH',
                u'tr-TR',
                u'uk-UA',
                u'zh-CN',
                u'zh-HK',
                u'zh-TW']

def picpath_bing(xmldoc):
    #Parsing the XML File
    for element in xmldoc.getElementsByTagName('url'):
        if SHOW_DEBUG:
            print ('Getting URL for Bing')
        url = 'http://www.bing.com' + element.firstChild.nodeValue

        #Get Current Date as fileName for the downloaded Picture
        picPath = saveDir  + 'bingwallpaper' + date +'.jpg'
        urlretrieve(url, picPath)
        if SHOW_DEBUG:
            print ('URL retrieved')
        #Convert Image
        picData = Image.open(picPath)
        if SHOW_DEBUG:
            print ('Image opened')
        picData.save(picPath)
        if SHOW_DEBUG:
            print ('Saving ...')
        picData.save(picPath.replace('jpg','bmp'))
        picPath = picPath.replace('jpg','bmp')
        return picPath

def get_usock_bing():
    i = 0
    while i<1:
        try:
            print ('Opening URL for Bing')
            usock = urlopen('http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-IN')
        except:
            i = 0
        else:
            i = 1
    return usock



if __name__=='__main__':

    #only on windows 
    #add_to_startup()
    choice = 1
    directoryCheck()

    wp_bing = saveDir  + 'bingwallpaper' + date +'.jpg'
    
    if path.isfile(wp_bing)==True:
        print ('Picture already found, updating that only')
        set_wallpaper_permanent(wp_bing)
    else:
        print ('Picture is not in the system, updating process start ...')
        usock = get_usock_bing()   
        xmldoc = minidom.parse(usock)
        picPath_bing = picpath_bing(xmldoc)
    if choice == 1:
        set_wallpaper_permanent(picPath_bing)
    else:
        print ("In development")
        set_wallpaper_permanent(picPath_bing)
