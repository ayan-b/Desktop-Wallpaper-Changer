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

import requests
from urllib.request import urlopen, urlretrieve
from xml.dom import minidom
from os import path
import pathlib
import datetime

from set_wallpaper_permanent import set_wallpaper_permanent
from debug import print_download_status
from save_image import save_image
from get_url import get_url

#get today's date
date = str(datetime.date.today())

def picpath_bing(xmldoc, saveDir, SHOW_DEBUG):
    #Parsing the XML File
    for element in xmldoc.getElementsByTagName('url'):
        if SHOW_DEBUG:
            print ('Getting URL for Bing')
        url = 'http://www.bing.com' + element.firstChild.nodeValue
        if SHOW_DEBUG:
            print ("Download from:%s" %url)
        #Get Current Date as fileName for the downloaded Picture
        picPath = saveDir  + 'bingwallpaper' + date +'.jpg'
        picPath = get_url (url, picPath, SHOW_DEBUG )
        picPath = save_image( picPath, SHOW_DEBUG )

    return picPath

def get_usock_bing(SHOW_DEBUG):
    i = 0
    while i<1:
        try:
            if SHOW_DEBUG:
                print ('Opening URL for Bing')
            usock = urlopen('http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-IN')
        except:
            i = 0
        else:
            i = 1
    return usock

def change_wp(wp_bing, saveDir, SHOW_DEBUG):
    if path.isfile(wp_bing)==True:
        if SHOW_DEBUG:
            print ('Picture already found, updating that only')
        set_wallpaper_permanent(wp_bing, SHOW_DEBUG)
    else:
        if SHOW_DEBUG:
            print ('Picture is not in the system, updating process starts ...')
        usock = get_usock_bing(SHOW_DEBUG)   
        xmldoc = minidom.parse(usock)
        picPath_bing = picpath_bing(xmldoc, saveDir, SHOW_DEBUG)
        set_wallpaper_permanent(picPath_bing, SHOW_DEBUG)
