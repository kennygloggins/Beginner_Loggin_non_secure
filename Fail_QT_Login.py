# By: Kenny_G_Loggins
# Created on: 7/28/20, 9:25 AM
# File: Fail_QT_Login.py
# Project: Beginner_Loggin_non_secure


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from login_fun import login_submit


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUI()



class Ui_Login(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.login_username_label = QtWidgets.QLabel(Dialog)
        self.login_username_label.setGeometry(QtCore.QRect(10, 60, 111, 36))
        self.login_username_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_username_label.setObjectName("login_username_label")
        self.login_password_label = QtWidgets.QLabel(Dialog)
        self.login_password_label.setGeometry(QtCore.QRect(10, 140, 111, 36))
        self.login_password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_password_label.setObjectName("login_password_label")
        self.login_username_input = QtWidgets.QLineEdit(Dialog)
        self.login_username_input.setGeometry(QtCore.QRect(125, 60, 152, 36))
        self.login_username_input.setAlignment(QtCore.Qt.AlignCenter)
        self.login_username_input.setObjectName("login_username_input")
        self.login_password_input = QtWidgets.QLineEdit(Dialog)
        self.login_password_input.setGeometry(QtCore.QRect(125, 140, 152, 36))
        self.login_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_password_input.setAlignment(QtCore.Qt.AlignCenter)
        self.login_password_input.setObjectName("login_password_input")
        self.login_warning_username = QtWidgets.QLabel(Dialog)
        self.login_warning_username.setGeometry(QtCore.QRect(125, 105, 152, 20))
        self.login_warning_username.setScaledContents(False)
        self.login_warning_username.setAlignment(QtCore.Qt.AlignCenter)
        self.login_warning_username.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.login_warning_username.setObjectName("login_warning_username")
        self.login_warning_password = QtWidgets.QLabel(Dialog)
        self.login_warning_password.setGeometry(QtCore.QRect(125, 182, 152, 20))
        self.login_warning_password.setScaledContents(False)
        self.login_warning_password.setAlignment(QtCore.Qt.AlignCenter)
        self.login_warning_password.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.login_warning_password.setObjectName("login_warning_password")
        self.login_x_username = QtWidgets.QLabel(Dialog)
        self.login_x_username.setGeometry(QtCore.QRect(290, 67, 22, 22))
        self.login_x_username.setText("")
        self.login_x_username.setPixmap(QtGui.QPixmap(""))
        self.login_x_username.setScaledContents(True)
        self.login_x_username.setObjectName("login_x_username")
        #
        self.login_login_button = QtWidgets.QPushButton(Dialog)
        self.login_login_button.setGeometry(QtCore.QRect(90, 230, 99, 38))
        self.login_login_button.setObjectName("login_login_button")
        self.login_login_cancel = QtWidgets.QPushButton(Dialog)
        self.login_login_cancel.setGeometry(QtCore.QRect(200, 230, 99, 38))
        self.login_login_cancel.setObjectName("login_login_cancel")
        self.login_x_username_2 = QtWidgets.QLabel(Dialog)
        self.login_x_username_2.setGeometry(QtCore.QRect(290, 147, 22, 22))
        self.login_x_username_2.setText("")
        self.login_x_username_2.setPixmap(QtGui.QPixmap(""))
        self.login_x_username_2.setScaledContents(True)
        self.login_x_username_2.setObjectName("login_x_username_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.login_login_button.clicked.connect(self.goget)
        self.login_login_cancel.clicked.connect(self.login_hide)

    def goget(self):
        _translate = QtCore.QCoreApplication.translate
        u_name = self.login_username_input.text()
        p_word = self.login_password_input.text()
        i = login_submit(u_name, p_word)
        if i == 0:
            self.login_warning_username.setText(_translate("Dialog", "Invalid username."))
            self.login_warning_password.setText(_translate("Dialog", "Invalid password."))
            self.login_x_username.setPixmap(QtGui.QPixmap("Nuvola_apps_error.svg"))
            self.login_x_username_2.setPixmap(QtGui.QPixmap("Nuvola_apps_error.svg"))
        elif i == 1:
            exit()
        elif i == 2:
            self.login_warning_username.setText(_translate("Dialog", "Invalid username."))
            self.login_x_username.setPixmap(QtGui.QPixmap("Nuvola_apps_error.svg"))
            self.login_x_username_2.setPixmap(QtGui.QPixmap(""))
            self.login_warning_password.setText(_translate("Dialog", ""))
        elif i == 3:
            self.login_warning_username.setText(_translate("Dialog", ""))
            self.login_x_username.setPixmap(QtGui.QPixmap(""))
            self.login_x_username_2.setPixmap(QtGui.QPixmap("Nuvola_apps_error.svg"))
            self.login_warning_password.setText(_translate("Dialog", "Invalid password."))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.login_username_label.setText(_translate("Dialog", "Username:"))
        self.login_password_label.setText(_translate("Dialog", "Password:"))
        self.login_warning_username.setText(_translate("Dialog", ""))
        self.login_warning_password.setText(_translate("Dialog", ""))
        self.login_login_button.setText(_translate("Dialog", "Login"))
        self.login_login_cancel.setText(_translate("Dialog", "Cancel"))
