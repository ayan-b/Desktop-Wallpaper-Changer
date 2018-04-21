import win32gui

from lib.balloontip import balloon_tip

def set_wallpaper_permanent(picPath, SHOW_DEBUG):
    if SHOW_DEBUG:
        print ('Setting the wallpaper')
    win32gui.SystemParametersInfo(0x0014, picPath, 1+2)
    balloon_tip("Desktop Wallpaper Changer", "Wallpaper Updated!")