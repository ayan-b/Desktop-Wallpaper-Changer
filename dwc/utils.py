import os
import sys
import urllib
from urllib.request import urlretrieve

from PIL import Image

from dwc.balloontip import balloon_tip
from dwc.debug import print_download_status


def save_image(url, picPath, SHOW_DEBUG):
    try:
        if SHOW_DEBUG:
            urlretrieve(url, picPath, print_download_status)
        else:
            urlretrieve(url, picPath)
    except urllib.error.URLError:
        raise urllib.error.URLError(
            "Seems something is wrong. If you think this should have not "
            "occurred, please report the bug in "
            "https://github.com/ayan-b/Desktop-Wallpaper-Changer"
        )
    except ConnectionAbortedError:
        os.remove(picPath)
        raise ConnectionAbortedError(
            "Please check your internet connection"
        )
    except Exception:
        if os.path.isfile(picPath):
            os.remove(picPath)
        raise Exception(
            "Some error occurred. If you think this should have not occurred, "
            "please report the bug in "
            "https://github.com/ayan-b/Desktop-Wallpaper-Changer"
        )
    if SHOW_DEBUG:
        print('URL retrieved')
    picData = Image.open(picPath)
    if SHOW_DEBUG:
        print('Image opened')
    picData.save(picPath)
    if SHOW_DEBUG:
        print('Saving ...')
    return picPath


def set_wallpaper_permanent(picPath, SHOW_DEBUG):
    if SHOW_DEBUG:
        print('Setting the wallpaper')
    if sys.platform.startswith('win32'):
        import win32gui

        win32gui.SystemParametersInfo(0x0014, picPath, 1+2)
        balloon_tip("Desktop Wallpaper Changer", "Wallpaper Updated!")
    elif sys.platform.startswith('linux'):
        from gi.repository import Gio

        gsettings = Gio.Settings.new('org.gnome.desktop.background')
        gsettings.set_string('picture-uri', "file://" + picPath)
        gsettings.apply()
    else:
        raise(
            "Sorry, your platform is not supported yet. Please open "
            "an issue in the GitHub issue tracker"
        )
