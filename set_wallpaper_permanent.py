import win32gui

def set_wallpaper_permanent(picPath, SHOW_DEBUG):
    if SHOW_DEBUG:
        print ('Setting the wallpaper')
    win32gui.SystemParametersInfo(0x0014, picPath, 1+2)