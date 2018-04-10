import urllib
from urllib.request import urlopen, urlretrieve
import os

from debug import print_download_status
from save_image import save_image

def get_url(url, picPath, SHOW_DEBUG):

    try:
        if SHOW_DEBUG:
            urlretrieve(url, picPath, print_download_status)
        else:
            urlretrieve(url, picPath)

    except urllib.error.HTTPError as e:
        print('HTTPError: %s. Exiting' % (str(e)))
        exit()

    except urllib.error.URLError as e:
        print('URLError: %s. Exiting' % (str(e)))
        os.remove(picPath)
        exit()

    except ConnectionAbortedError as e:
        print('ConnectionAbortedError: %s. Exiting' % (str(e)))
        os.remove(picPath)
        exit()

    except Exception as e:
        print ('Some error occurred: %s. Exiting' % (str(e)))
        if os.path.isfile(picPath):
            os.remove(picPath)
        exit()

        
    if SHOW_DEBUG:
        print ('URL retrieved')

    return picPath