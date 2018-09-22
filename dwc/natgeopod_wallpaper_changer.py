import datetime
from os import path

import requests

from debug import print_download_status
from utils import save_image, set_wallpaper_permanent

date = datetime.date.today()


def get_photourl():
    url = 'https://www.nationalgeographic.com/photography/photo-of-the-day/\
_jcr_content/.gallery.'
    month = str(date.month)
    year = str(date.year)
    if date.month < 10:
        month = '0' + month
    url = url + year + '-' + month + '.json'
    source = requests.get(url)
    if source.status_code == 200:
        source_code = source.json()
        if 'items' in source_code:
            photo = source_code['items'][0]
            photo_url = photo['url'] + photo['sizes']['2048']
            return str(photo_url)


def picpath_natgeo_pod(saveDir, SHOW_DEBUG):
    photo_url = get_photourl()
    natgeo_pod_path = saveDir + 'NatGeo_PoD' + str(date) + '.jpg'
    if SHOW_DEBUG:
        print("Download from: ", photo_url)

    savelink = save_image(photo_url, natgeo_pod_path, SHOW_DEBUG)

    return savelink


def change_wp(wp_natgeo_pod, saveDir, SHOW_DEBUG):

    if path.isfile(wp_natgeo_pod) is True:
        if SHOW_DEBUG:
            print('Nat Geo PoD Picture already found, updating that only')
        set_wallpaper_permanent(wp_natgeo_pod, SHOW_DEBUG)

    else:
        if SHOW_DEBUG:
            print('Picture is not in the system, updating process starts ...')
        savelink = picpath_natgeo_pod(saveDir, SHOW_DEBUG)
        set_wallpaper_permanent(savelink, SHOW_DEBUG)
