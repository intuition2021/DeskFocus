import ast
import time
from datetime import datetime as dt
from datetimerange import DateTimeRange

file = open("sysInfo.txt")
sysInfo = ast.literal_eval(file.read())

daysNeeded = sysInfo["days"]
timeStamp = sysInfo["time"]

redirect = "127.0.0.1"
today = dt.today().date().strftime('%A')

date = dt.now()

startTime = ""
endTime = ""
time_range = ""

timeStrStart = sysInfo["time"][today][0]
timeStrEnd = sysInfo["time"][today][1]

if today in daysNeeded:
    day = int(date.strftime("%d"))
    month = int(date.strftime("%m"))
    year = int(date.strftime("%Y"))

    timeObjStart = dt.strptime(timeStrStart, '%H:%M')
    timeObjEnd = dt.strptime(timeStrEnd, '%H:%M')

    startTime = timeObjStart.replace(year=year, month=month, day=day)
    endTime = timeObjEnd.replace(year=year, month=month, day=day)

    time_range = DateTimeRange(startTime, endTime)

myhost = sysInfo["system"]

while True:
    while today in daysNeeded and dt.now() in time_range:
        with open(myhost, 'r+') as myhostfile:
            hosts = myhostfile.read()
            for site in sysInfo["blockSites"]:
                if site not in hosts:
                    myhostfile.write(redirect + ' ' + site + '\n')

    with open(myhost, 'r+') as myhostfile:
        hosts = myhostfile.readlines()
        myhostfile.seek(0)
        for host in hosts:
            if not any(site in host for site in sysInfo["blockSites"]):
                myhostfile.write(host)
        myhostfile.truncate()

    time.sleep(10)
