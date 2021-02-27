# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Python Stop watch")

		# setting geometry
		self.setGeometry(100, 100, 400, 500)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for widgets
	def UiComponents(self):

		# counter
		self.count = 0

		# creating flag
		self.flag = False

		# creating a label to show the time
		self.label = QLabel(self)

		# setting geometry of label
		self.label.setGeometry(75, 100, 250, 70)

		# adding border to the label
		self.label.setStyleSheet("border : 4px solid black;")

		# setting text to the label
		self.label.setText(str(self.count))

		# setting font to the label
		self.label.setFont(QFont('Arial', 25))

		# setting alignment to the text of label
		self.label.setAlignment(Qt.AlignCenter)

		# creating start button
		start = QPushButton("Start", self)

		# setting geometry to the button
		start.setGeometry(125, 250, 150, 40)

		# add action to the method
		start.pressed.connect(self.Start)

		# creating pause button
		pause = QPushButton("Pause", self)

		# setting geometry to the button
		pause.setGeometry(125, 300, 150, 40)

		# add action to the method
		pause.pressed.connect(self.Pause)

		# creating reset button
		re_set = QPushButton("Re-set", self)

		# setting geometry to the button
		re_set.setGeometry(125, 350, 150, 40)

		# add action to the method
		re_set.pressed.connect(self.Re_set)

		# creating a timer object
		timer = QTimer(self)

		# adding action to timer
		timer.timeout.connect(self.showTime)

		# update the timer every tenth second
		timer.start(100)

	# method called by timer
	def showTime(self):

		# checking if flag is true
		if self.flag:

			# incrementing the counter
			self.count+= 1

		# getting text from count
		text = str(self.count / 10)

		# showing text
		self.label.setText(text)


	def Start(self):

		# making flag to true
		self.flag = True

	def Pause(self):

		# making flag to False
		self.flag = False

	def Re_set(self):

		# making flag to false
		self.flag = False

		# reseeting the count
		self.count = 0

		# setting text to label
		self.label.setText(str(self.count))


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
