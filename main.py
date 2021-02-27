import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

### SAMPLE CODE FOR TESTING

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget

import tkinter as tk

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
        self.width = self.screen_width/2
        self.height = self.screen_height * 2/3
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

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())