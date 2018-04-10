from PIL import Image

def save_image( picPath, SHOW_DEBUG ):
    picData = Image.open(picPath)
    if SHOW_DEBUG:
        print ('Image opened')
    picData.save(picPath)
    if SHOW_DEBUG:
        print ('Saving ...')
    return picPath