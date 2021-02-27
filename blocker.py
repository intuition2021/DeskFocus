import ast
import time
from datetime import datetime as dt

file = open("sysInfo.txt")
sysInfo = ast.literal_eval(file.read())

daysNeeded = sysInfo["days"]
timeStamp = sysInfo["time"]

#timeStrStart = sysInfo["time"][0]
#timeObjStart = dt.strptime(timeStrStart, '%H:%M')

redirect = "127.0.0.1"
today = dt.today().date().strftime('%A')

while today in daysNeeded:
    with open(sysInfo["system"], 'r+') as file:
        content = file.read()
    for website in sysInfo["blockSites"]:
        if website in content:
            pass
        else:
            file.write(redirect + " " + website + "\n")

    time.sleep(10)