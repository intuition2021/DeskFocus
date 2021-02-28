# -*- coding: utf-8 -*-

import ast
import ctypes
import json
import logging
import os
import sys

from PyDictionary import PyDictionary
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

dictonary_options_list = ["definition", "synonym", "antonym"]

dayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hourList = []
minList = []

for i in range(0, 24):
    strHr = str(i)
    if len(strHr) == 1:
        strHr = "0" + strHr

    hourList.append(strHr)

for i in range(0, 60):
    strMin = str(i)
    if len(strMin) == 1:
        strMin = "0" + strMin

    minList.append(strMin)


def createSysInfo(daySelected, startTime, endTime):
    systemInfo = {}

    systemInfo['system'] = r'/private/etc/hosts'

    # in GUI, create a text box for them to enter all the websites they want to block
    # then over here, parse the information -> make it a json
    blockSites = []

    file = open("blockSites.txt", "r")
    for f in file:
        f = f.strip()
        blockSites.append(f)

    systemInfo["blockSites"] = blockSites

    file = open("sysInfo.txt")

    daysNeeded = []
    timeStamp = {}

    if os.stat("sysInfo.txt").st_size != 0:
        sysInfo = ast.literal_eval(file.read())
        systemInfo["days"] = sysInfo["days"]
        systemInfo["time"] = sysInfo["time"]
        daysNeeded = systemInfo["days"]
        timeStamp = systemInfo["time"]

    if daySelected not in daysNeeded:
        daysNeeded.append(daySelected)
        systemInfo["days"] = daysNeeded

    #if daySelected not in timeStamp:
    timeStamp[daySelected] = [startTime, endTime]
    systemInfo["time"] = timeStamp

    newFile = json.dumps(systemInfo, indent=4)
    with open("sysInfo.txt", "w") as x:
        x.write(newFile)

    bashCommand = "sudo python blocker.py"

    child = os.fork()

    if child == 0:
        os.system(bashCommand)

