from os import getlogin, path

def add_to_startup(file_path=""):
    #link=https://stackoverflow.com/questions/4438020/how-to-start-a-python-file-while-windows-starts
    USER_NAME = getlogin()
    if file_path == "":
        file_path = path.dirname(path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)