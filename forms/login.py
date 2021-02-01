import sys, os
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from rest_framework import request, response


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("gui/login.ui", self)

        print(dir(self))
        self.pushButton_access.clicked.connect(self.bt_access_clicked)
        self.pushButton_error.clicked.connect(self.bt_error_clicked)
        self.show()

    def bt_access_clicked(self, **kargs):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        print(username, password)
        return

    def bt_error_clicked(self, **kargs):
        print("Botão de error pressionado.")
        return


app = QtWidgets.QApplication(sys.argv)
w = Login()
app.exec_()