class Ui_MainWindow(object):

    def on_click_blocker_btn(self):
        # Add the days in the week
        # self.comboBox_webday_dropdown.addItems(dayList)

        # Get information for blocker
        daySelected = self.comboBox_webday_dropdown.currentText()
        startTime = self.comboBox_starthr.currentText() + ":" + self.comboBox_startmin.currentText()
        endTime = self.comboBox_stophr.currentText() + ":" + self.comboBox_stopmin.currentText()

        blockSites = self.plainTextEdit_sites.toPlainText()

        file = open("blockSites.txt", "w+")
        file.write(blockSites)
        file.close()

        print("things: {} {} {} {}".format(daySelected, startTime, endTime, blockSites))

        createSysInfo(daySelected, startTime, endTime)

        #worker = threading.Thread(target=createSysInfo(daySelected, startTime, endTime), args=(1,))
        #worker.start()

    def toggleStudy(self):
        _translate = QtCore.QCoreApplication.translate
        if (self.isStudy):
            self.isStudy = False
            self.pushButton_study_toggle.setText(_translate("MainWindow", "Relaxing"))
        else:
            self.isStudy = True
            self.pushButton_study_toggle.setText(_translate("MainWindow", "Studying"))

    def startTimer(self):
        self.flagTimer = True
        self.msgDelievered = False

    def pauseTimer(self):
        print("Timer paused!")
        self.flagTimer = False
        # self.timerPaused = True

    def stopTimer(self):
        print("Timer stopped!")
        self.flagTimer = False
        self.timeRequired = int(self.spinBox_pom_min.text()) * 60
        self.label_current_time
        # self.timerRunning = False

    # method called by timer
    def showTime(self):
        # checking if flag is true
        if (self.flagTimer and self.timeRequired != 0):
            # decrement the counter
            self.timeRequired -= 1

        # getting text from count
        mins, secs = divmod(self.timeRequired, 60)
        hours, mins = divmod(mins, 60)
        text = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        # text = str(self.timeRequired / 10)

        # showing text
        self.label_current_time.setText(text)

        if ((self.timeRequired == 0) and (self.msgDelievered == False)):
            self.timesUpMsg = QtWidgets.QMessageBox()
            self.timesUpMsg.resize(300, 250)
            self.timesUpMsg.setWindowTitle("Times Up!")

            if (self.isStudy):
                self.timesUpMsg.setText("Time for a break!")
            else:
                self.timesUpMsg.setText("Get back to work!")
            x = self.timesUpMsg.exec_()
            self.msgDelievered = True

    def searchForWord(self):
        _translate = QtCore.QCoreApplication.translate
        word = self.lineEdit_dictsearch_2.text()
        search_param = str(self.comboBox_lookup_2.currentText())

        if (word == ""):
            self.label_dictresult.setText(_translate("MainWindow", "Enter search term!"))
            return

        dictionary = PyDictionary()

        print(dictionary.meaning(word))

        self.label_dictresult.setText(_translate("MainWindow", "moretext"))

        if (search_param == "definition"):
            self.label_dictresult.setText(_translate("MainWindow", str(dictionary.meaning(word))))
        elif (search_param == "synonym"):
            self.label_dictresult.setText(_translate("MainWindow", str(dictionary.synonym(word))))
        else:
            self.label_dictresult.setText(_translate("MainWindow", str(dictionary.antonym(word))))


    def setupUi(self, MainWindow):
        self.thread = None
        self.threadRunning = False
        self.timerRunning = False
        self.timerPaused = False
        self.timeRequired = 5*60
        self.flagTimer = False
        self.msgDelievered = True

        myappid = u'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 454)
        MainWindow.setWindowIcon(QtGui.QIcon(".images/DeskFocus.ico"))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")

        # pomodoro tab
        self.tab_pomodoro = QtWidgets.QWidget()
        self.tab_pomodoro.setObjectName("tab_pomodoro")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_pomodoro)
        self.gridLayout_6.setObjectName("gridLayout_6")

        # minutes selection box
        self.spinBox_pom_min = QtWidgets.QSpinBox(self.tab_pomodoro)
        self.spinBox_pom_min.setMinimum(5)
        self.spinBox_pom_min.setMaximum(200)
        self.spinBox_pom_min.setSingleStep(5)
        self.spinBox_pom_min.setObjectName("spinBox_pom_min")
        self.gridLayout_6.addWidget(self.spinBox_pom_min, 0, 1, 1, 1)

        # current time label
        self.label_current_time = QtWidgets.QLabel(self.tab_pomodoro)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(40)
        self.label_current_time.setFont(font)
        self.label_current_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_time.setObjectName("label_current_time")
        self.gridLayout_6.addWidget(self.label_current_time, 2, 0, 1, 2)

        # pause button
        self.pb_pause = QtWidgets.QPushButton(self.tab_pomodoro)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pb_pause.setFont(font)
        self.pb_pause.setObjectName("pb_pause")
        self.gridLayout_6.addWidget(self.pb_pause, 4, 0, 1, 2)

        # start button
        self.pb_start = QtWidgets.QPushButton(self.tab_pomodoro)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pb_start.setFont(font)
        self.pb_start.setObjectName("pb_start")
        self.gridLayout_6.addWidget(self.pb_start, 3, 0, 1, 2)

        # stop button
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_pomodoro)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_6.addWidget(self.pushButton_3, 5, 0, 1, 2)

        # start timer
        self.pb_start.pressed.connect(self.startTimer)
        # pause the timer
        self.pb_pause.pressed.connect(self.pauseTimer)
        # stop the timer
        self.pushButton_3.pressed.connect(self.stopTimer)

        # minutes word label
        self.label_min_pomo = QtWidgets.QLabel(self.tab_pomodoro)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_min_pomo.setFont(font)
        self.label_min_pomo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_min_pomo.setObjectName("label_min_pomo")
        self.gridLayout_6.addWidget(self.label_min_pomo, 0, 0, 1, 1)

        # study - relax toggle button
        self.isStudy = True
        self.pushButton_study_toggle = QtWidgets.QPushButton(self.tab_pomodoro)
        self.pushButton_study_toggle.setObjectName("pushButton_study_toggle")
        self.gridLayout_6.addWidget(self.pushButton_study_toggle, 1, 0, 1, 2)

        # setting calling method by button
        self.pushButton_study_toggle.clicked.connect(self.toggleStudy)

        # creating a timer object
        self.timer = QTimer(self.tab_pomodoro)

        # adding action to timer
        self.timer.timeout.connect(self.showTime)

        self.timer.start(1000)

        self.tabWidget.addTab(self.tab_pomodoro, "")

        # web blocker tab
        self.tab_webblocker = QtWidgets.QWidget()
        self.tab_webblocker.setObjectName("tab_webblocker")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_webblocker)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBox_starthr = QtWidgets.QComboBox(self.tab_webblocker)
        self.comboBox_starthr.setObjectName("comboBox_starthr")
        self.gridLayout_5.addWidget(self.comboBox_starthr, 2, 1, 1, 1)

        self.comboBox_starthr.addItems(hourList)

        self.label_2 = QtWidgets.QLabel(self.tab_webblocker)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_webblocker)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_webblocker)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 4, 0, 1, 1)
        self.comboBox_startmin = QtWidgets.QComboBox(self.tab_webblocker)
        self.comboBox_startmin.setObjectName("comboBox_startmin")
        self.gridLayout_5.addWidget(self.comboBox_startmin, 2, 2, 1, 1)

        self.comboBox_startmin.addItems(minList)

        self.comboBox_webday_dropdown = QtWidgets.QComboBox(self.tab_webblocker)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_webday_dropdown.setFont(font)
        self.comboBox_webday_dropdown.setObjectName("comboBox_webday_dropdown")
        self.comboBox_webday_dropdown.addItems(dayList)
        self.gridLayout_5.addWidget(self.comboBox_webday_dropdown, 1, 1, 1, 2)
        self.plainTextEdit_sites = QtWidgets.QPlainTextEdit(self.tab_webblocker)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.plainTextEdit_sites.setFont(font)
        self.plainTextEdit_sites.setObjectName("plainTextEdit_sites")
        self.gridLayout_5.addWidget(self.plainTextEdit_sites, 5, 1, 1, 2)
        self.label_blocklist = QtWidgets.QLabel(self.tab_webblocker)
        self.label_blocklist.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_blocklist.setFont(font)
        self.label_blocklist.setAlignment(QtCore.Qt.AlignCenter)
        self.label_blocklist.setObjectName("label_blocklist")
        self.gridLayout_5.addWidget(self.label_blocklist, 5, 0, 1, 1)
        self.pushButton_web_update = QtWidgets.QPushButton(self.tab_webblocker)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_web_update.setFont(font)
        self.pushButton_web_update.setObjectName("pushButton_web_update")
        self.gridLayout_5.addWidget(self.pushButton_web_update, 8, 0, 1, 3)
        self.comboBox_stophr = QtWidgets.QComboBox(self.tab_webblocker)
        self.comboBox_stophr.setObjectName("comboBox_stophr")
        self.gridLayout_5.addWidget(self.comboBox_stophr, 4, 1, 1, 1)

        self.comboBox_stophr.addItems(hourList)

        self.comboBox_stopmin = QtWidgets.QComboBox(self.tab_webblocker)
        self.comboBox_stopmin.setObjectName("comboBox_stopmin")
        self.gridLayout_5.addWidget(self.comboBox_stopmin, 4, 2, 1, 1)

        self.comboBox_stopmin.addItems(minList)

        self.pushButton_web_update.clicked.connect(self.on_click_blocker_btn)

        self.tabWidget.addTab(self.tab_webblocker, "")

        # dictionary tab
        self.tab_dictionary = QtWidgets.QWidget()
        self.tab_dictionary.setObjectName("tab_dictionary")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_dictionary)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_dictionary_2 = QtWidgets.QGridLayout()
        self.gridLayout_dictionary_2.setObjectName("gridLayout_dictionary_2")
        self.lineEdit_dictsearch_2 = QtWidgets.QLineEdit(self.tab_dictionary)
        font = QtGui.QFont()
        font.setPointSize(10)

        self.lineEdit_dictsearch_2.setFont(font)
        self.lineEdit_dictsearch_2.setText("")
        self.lineEdit_dictsearch_2.setDragEnabled(True)
        self.lineEdit_dictsearch_2.setObjectName("lineEdit_dictsearch_2")
        self.gridLayout_dictionary_2.addWidget(self.lineEdit_dictsearch_2, 2, 1, 1, 1)

        self.pushButton_dictsearch = QtWidgets.QPushButton(self.tab_dictionary)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_dictsearch.setFont(font)
        self.pushButton_dictsearch.setObjectName("pushButton_dictsearch")
        self.gridLayout_dictionary_2.addWidget(self.pushButton_dictsearch, 3, 0, 1, 2)

        self.label_lookup_2 = QtWidgets.QLabel(self.tab_dictionary)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_lookup_2.setFont(font)
        self.label_lookup_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lookup_2.setObjectName("label_lookup_2")
        self.gridLayout_dictionary_2.addWidget(self.label_lookup_2, 1, 0, 1, 1)

        self.comboBox_lookup_2 = QtWidgets.QComboBox(self.tab_dictionary)
        self.comboBox_lookup_2.setObjectName("comboBox_lookup_2")
        self.gridLayout_dictionary_2.addWidget(self.comboBox_lookup_2, 1, 1, 1, 1)
        # add language list for original text
        self.comboBox_lookup_2.addItems(dictonary_options_list)

        self.label_dictresult = QtWidgets.QLabel(self.tab_dictionary)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dictresult.setFont(font)
        self.label_dictresult.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dictresult.setObjectName("label_dictresult")
        self.label_dictresult.setWordWrap(True)
        self.gridLayout_dictionary_2.addWidget(self.label_dictresult, 4, 1, 1, 1)

        self.label_result_2 = QtWidgets.QLabel(self.tab_dictionary)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_result_2.setFont(font)
        self.label_result_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result_2.setObjectName("label_result_2")
        self.gridLayout_dictionary_2.addWidget(self.label_result_2, 4, 0, 1, 1)

        self.label_searchtern_2 = QtWidgets.QLabel(self.tab_dictionary)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_searchtern_2.setFont(font)
        self.label_searchtern_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_searchtern_2.setObjectName("label_searchtern_2")
        self.gridLayout_dictionary_2.addWidget(self.label_searchtern_2, 2, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout_dictionary_2, 0, 0, 1, 1)

        # search for word if field not empty
        self.pushButton_dictsearch.clicked.connect(self.searchForWord)

        self.tabWidget.addTab(self.tab_dictionary, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DeskFocus"))
        self.label_current_time.setText(_translate("MainWindow", "00:05:00"))
        self.pb_pause.setText(_translate("MainWindow", "PAUSE"))
        self.pb_start.setText(_translate("MainWindow", "START"))
        self.pushButton_3.setText(_translate("MainWindow", "SET"))
        self.label_min_pomo.setText(_translate("MainWindow", "Minutes"))
        self.pushButton_study_toggle.setText(_translate("MainWindow", "Studying"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_pomodoro), _translate("MainWindow", "Pomodoro"))
        self.label_2.setText(_translate("MainWindow", "Start blocking"))
        self.label_6.setText(_translate("MainWindow", "Day"))
        self.label_3.setText(_translate("MainWindow", "End blocking"))
        self.plainTextEdit_sites.setPlainText(_translate("MainWindow", "www.facebook.com"))
        self.label_blocklist.setText(_translate("MainWindow", "BlockList"))
        self.pushButton_web_update.setText(_translate("MainWindow", "Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_webblocker),
                                  _translate("MainWindow", "WebBlocker"))
        self.lineEdit_dictsearch_2.setToolTip(_translate("MainWindow", "enter word here"))
        self.pushButton_dictsearch.setText(_translate("MainWindow", "Search"))
        self.label_lookup_2.setText(_translate("MainWindow", "Look up"))
        self.label_dictresult.setText(_translate("MainWindow", "Nothing to see :)"))
        self.label_result_2.setText(_translate("MainWindow", "Result"))
        self.label_searchtern_2.setText(_translate("MainWindow", "Search term"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dictionary), _translate("MainWindow", "Dictionary"))


    def closeEvent(self, event):
        self.stopTimer()

if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Run the application!
    sys.exit(app.exec_())

