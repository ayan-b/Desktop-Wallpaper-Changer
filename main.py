#! /usr/bin/python3

import datetime
import pathlib
import os

from lib.set_wallpaper_permanent import set_wallpaper_permanent
from lib.add_to_startup import add_to_startup
import lib.bing_wallpaper_changer
import lib.pod_wallpaper_changer
import lib.unsplash_wallpaper_changer
import lib.space_wallpaper_changer

SHOW_DEBUG = True

#Directory to save images
if os.path.exists("F:")==True:
    saveDir = "F:\\WallPaper\\"
else:
    saveDir = os.path.join(os.getcwd(), r'WallPaper')

date = datetime.date.today()

def directoryCheck ():
    #create the directory if it does not exist
    pathlib.Path(saveDir).mkdir(parents=True, exist_ok=True)

if __name__=='__main__':

    #only on windows 
    #add_to_startup()

    choice = 0
    directoryCheck()
    print ("Choice: ? 0: NASA Astronomy Picture of the Day, 1: Bing Image of the Day, 2: Random Pictures from Unsplash, 3. Space.com Image of the day ",)
    choice = int(input())
    wp_bing = saveDir  + 'bingwallpaper' + str(date) +'.jpg'
    wp_pod = saveDir + 'NASA_PoD' + str(date) + '.jpg'
    wp_unsplash = saveDir + 'unsplash' + str(date) + '.jpg'
    wp_space = saveDir + 'space' + str(date) + '.jpg'

    if choice == 1:
        lib.bing_wallpaper_changer.change_wp( wp_bing, saveDir, SHOW_DEBUG )

    elif choice == 0: 
        lib.pod_wallpaper_changer.change_wp( wp_pod, saveDir, SHOW_DEBUG, date )
    
    elif choice == 2:
        lib.unsplash_wallpaper_changer.change_wp( wp_unsplash, saveDir, SHOW_DEBUG )

    elif choice == 3:
        print ('Under Development')
        #space_wallpaper_changer.change_wp( wp_space, saveDir, SHOW_DEBUG )