# import sys
#
# from PyQt5 import QtCore
#
#
# def timerEvent():
#     global time
#     time = time.addSecs(1)
#     print(time.toString("hh:mm:ss"))
#
#
# app = QtCore.QCoreApplication(sys.argv)
#
# timer = QtCore.QTimer()
# time = QtCore.QTime(0, 0, 0)
#
# timer.timeout.connect(timerEvent)
# timer.start(1000)
#
# sys.exit(app.exec_())



# import the time module
import time


# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer)
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))