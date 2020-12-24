# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 557)
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lable1 = QtWidgets.QLabel(self.centralwidget)
        self.lable1.setGeometry(QtCore.QRect(50, 130, 521, 18))
        self.lable1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lable1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lable1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lable1.setLineWidth(-4)
        self.lable1.setMidLineWidth(33)
        self.lable1.setWordWrap(False)
        self.lable1.setObjectName("lable1")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 150, 621, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(170, 10, 111, 111))
        self.label2.setStyleSheet("background-image: url(:/dbaccess/work/Sharif university projects/DB-Security/final-project/db-security-final-project/pic/images.jpeg);")
        self.label2.setText("")
        self.label2.setPixmap(QtGui.QPixmap("pic/images.jpeg"))
        self.label2.setScaledContents(True)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(340, 10, 111, 111))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        self.label3.setFont(font)
        self.label3.setStyleSheet("background-image: url(:/sina/work/Sharif university projects/DB-Security/final-project/db-security-final-project/pic/download.jpeg);")
        self.label3.setText("")
        self.label3.setPixmap(QtGui.QPixmap("pic/download.jpeg"))
        self.label3.setScaledContents(True)
        self.label3.setObjectName("label3")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(200, 320, 201, 41))
        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setStyleSheet("color: rgb(94, 92, 91);\n"
"font: 12pt \"A Iranian Sans\";\n"
"border-color: rgb(255, 0, 4);\n"
"border-top-color: rgb(255, 0, 4);")
        self.lineEdit1.setText("")
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit1_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1_2.setGeometry(QtCore.QRect(200, 400, 201, 41))
        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit1_2.setFont(font)
        self.lineEdit1_2.setStyleSheet("color: rgb(94, 92, 91);\n"
"selection-color: rgb(85, 255, 0);\n"
"font: 12pt \"A Iranian Sans\";\n"
"border-color: rgb(255, 0, 4);\n"
"border-top-color: rgb(255, 0, 4);")
        self.lineEdit1_2.setText("")
        self.lineEdit1_2.setObjectName("lineEdit1_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 209, 201, 51))
        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 20pt \"A Iranian Sans\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 270, 621, 51))
        font = QtGui.QFont()
        font.setFamily("A Iranian Sans")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 15pt \"A Iranian Sans\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 460, 201, 41))
        self.pushButton.setStyleSheet("color: rgb(255, 0, 4);\n"
"border-color: rgb(5, 9, 255);\n"
"color: rgb(0, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lable1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Wellcome to the access controll system of Sina hospital</span></p></body></html>"))
        self.lineEdit1.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>username </p></body></html>"))
        self.lineEdit1.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.lineEdit1_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>username </p></body></html>"))
        self.lineEdit1_2.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#157daa;\">Login</span></p></body></html>"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#aa0000;\">Please enter your Username and Password</span></p><p align=\"center\"><span style=\" color:#aa0000;\"><br/></span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Login into the System"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
