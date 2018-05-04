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
import lib.natgeopod_wallpaper_changer

SHOW_DEBUG = True

#Directory to save images
if os.path.exists("F:")==True:
    saveDirBing = "F:\\WallPaper\\Bing\\"
    saveDirAPoD = "F:\\WallPaper\\APoD\\"
    saveDirUnsplash = "F:\\WallPaper\\Unsplash\\"
    saveDirSpace = "F:\\WallPaper\\Space\\"  
    saveDirNatGeoPoD = "F:\\WallPaper\\NatGeoPoD\\"

else:
    saveDirBing = os.path.join(os.getcwd(), r'WallPaper\\Bing\\')
    saveDirAPoD = os.path.join(os.getcwd(), r'WallPaper\\APoD\\')
    saveDirUnsplash = os.path.join(os.getcwd(), r'WallPaper\\Unsplash\\')
    saveDirSpace = os.path.join(os.getcwd(), r'WallPaper\\Space\\')
    saveDirNatGeoPoD = os.path.join(os.getcwd(), r'WallPaper\\NatGeoPoD\\')


date = datetime.date.today()

def directoryCheck ():
    #create the directory if it does not exist
    pathlib.Path(saveDirBing).mkdir(parents=True, exist_ok=True)
    pathlib.Path(saveDirAPoD).mkdir(parents=True, exist_ok=True)
    pathlib.Path(saveDirUnsplash).mkdir(parents=True, exist_ok=True)
    pathlib.Path(saveDirSpace).mkdir(parents=True, exist_ok=True)
    pathlib.Path(saveDirNatGeoPoD).mkdir(parents=True, exist_ok=True)

if __name__=='__main__':

    #only on windows 
    #add_to_startup()

    choice = 0
    directoryCheck()
    print ("Choice: ? 0: NASA Astronomy Picture of the Day, 1: Bing Image of the Day, 2: Random Pictures from Unsplash, 3: Space.com Image of the day, 4: National Geographic PoD ",)
    choice = int(input())
    wp_bing = saveDirBing  + 'bingwallpaper' + str(date) +'.jpg'
    wp_pod = saveDirAPoD + 'NASA_PoD' + str(date) + '.jpg'
    wp_unsplash = saveDirUnsplash + 'unsplash' + str(date) + '.jpg'
    wp_space = saveDirSpace + 'space' + str(date) + '.jpg'
    wp_natgeo_pod = saveDirNatGeoPoD + 'NatGeo_PoD' + str(date) + '.jpg'

    if choice == 1:
        lib.bing_wallpaper_changer.change_wp( wp_bing, saveDirBing, SHOW_DEBUG )

    elif choice == 0: 
        lib.pod_wallpaper_changer.change_wp( wp_pod, saveDirAPoD, SHOW_DEBUG, date )
    
    elif choice == 2:
        lib.unsplash_wallpaper_changer.change_wp( wp_unsplash, saveDirUnsplash, SHOW_DEBUG )

    elif choice == 3:
        print ('Under Development')
        #space_wallpaper_changer.change_wp( wp_space, saveDirSpace, SHOW_DEBUG )
    
    elif choice == 4:
        lib.natgeopod_wallpaper_changer.change_wp(wp_natgeo_pod, saveDirNatGeoPoD, SHOW_DEBUG)
