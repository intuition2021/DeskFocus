# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import ast
import json
import os
import time
from datetime import datetime as dt
from datetimerange import DateTimeRange
from PyQt5 import QtCore, QtGui, QtWidgets

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

    systemInfo['system'] = r"C:\Windows\System32\drivers\etc\hosts"

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
    sysInfo = ""
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

    if daySelected not in timeStamp:
        timeStamp[daySelected] = [startTime, endTime]
        systemInfo["time"] = timeStamp

    newFile = json.dumps(systemInfo, indent=4)
    with open("sysInfo.txt", "w") as x:
        x.write(newFile)
    x.close()

def blocker():
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

        createSysInfo(daySelected, startTime, endTime)

        print("things: {} {} {} {}".format(daySelected, startTime, endTime, blockSites))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_pomodoro = QtWidgets.QWidget()
        self.tab_pomodoro.setObjectName("tab_pomodoro")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_pomodoro)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.spinBox_pom_min = QtWidgets.QSpinBox(self.tab_pomodoro)
        self.spinBox_pom_min.setMinimum(5)
        self.spinBox_pom_min.setMaximum(200)
        self.spinBox_pom_min.setSingleStep(5)
        self.spinBox_pom_min.setObjectName("spinBox_pom_min")
        self.gridLayout_6.addWidget(self.spinBox_pom_min, 0, 1, 1, 1)
        self.label_current_time = QtWidgets.QLabel(self.tab_pomodoro)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(40)
        self.label_current_time.setFont(font)
        self.label_current_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_time.setObjectName("label_current_time")
        self.gridLayout_6.addWidget(self.label_current_time, 2, 0, 1, 2)
        self.pb_pause = QtWidgets.QPushButton(self.tab_pomodoro)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pb_pause.setFont(font)
        self.pb_pause.setObjectName("pb_pause")
        self.gridLayout_6.addWidget(self.pb_pause, 4, 0, 1, 2)
        self.pb_start = QtWidgets.QPushButton(self.tab_pomodoro)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pb_start.setFont(font)
        self.pb_start.setObjectName("pb_start")
        self.gridLayout_6.addWidget(self.pb_start, 3, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_pomodoro)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_6.addWidget(self.pushButton_3, 5, 0, 1, 2)
        self.label_min_pomo = QtWidgets.QLabel(self.tab_pomodoro)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_min_pomo.setFont(font)
        self.label_min_pomo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_min_pomo.setObjectName("label_min_pomo")
        self.gridLayout_6.addWidget(self.label_min_pomo, 0, 0, 1, 1)
        self.pushButton_study_toggle = QtWidgets.QPushButton(self.tab_pomodoro)
        self.pushButton_study_toggle.setObjectName("pushButton_study_toggle")
        self.gridLayout_6.addWidget(self.pushButton_study_toggle, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_pomodoro, "")

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
        self.comboBox_lookup_2_ = QtWidgets.QComboBox(self.tab_dictionary)
        self.comboBox_lookup_2_.setObjectName("comboBox_lookup_2_")
        self.gridLayout_dictionary_2.addWidget(self.comboBox_lookup_2_, 1, 1, 1, 1)
        self.textBrowser_dictresult_2 = QtWidgets.QTextBrowser(self.tab_dictionary)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_dictresult_2.setFont(font)
        self.textBrowser_dictresult_2.setObjectName("textBrowser_dictresult_2")
        self.gridLayout_dictionary_2.addWidget(self.textBrowser_dictresult_2, 4, 1, 1, 1)
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
        self.tabWidget.addTab(self.tab_dictionary, "")
        self.tab_todo = QtWidgets.QWidget()
        self.tab_todo.setObjectName("tab_todo")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_todo)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_index_selector_delete = QtWidgets.QSpinBox(self.tab_todo)
        self.spinBox_index_selector_delete.setMinimum(1)
        self.spinBox_index_selector_delete.setObjectName("spinBox_index_selector_delete")
        self.gridLayout.addWidget(self.spinBox_index_selector_delete, 5, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_todo)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.lineEdit_addtask = QtWidgets.QLineEdit(self.tab_todo)
        self.lineEdit_addtask.setObjectName("lineEdit_addtask")
        self.gridLayout.addWidget(self.lineEdit_addtask, 0, 3, 1, 1)
        self.dateEdit_duedaete = QtWidgets.QDateEdit(self.tab_todo)
        self.dateEdit_duedaete.setObjectName("dateEdit_duedaete")
        self.gridLayout.addWidget(self.dateEdit_duedaete, 2, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_todo)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        self.spinBox_priority = QtWidgets.QSpinBox(self.tab_todo)
        self.spinBox_priority.setMinimum(1)
        self.spinBox_priority.setMaximum(5)
        self.spinBox_priority.setObjectName("spinBox_priority")
        self.gridLayout.addWidget(self.spinBox_priority, 3, 3, 1, 1)
        self.pushButton_addtask = QtWidgets.QPushButton(self.tab_todo)
        self.pushButton_addtask.setObjectName("pushButton_addtask")
        self.gridLayout.addWidget(self.pushButton_addtask, 3, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_todo)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 1, 1, 1)
        self.pushButton_completedtask = QtWidgets.QPushButton(self.tab_todo)
        self.pushButton_completedtask.setObjectName("pushButton_completedtask")
        self.gridLayout.addWidget(self.pushButton_completedtask, 5, 4, 1, 1)
        self.scrollArea_listtasks = QtWidgets.QScrollArea(self.tab_todo)
        self.scrollArea_listtasks.setWidgetResizable(True)
        self.scrollArea_listtasks.setObjectName("scrollArea_listtasks")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 516, 184))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_listtasks.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea_listtasks, 4, 1, 1, 4)
        self.label_9 = QtWidgets.QLabel(self.tab_todo)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_todo)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.tab_todo)
        self.progressBar.setProperty("value", 3)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 6, 2, 1, 3)
        self.tabWidget.addTab(self.tab_todo, "")
        self.tab_about_us = QtWidgets.QWidget()
        self.tab_about_us.setObjectName("tab_about_us")
        self.tabWidget.addTab(self.tab_about_us, "")
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
        self.label_current_time.setText(_translate("MainWindow", "CURRENT TIME"))
        self.pb_pause.setText(_translate("MainWindow", "PAUSE"))
        self.pb_start.setText(_translate("MainWindow", "START"))
        self.pushButton_3.setText(_translate("MainWindow", "STOP"))
        self.label_min_pomo.setText(_translate("MainWindow", "Minutes"))
        self.pushButton_study_toggle.setText(_translate("MainWindow", "Study"))
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
        self.textBrowser_dictresult_2.setHtml(_translate("MainWindow",
                                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_result_2.setText(_translate("MainWindow", "Result"))
        self.label_searchtern_2.setText(_translate("MainWindow", "Search term"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dictionary),
                                  _translate("MainWindow", "Dictionary"))
        self.label_8.setText(_translate("MainWindow", "Priority"))
        self.label_7.setText(_translate("MainWindow", "Task"))
        self.pushButton_addtask.setText(_translate("MainWindow", "Add Task"))
        self.label_10.setText(_translate("MainWindow", "Index"))
        self.pushButton_completedtask.setText(_translate("MainWindow", "Completed!"))
        self.label_9.setText(_translate("MainWindow", "Due Date"))
        self.label_11.setText(_translate("MainWindow", "Almost there!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_todo), _translate("MainWindow", "Todo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_about_us), _translate("MainWindow", "About Us"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

