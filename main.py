# -*- coding: utf-8 -*-


######## imports ########

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

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

class App(QMainWindow):
    def get_dimensions(self):
        root = tk.Tk()
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

    def __init__(self):
        super().__init__()

        self.get_dimensions()

        self.title = 'DeskFocus'
        self.left = 0
        self.top = 0
        self.width = self.screen_width/4
        self.height = self.screen_height/4
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.show()

######## Tab widget within main window ########

class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())


        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab_dictionary = QWidget()
        self.tab_tasklist = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab_dictionary, "📖 Dictionary")
        self.tabs.addTab(self.tab_tasklist, "🗎 Task List")

        # Create first tab
        self.tab_dictionary.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab_dictionary.layout.addWidget(self.pushButton1)
        self.tab_dictionary.setLayout(self.tab_dictionary.layout)

        self.createDictionaryBox()

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def createDictionaryBox(self):
        self.dict_layout = QtWidgets.QGridLayout()

        # create dictionary options dropdown
        self.dictionary_dropdown = QtWidgets.QComboBox(self.tab_dictionary)

        # add options for dictionary
        self.dictionary_dropdown.addItems(dictonary_options_list)

        # adjust parameters of dictionary options dropdown
        self.dictionary_dropdown.setMaximumSize(QtCore.QSize(407, 16777215))
        self.dictionary_dropdown.setObjectName("dictionary_dropdown")

        self.dict_layout.addWidget(self.dictionary_dropdown, 0, 1, 1, 1)




    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())