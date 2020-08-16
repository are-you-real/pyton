# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 538)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.changeText = QtWidgets.QPushButton(self.centralwidget)
        self.changeText.setGeometry(QtCore.QRect(60, 90, 89, 25))
        self.changeText.setObjectName("changeText")
        self.changeText.clicked.connect(lambda: self.click())



        self.textToChange = QtWidgets.QLabel(self.centralwidget)
        self.textToChange.setGeometry(QtCore.QRect(290, 60, 131, 81))
        self.textToChange.setObjectName("textToChange")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 22))
        self.menubar.setObjectName("menubar")

        self.menusave = QtWidgets.QMenu(self.menubar)
        self.menusave.setObjectName("menusave")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menusave.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.changeText.setText(_translate("MainWindow", "change text"))
        self.textToChange.setText(_translate("MainWindow", "some text"))
        self.menusave.setTitle(_translate("MainWindow", "save"))

    def click(self):
        print("sth")
        self.textToChange.setText(" dziala?")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
