#! /usr/bin/python3

import ctypes
from urllib.request import urlopen, urlretrieve
from xml.dom import minidom
from PIL import Image
from os import walk, getenv, system, getlogin
from shutil import copyfile
import pathlib
import datetime
import win32gui

#link=https://stackoverflow.com/questions/4438020/how-to-start-a-python-file-while-windows-starts
def add_to_startup(file_path=""):
    USER_NAME = getlogin()
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

def set_wallpaper_permanent(picPath):
    appdata = getenv("APPDATA")
    dst = appdata+"\Microsoft\Windows\Themes"
    image = picPath
    for root2, dirs2, files2 in walk(dst):
        for files2 in files2:
            if files2.endswith((".jpg")):
                copyfile(image,files2)
            copyfile(image, dst + "\TranscodedWallpaper")
    system("taskkill /f /im explorer.exe")
    system("C:\Windows\explorer.exe")

def set_wallpaper_temporary(picPath):
    ctypes.windll.user32.SystemParametersInfoA(20, 0, picPath.encode("us-ascii"), 2)

def set_wallpaper_permanent2(picPath):
    win32gui.SystemParametersInfo(0x0014, picPath, 1+2)
    
if __name__=='__main__':

    #only on windows 
    #add_to_startup()
    
    #Directory to save images
    saveDir = 'F:\BingWallPaper\\'
    
    #create the directory directory if it does not exist
    pathlib.Path(saveDir).mkdir(parents=True, exist_ok=True)

    i = 0
    while i<1:
        try:
            usock = urlopen('http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=zh-CN')
        except:
            i = 0
        else:
            i = 1
            
    xmldoc = minidom.parse(usock)

    #get today's date
    date = str(datetime.date.today())
    
    #Parsing the XML File
    for element in xmldoc.getElementsByTagName('url'):
        url = 'http://www.bing.com' + element.firstChild.nodeValue

        #Get Current Date as fileName for the downloaded Picture
        #picPath_temp = saveDir  + 'bingwallpaper' + date + '.jpg'  .... experimenting stuff
        picPath = saveDir  + 'bingwallpaper' + date +'.jpg'
        #if os.path.exists(picPath)==False:
        if True:
            urlretrieve(url, picPath)
            #Convert Image
            picData = Image.open(picPath)
            picData.save(picPath)
            picData.save(picPath.replace('jpg','bmp'))
            picPath = picPath.replace('jpg','bmp')
    set_wallpaper_permanent2(picPath)
