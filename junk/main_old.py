# -*- coding: utf-8 -*-


######## imports ########

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, \
    QSpacerItem, QStatusBar, QTextBrowser
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot, QMetaObject, QCoreApplication

from PyDictionary import PyDictionary

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget

import tkinter as tk


######## Constants ########

dictonary_options_list = ["definition", "synonym", "antonym"]


######## Class for the main window ########

class Ui_MainWsindow(object):
    # def get_dimensions(self):
    #     root = tk.Tk()
    #     self.screen_width = root.winfo_screenwidth()
    #     self.screen_height = root.winfo_screenheight()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 275)
        MainWindow.setWindowIcon(QtGui.QIcon("../images/DeskTranslate.ico")) # todo change this
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 25, 200, 200))
        self.label.setMinimumSize(QtCore.QSize(200, 200))
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setObjectName("label")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        #        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 431, 251))
        self.tabWidget.setObjectName("tabWidget")

        self.gridLayout_dictionary = QGridLayout()
        self.gridLayout_dictionary.setObjectName("gridLayout_dictionary")
        self.lineEdit_dictsearch = QLineEdit(self.centralwidget_dict)
        self.lineEdit_dictsearch.setObjectName("lineEdit_dictsearch")
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_dictsearch.setFont(font)
        self.lineEdit_dictsearch.setDragEnabled(True)

        self.gridLayout_dictionary.addWidget(self.lineEdit_dictsearch, 1, 1, 1, 1)

        self.label_lookup = QLabel(self.centralwidget_dict)
        self.label_lookup.setObjectName("label_lookup")
        self.label_lookup.setFont(font)
        self.label_lookup.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_dictionary.addWidget(self.label_lookup, 0, 0, 1, 1)

        self.textBrowser_dictresult = QTextBrowser(self.centralwidget_dict)
        self.textBrowser_dictresult.setObjectName("textBrowser_dictresult")
        self.textBrowser_dictresult.setFont(font)

        self.gridLayout_dictionary.addWidget(self.textBrowser_dictresult, 3, 1, 1, 1)

        self.comboBox_lookup = QComboBox(self.centralwidget_dict)
        self.comboBox_lookup.setObjectName("comboBox_lookup")

        self.gridLayout_dictionary.addWidget(self.comboBox_lookup, 0, 1, 1, 1)

        self.label_searchtern = QLabel(self.centralwidget_dict)
        self.label_searchtern.setObjectName("label_searchtern")
        self.label_searchtern.setFont(font)
        self.label_searchtern.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_dictionary.addWidget(self.label_searchtern, 1, 0, 1, 1)

        self.label_result = QLabel(self.centralwidget_dict)
        self.label_result.setObjectName("label_result")
        self.label_result.setFont(font)
        self.label_result.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_dictionary.addWidget(self.label_result, 3, 0, 1, 1)

        self.verticalSpacer_dict = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_dictionary.addItem(self.verticalSpacer_dict, 2, 1, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_dictionary, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget_dict)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        # if QT_CONFIG(tooltip)
        self.lineEdit_dictsearch.setToolTip(QCoreApplication.translate("MainWindow", "enter word here", None))
        # endif // QT_CONFIG(tooltip)
        self.lineEdit_dictsearch.setText("")
        self.label_lookup.setText(QCoreApplication.translate("MainWindow", "Look up", None))
        self.textBrowser_dictresult.setHtml(QCoreApplication.translate("MainWindow",
                                                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                       "p,"
                                                                       "li { white-space: pre-wrap; }\n"
                                                                       "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                                       "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                                       None))
        self.label_searchtern.setText(QCoreApplication.translate("MainWindow", "Search term", None))
        self.label_result.setText(QCoreApplication.translate("MainWindow", "result", None))
    # retranslateUi


        # self.layout = QVBoxLayout(self)
        #
        # # Initialize tab screen
        # self.tabs = QTabWidget()
        # self.tab_dictionary = QWidget()
        # self.tab_tasklist = QWidget()
        # self.tabs.resize(300, 200)
        #
        # # Add tabs
        # self.tabs.addTab(self.tab_dictionary, "📖 Dictionary")
        # self.tabs.addTab(self.tab_tasklist, "🗎 Task List")
        #
        # # Create first tab
        # self.tab_dictionary.layout = QVBoxLayout(self)
        # self.pushButton1 = QPushButton("PyQt5 button")
        # self.tab_dictionary.layout.addWidget(self.pushButton1)
        # self.tab_dictionary.setLayout(self.tab_dictionary.layout)
        #
        # MyTableWidget.createDictionaryBox(MainWindow)
        #
        # # Add tabs to widget
        # self.layout.addWidget(self.tabs)
        # self.setLayout(self.layout)



        # self.get_dimensions()
        #
        # self.title = 'DeskFocus'
        # self.left = 0
        # self.top = 0
        # self.width = self.screen_width/4
        # self.height = self.screen_height/4
        # self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        #
        # self.table_widget = MyTableWidget(self, MainWindow)
        # self.setCentralWidget(self.table_widget)
        #
        # qtRectangle = self.frameGeometry()
        # centerPoint = QDesktopWidget().availableGeometry().center()
        # qtRectangle.moveCenter(centerPoint)
        # self.move(qtRectangle.topLeft())
        # qtRectangle = self.frameGeometry()
        # centerPoint = QDesktopWidget().availableGeometry().center()
        # qtRectangle.moveCenter(centerPoint)
        # self.move(qtRectangle.topLeft())
        #
        # self.show()

