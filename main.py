# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import ctypes

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyDictionary import PyDictionary
import logging
from threading import Thread
import time
import sys
import os

dictonary_options_list = ["definition", "synonym", "antonym"]

class Ui_MainWindow(object):

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

        # _translate = QtCore.QCoreApplication.translate
        # self.timerRunning = True
        #
        # if self.timerPaused:
        #     self.timerPaused = False
        # else:
        #     self.timeRequired = int(self.spinBox_pom_min.text()) * 60

        # child = os.fork()
        #
        # if child == 0:
        #     self.timerCountingDown()

        # # # Thread execution point
        # print("Launching a worker thread...")
        # if self.thread is not None:
        #     self.thread.join()
        #     print("thread joined")
        #
        # self.label_current_time.setText(_translate("MainWindow", "what"))
        #
        # if not self.threadRunning:
        #     self.thread = Thread(target=self.timerCountingDown(), args=())
        #     self.thread.daemon = True
        #     self.thread.start()
        #     print("Launched!")

    # obeslete function
    # def timerCountingDown(self):
    #     _translate = QtCore.QCoreApplication.translate
    #     print("timer is counting down")
    #     while self.timerRunning:
    #         print("timer entered while")
    #         self.label_current_time.setText(_translate("MainWindow", "Nice"))
    #         if self.timerPaused:
    #             print("stuck in paused")
    #             continue
    #         elif self.timeRequired:
    #             mins, secs = divmod(self.timeRequired, 60)
    #             hours, mins = divmod(mins, 60)
    #             timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
    #             print(timer)
    #             self.label_current_time.setText(_translate("MainWindow", timer))
    #             self.timeRequired -= 5
    #             print("tick")
    #         else:
    #             print("times up!")
    #             self.timerRunning = False
    #             break
    #
    #         time.sleep(5)

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
        self.label_blocklist = QtWidgets.QLabel(self.tab_webblocker)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_blocklist.setFont(font)
        self.label_blocklist.setAlignment(QtCore.Qt.AlignCenter)
        self.label_blocklist.setObjectName("label_blocklist")
        self.gridLayout_5.addWidget(self.label_blocklist, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_webblocker)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButton_web_update = QtWidgets.QPushButton(self.tab_webblocker)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_web_update.setFont(font)
        self.pushButton_web_update.setObjectName("pushButton_web_update")
        self.gridLayout_5.addWidget(self.pushButton_web_update, 8, 0, 1, 2)
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
        self.timeEdit = QtWidgets.QTimeEdit(self.tab_webblocker)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_5.addWidget(self.timeEdit, 2, 1, 1, 2)
        self.comboBox_webday_dropdown = QtWidgets.QComboBox(self.tab_webblocker)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_webday_dropdown.setFont(font)
        self.comboBox_webday_dropdown.setObjectName("comboBox_webday_dropdown")
        self.gridLayout_5.addWidget(self.comboBox_webday_dropdown, 1, 1, 1, 1)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.tab_webblocker)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeEdit_2.setFont(font)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.gridLayout_5.addWidget(self.timeEdit_2, 4, 1, 1, 2)
        self.plainTextEdit_sites = QtWidgets.QPlainTextEdit(self.tab_webblocker)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.plainTextEdit_sites.setFont(font)
        self.plainTextEdit_sites.setObjectName("plainTextEdit_sites")
        self.gridLayout_5.addWidget(self.plainTextEdit_sites, 7, 1, 1, 1)
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

        # # to do list tab
        # self.tab_todo = QtWidgets.QWidget()
        # self.tab_todo.setObjectName("tab_todo")
        #
        # self.gridLayout = QtWidgets.QGridLayout(self.tab_todo)
        # self.gridLayout.setObjectName("gridLayout")
        #
        # self.spinBox_index_selector_delete = QtWidgets.QSpinBox(self.tab_todo)
        # self.spinBox_index_selector_delete.setMinimum(1)
        # self.spinBox_index_selector_delete.setObjectName("spinBox_index_selector_delete")
        # self.gridLayout.addWidget(self.spinBox_index_selector_delete, 5, 3, 1, 1)
        #
        # self.label_8 = QtWidgets.QLabel(self.tab_todo)
        # self.label_8.setObjectName("label_8")
        # self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        #
        # self.lineEdit_addtask = QtWidgets.QLineEdit(self.tab_todo)
        # self.lineEdit_addtask.setObjectName("lineEdit_addtask")
        # self.gridLayout.addWidget(self.lineEdit_addtask, 0, 3, 1, 1)
        #
        # self.dateEdit_duedaete = QtWidgets.QDateEdit(self.tab_todo)
        # self.dateEdit_duedaete.setObjectName("dateEdit_duedaete")
        # self.gridLayout.addWidget(self.dateEdit_duedaete, 2, 3, 1, 1)
        #
        # self.label_7 = QtWidgets.QLabel(self.tab_todo)
        # self.label_7.setObjectName("label_7")
        # self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        #
        # self.spinBox_priority = QtWidgets.QSpinBox(self.tab_todo)
        # self.spinBox_priority.setMinimum(1)
        # self.spinBox_priority.setMaximum(5)
        # self.spinBox_priority.setObjectName("spinBox_priority")
        # self.gridLayout.addWidget(self.spinBox_priority, 3, 3, 1, 1)
        #
        # self.pushButton_addtask = QtWidgets.QPushButton(self.tab_todo)
        # self.pushButton_addtask.setObjectName("pushButton_addtask")
        # self.gridLayout.addWidget(self.pushButton_addtask, 3, 4, 1, 1)
        #
        # self.label_10 = QtWidgets.QLabel(self.tab_todo)
        # self.label_10.setObjectName("label_10")
        # self.gridLayout.addWidget(self.label_10, 5, 1, 1, 1)
        #
        # self.pushButton_completedtask = QtWidgets.QPushButton(self.tab_todo)
        # self.pushButton_completedtask.setObjectName("pushButton_completedtask")
        # self.gridLayout.addWidget(self.pushButton_completedtask, 5, 4, 1, 1)
        #
        # self.scrollArea_listtasks = QtWidgets.QScrollArea(self.tab_todo)
        # self.scrollArea_listtasks.setWidgetResizable(True)
        # self.scrollArea_listtasks.setObjectName("scrollArea_listtasks")
        # self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 516, 184))
        # self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        # self.scrollArea_listtasks.setWidget(self.scrollAreaWidgetContents_2)
        # self.gridLayout.addWidget(self.scrollArea_listtasks, 4, 1, 1, 4)
        #
        # self.label_9 = QtWidgets.QLabel(self.tab_todo)
        # self.label_9.setObjectName("label_9")
        # self.gridLayout.addWidget(self.label_9, 2, 1, 1, 1)
        #
        # self.label_11 = QtWidgets.QLabel(self.tab_todo)
        # self.label_11.setObjectName("label_11")
        # self.gridLayout.addWidget(self.label_11, 6, 1, 1, 1)
        #
        # self.progressBar = QtWidgets.QProgressBar(self.tab_todo)
        # self.progressBar.setProperty("value", 3)
        # self.progressBar.setObjectName("progressBar")
        # self.gridLayout.addWidget(self.progressBar, 6, 2, 1, 3)
        #
        # self.tabWidget.addTab(self.tab_todo, "")

        # # about us tab
        # self.tab_about_us = QtWidgets.QWidget()
        # self.tab_about_us.setObjectName("tab_about_us")
        # self.tabWidget.addTab(self.tab_about_us, "")

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
        self.label_blocklist.setText(_translate("MainWindow", "BlockList"))
        self.label_2.setText(_translate("MainWindow", "Start blocking"))
        self.pushButton_web_update.setText(_translate("MainWindow", "Update"))
        self.label_6.setText(_translate("MainWindow", "Day"))
        self.label_3.setText(_translate("MainWindow", "End blocking"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "HH:mm "))
        self.timeEdit_2.setDisplayFormat(_translate("MainWindow", "HH:mm "))
        self.plainTextEdit_sites.setPlainText(_translate("MainWindow", "www.facebook.com"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_webblocker), _translate("MainWindow", "WebBlocker"))
        self.lineEdit_dictsearch_2.setToolTip(_translate("MainWindow", "enter word here"))
        self.pushButton_dictsearch.setText(_translate("MainWindow", "Search"))
        self.label_lookup_2.setText(_translate("MainWindow", "Look up"))
        self.label_dictresult.setText(_translate("MainWindow", "Nothing to see :)"))
        self.label_result_2.setText(_translate("MainWindow", "Result"))
        self.label_searchtern_2.setText(_translate("MainWindow", "Search term"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dictionary), _translate("MainWindow", "Dictionary"))
        # self.label_8.setText(_translate("MainWindow", "Priority"))
        # self.label_7.setText(_translate("MainWindow", "Task"))
        # self.pushButton_addtask.setText(_translate("MainWindow", "Add Task"))
        # self.label_10.setText(_translate("MainWindow", "Index"))
        # self.pushButton_completedtask.setText(_translate("MainWindow", "Completed!"))
        # self.label_9.setText(_translate("MainWindow", "Due Date"))
        # self.label_11.setText(_translate("MainWindow", "Almost there!"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_todo), _translate("MainWindow", "Todo"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_about_us), _translate("MainWindow", "About Us"))

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
    # MainWindow.hide()

    # # SplashScreenWindow
    # splash_screen_window = SplashScreenWindow(MainWindow)
    # splash_screen_window.show()
    # QTimer.singleShot(2500, splash_screen_window.close)

    # Run the application!
    sys.exit(app.exec_())



