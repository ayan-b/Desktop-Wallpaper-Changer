#! /usr/bin/python3

import datetime
import pathlib

from set_wallpaper_permanent import set_wallpaper_permanent
from add_to_startup import add_to_startup
import bing_wallpaper_changer
import pod_wallpaper_changer

SHOW_DEBUG = True
#Directory to save images
saveDir = 'F:\WallPaper\\'

date = str(datetime.date.today())

def directoryCheck ():
    #create the directory directory if it does not exist
    pathlib.Path(saveDir).mkdir(parents=True, exist_ok=True)

if __name__=='__main__':

    #only on windows 
    #add_to_startup()
    choice = 1
    directoryCheck()

    wp_bing = saveDir  + 'bingwallpaper' + date +'.jpg'
    wp_pod = saveDir + 'NASA_PoD' + date + '.jpg'

    if choice == 1:
        bing_wallpaper_changer.change_wp(wp_bing, SHOW_DEBUG)

    else:   
        pod_wallpaper_changer.change_wp(wp_pod, SHOW_DEBUG)