######## Tab widget within main window ########

class MyTableWidget(QWidget):

    def __init__(self, parent, MainWindow):
        super(QWidget, self).__init__(parent)

        ## Widget gallery style (use for settings)
        # self.originalPalette = QApplication.palette()
        #
        # styleComboBox = QComboBox()
        # styleComboBox.addItems(QStyleFactory.keys())
        #
        # styleLabel = QLabel("&Style:")
        # styleLabel.setBuddy(styleComboBox)
        #
        # self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
        # self.useStylePaletteCheckBox.setChecked(True)




    def createDictionaryBox(self, MainWindow):
        self.centralwidget_dict = QWidget(MainWindow)
        self.centralwidget_dict.setObjectName("centralwidget_dict")
        self.gridLayout = QGridLayout(self.centralwidget_dict)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_dictionary = QGridLayout()
        self.gridLayout_dictionary.setObjectName("gridLayout_dictionary")
        self.lineEdit_dictsearch = QLineEdit(self.centralwidget_dict)
        self.lineEdit_dictsearch.setObjectName("lineEdit_dictsearch")
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_dictsearch.setFont(font)
        self.lineEdit_dictsearch.setDragEnabled(True)

        self.gridLayout_dictionary.addWidget(self.lineEdit_dictsearch, 1, 1, 1, 1)

        self.label_lookup = QLabel(self.centralwidget_dict)
        self.label_lookup.setObjectName("label_lookup")
        self.label_lookup.setFont(font)
        self.label_lookup.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_dictionary.addWidget(self.label_lookup, 0, 0, 1, 1)

        self.textBrowser_dictresult = QTextBrowser(self.centralwidget_dict)
        self.textBrowser_dictresult.setObjectName("textBrowser_dictresult")
        self.textBrowser_dictresult.setFont(font)

        self.gridLayout_dictionary.addWidget(self.textBrowser_dictresult, 3, 1, 1, 1)

        self.comboBox_lookup = QComboBox(self.centralwidget_dict)
        self.comboBox_lookup.setObjectName("comboBox_lookup")

        self.gridLayout_dictionary.addWidget(self.comboBox_lookup, 0, 1, 1, 1)

        self.label_searchtern = QLabel(self.centralwidget_dict)
        self.label_searchtern.setObjectName("label_searchtern")
        self.label_searchtern.setFont(font)
        self.label_searchtern.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_dictionary.addWidget(self.label_searchtern, 1, 0, 1, 1)

        self.label_result = QLabel(self.centralwidget_dict)
        self.label_result.setObjectName("label_result")
        self.label_result.setFont(font)
        self.label_result.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_dictionary.addWidget(self.label_result, 3, 0, 1, 1)

        self.verticalSpacer_dict = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_dictionary.addItem(self.verticalSpacer_dict, 2, 1, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_dictionary, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget_dict)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUI

        # # setupUi
        # self.dict_layout = QtWidgets.QGridLayout()
        #
        # # create dictionary options dropdown
        # self.dictionary_dropdown = QtWidgets.QComboBox(self.tab_dictionary)
        #
        # # add options for dictionary
        # self.dictionary_dropdown.addItems(dictonary_options_list)
        #
        # # adjust parameters of dictionary options dropdown
        # self.dictionary_dropdown.setMaximumSize(QtCore.QSize(407, 16777215))
        # self.dictionary_dropdown.setObjectName("dictionary_dropdown")
        #
        # self.dict_layout.addWidget(self.dictionary_dropdown, 0, 1, 1, 1)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        # if QT_CONFIG(tooltip)
        self.lineEdit_dictsearch.setToolTip(QCoreApplication.translate("MainWindow", "enter word here", None))
        # endif // QT_CONFIG(tooltip)
        self.lineEdit_dictsearch.setText("")
        self.label_lookup.setText(QCoreApplication.translate("MainWindow", "Look up", None))
        self.textBrowser_dictresult.setHtml(QCoreApplication.translate("MainWindow",
                                                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                       "p,"
                                                                       "li { white-space: pre-wrap; }\n"
                                                                       "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                                       "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                                       None))
        self.label_searchtern.setText(QCoreApplication.translate("MainWindow", "Search term", None))
        self.label_result.setText(QCoreApplication.translate("MainWindow", "result", None))
    # retranslateUi


    # @pyqtSlot()
    # def on_click(self):
    #     print("\n")
    #     for currentQTableWidgetItem in self.tableWidget.selectedItems():
    #         print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

 def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DeskFocus <3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_translate), _translate("MainWindow", "📙 Guide"))
        self.label_result.setText(_translate("MainWindow", "result"))
        self.label_searchtern.setText(_translate("MainWindow", "Search term"))
        self.label_lookup.setText(_translate("MainWindow", "Look up"))
        self.lineEdit_dictsearch.setText("")

        # if QT_CONFIG(tooltip)
        self.lineEdit_dictsearch.setToolTip(_translate("MainWindow", "enter word here"))
        # endif // QT_CONFIG(tooltip)

        self.textBrowser_dictresultsetText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">"
                                     "Result here</span></p></body></html>"))
    # retranslateUi
if __name__ == '__main__':
    # Main window
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    app = QApplication(sys.argv)
    # Run the application!
    sys.exit(app.exec_())