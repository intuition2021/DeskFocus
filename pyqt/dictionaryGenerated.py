# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dictionaryGenerated.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 555)
        self.centralwidget_dict = QtWidgets.QWidget(MainWindow)
        self.centralwidget_dict.setObjectName("centralwidget_dict")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget_dict)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_dictionary = QtWidgets.QGridLayout()
        self.gridLayout_dictionary.setObjectName("gridLayout_dictionary")
        self.textBrowser_dictresult = QtWidgets.QTextBrowser(self.centralwidget_dict)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_dictresult.setFont(font)
        self.textBrowser_dictresult.setObjectName("textBrowser_dictresult")
        self.gridLayout_dictionary.addWidget(self.textBrowser_dictresult, 4, 1, 1, 1)
        self.label_searchtern = QtWidgets.QLabel(self.centralwidget_dict)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_searchtern.setFont(font)
        self.label_searchtern.setAlignment(QtCore.Qt.AlignCenter)
        self.label_searchtern.setObjectName("label_searchtern")
        self.gridLayout_dictionary.addWidget(self.label_searchtern, 2, 0, 1, 1)
        self.lineEdit_dictsearch = QtWidgets.QLineEdit(self.centralwidget_dict)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dictsearch.setFont(font)
        self.lineEdit_dictsearch.setText("")
        self.lineEdit_dictsearch.setDragEnabled(True)
        self.lineEdit_dictsearch.setObjectName("lineEdit_dictsearch")
        self.gridLayout_dictionary.addWidget(self.lineEdit_dictsearch, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_dictionary.addItem(spacerItem, 3, 1, 1, 1)
        self.comboBox_lookup = QtWidgets.QComboBox(self.centralwidget_dict)
        self.comboBox_lookup.setObjectName("comboBox_lookup")
        self.gridLayout_dictionary.addWidget(self.comboBox_lookup, 1, 1, 1, 1)
        self.label_result = QtWidgets.QLabel(self.centralwidget_dict)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_result.setFont(font)
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.gridLayout_dictionary.addWidget(self.label_result, 4, 0, 1, 1)
        self.label_lookup = QtWidgets.QLabel(self.centralwidget_dict)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_lookup.setFont(font)
        self.label_lookup.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lookup.setObjectName("label_lookup")
        self.gridLayout_dictionary.addWidget(self.label_lookup, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_dictionary, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget_dict)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_dictresult.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_searchtern.setText(_translate("MainWindow", "Search term"))
        self.lineEdit_dictsearch.setToolTip(_translate("MainWindow", "enter word here"))
        self.label_result.setText(_translate("MainWindow", "Result"))
        self.label_lookup.setText(_translate("MainWindow", "Look up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

