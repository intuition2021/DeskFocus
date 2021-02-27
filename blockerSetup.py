import json

linux_sys = '/etc/hosts'
mac_sys = '/private/etc/hosts'
window_sys = r"C:\Windows\System32\drivers\etc\hosts"

chooseSystem = input("Please enter: 1 for Windows | 2 for Mac\n")
systemInfo = {}

while True:
    if chooseSystem == "1":
        systemInfo['system'] = window_sys
        break
    elif chooseSystem == "2":
        systemInfo['system'] = mac_sys
        break
    else:
        print("invalid")
        chooseSystem = input("Please enter: 1 for Windows | 2 for Mac\n")
        continue

# in GUI, create a text box for them to enter all the websites they want to block
# then over here, parse the information -> make it a json
blockSites = []

file = open("blockSites.txt", "r")
for f in file:
    f = f.strip()
    blockSites.append(f)

systemInfo["blockSites"] = blockSites

# in GUI, create bottoms, drag downs to set day and time
# date.weekday where 1 is Monday, ..., 7 is Sunday
systemInfo["days"] = ["Monday", "Saturday"]
systemInfo["time"] = {"Monday": ("16:00", "17:00"), "Saturday": ("16:00", "17:00")}

newFile = json.dumps(systemInfo, indent=4)
with open("sysInfo.txt", "w") as x:
    x.write(newFile)
x.close()
