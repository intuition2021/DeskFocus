# -*- coding: utf-8 -*-


######## imports ########

import sys

import ctypes

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QColorDialog, QSizePolicy, QMessageBox, QLabel

######## Constants ########

dictonary_options_list = ["definition", "synonym", "antonym"]


######## Class for the main window ########

class Ui_MainWindow(object):
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

        self.tab_translate = QtWidgets.QWidget()
        self.tab_translate.setObjectName("tab_translate")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_translate)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")

        self.language_label = QtWidgets.QLabel(self.tab_translate)
        self.language_label.setMinimumSize(QtCore.QSize(476, 0))
        self.language_label.setMaximumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.language_label.setFont(font)
        self.language_label.setAlignment(QtCore.Qt.AlignCenter)
        self.language_label.setObjectName("label")

        self.gridLayout_7.addWidget(self.language_label, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frm_label = QtWidgets.QLabel(self.tab_translate)
        self.frm_label.setMaximumSize(QtCore.QSize(67, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frm_label.setFont(font)
        self.frm_label.setObjectName("frm_label")

        self.gridLayout_6.addWidget(self.frm_label, 0, 0, 1, 1)

        self.frm_dropdown = QtWidgets.QComboBox(self.tab_translate)
        self.frm_dropdown.setMaximumSize(QtCore.QSize(407, 16777215))
        self.frm_dropdown.setObjectName("frm_dropdown")

        self.gridLayout_6.addWidget(self.frm_dropdown, 0, 1, 1, 1)

        self.to_label = QtWidgets.QLabel(self.tab_translate)
        self.to_label.setMaximumSize(QtCore.QSize(67, 16777215))

        # add language list for original text
        self.frm_dropdown.addItems(dictonary_options_list)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.to_label.setFont(font)
        self.to_label.setObjectName("to_label")

        self.gridLayout_6.addWidget(self.to_label, 1, 0, 1, 1)

        self.to_dropdown = QtWidgets.QComboBox(self.tab_translate)
        self.to_dropdown.setMaximumSize(QtCore.QSize(407, 16777215))
        self.to_dropdown.setObjectName("to_dropdown")

        self.gridLayout_6.addWidget(self.to_dropdown, 1, 1, 1, 1)
        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(6, -1, 6, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.select_borders_btn = QtWidgets.QPushButton(self.tab_translate)
        self.select_borders_btn.setMaximumSize(QtCore.QSize(238, 115))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_borders_btn.setFont(font)
        self.select_borders_btn.setAutoDefault(False)
        self.select_borders_btn.setObjectName("select_borders_btn")
        self.select_borders_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.select_borders_btn.clicked.connect(self.on_click_select_borders)

        # add language list for translation text
        self.to_dropdown.addItems(dictonary_options_list)

        self.horizontalLayout.addWidget(self.select_borders_btn)
        self.translate_btn = QtWidgets.QPushButton(self.tab_translate)
        self.translate_btn.setMaximumSize(QtCore.QSize(238, 115))
        font = QtGui.QFont()
        font.setPointSize(12)

        # self.translate_btn.clicked.connect(self.on_click_openTranslateWin)
        self.translate_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.translate_btn.setFont(font)
        self.translate_btn.setAutoDefault(False)
        self.translate_btn.setObjectName("translate_btn")

        self.horizontalLayout.addWidget(self.translate_btn)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout_7.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_translate, "")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DeskTranslator v1.0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_translate), _translate("MainWindow", "📙 Guide"))
        self.frm_label.setText(_translate("MainWindow", "From:"))
        self.to_label.setText(_translate("MainWindow", "To:"))
        self.translate_btn.setText(_translate("MainWindow", "Translate"))
        self.select_borders_btn.setText(_translate("MainWindow", "Select borders"))
        self.language_label.setText(_translate("MainWindow", "Select language"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_translate), _translate("MainWindow", "🌐 Translate"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Main window
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Run the application!
    sys.exit(app.exec_())