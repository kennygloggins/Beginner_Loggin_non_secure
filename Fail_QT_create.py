# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_create.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Create(object):
    def setupUi(self, Create):
        Create.setObjectName("Create")
        Create.resize(400, 300)
        Create.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_username_label = QtWidgets.QLabel(Create)
        self.login_username_label.setGeometry(QtCore.QRect(30, 23, 111, 36))
        self.login_username_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_username_label.setObjectName("login_username_label")
        self.login_password_label = QtWidgets.QLabel(Create)
        self.login_password_label.setGeometry(QtCore.QRect(30, 93, 111, 36))
        self.login_password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_password_label.setObjectName("login_password_label")
        self.login_username_input = QtWidgets.QLineEdit(Create)
        self.login_username_input.setGeometry(QtCore.QRect(145, 23, 152, 36))
        self.login_username_input.setAlignment(QtCore.Qt.AlignCenter)
        self.login_username_input.setObjectName("login_username_input")
        self.login_password_input = QtWidgets.QLineEdit(Create)
        self.login_password_input.setGeometry(QtCore.QRect(145, 93, 152, 36))
        self.login_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_password_input.setAlignment(QtCore.Qt.AlignCenter)
        self.login_password_input.setObjectName("login_password_input")
        self.login_warning_username = QtWidgets.QLabel(Create)
        self.login_warning_username.setGeometry(QtCore.QRect(145, 68, 152, 20))
        self.login_warning_username.setScaledContents(False)
        self.login_warning_username.setAlignment(QtCore.Qt.AlignCenter)
        self.login_warning_username.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.login_warning_username.setObjectName("login_warning_username")
        self.login_warning_password = QtWidgets.QLabel(Create)
        self.login_warning_password.setGeometry(QtCore.QRect(145, 135, 152, 20))
        self.login_warning_password.setScaledContents(False)
        self.login_warning_password.setAlignment(QtCore.Qt.AlignCenter)
        self.login_warning_password.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.login_warning_password.setObjectName("login_warning_password")
        self.login_x_username = QtWidgets.QLabel(Create)
        self.login_x_username.setGeometry(QtCore.QRect(310, 30, 22, 22))
        self.login_x_username.setText("")
        self.login_x_username.setPixmap(QtGui.QPixmap(":/pics/Nuvola_apps_error.svg"))
        self.login_x_username.setScaledContents(True)
        self.login_x_username.setObjectName("login_x_username")
        self.login_x_password = QtWidgets.QLabel(Create)
        self.login_x_password.setGeometry(QtCore.QRect(310, 100, 22, 22))
        self.login_x_password.setText("")
        self.login_x_password.setPixmap(QtGui.QPixmap(":/pics/Nuvola_apps_error.svg"))
        self.login_x_password.setScaledContents(True)
        self.login_x_password.setObjectName("login_x_password")
        self.login_login_button = QtWidgets.QPushButton(Create)
        self.login_login_button.setGeometry(QtCore.QRect(120, 230, 99, 38))
        self.login_login_button.setObjectName("login_login_button")
        self.login_login_cancel = QtWidgets.QPushButton(Create)
        self.login_login_cancel.setGeometry(QtCore.QRect(225, 230, 99, 38))
        self.login_login_cancel.setObjectName("login_login_cancel")
        self.login_repass_label = QtWidgets.QLabel(Create)
        self.login_repass_label.setGeometry(QtCore.QRect(10, 163, 131, 36))
        self.login_repass_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.login_repass_label.setScaledContents(True)
        self.login_repass_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_repass_label.setObjectName("login_repass_label")
        self.login_repass_input = QtWidgets.QLineEdit(Create)
        self.login_repass_input.setEnabled(True)
        self.login_repass_input.setGeometry(QtCore.QRect(145, 163, 152, 36))
        self.login_repass_input.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.login_repass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_repass_input.setAlignment(QtCore.Qt.AlignCenter)
        self.login_repass_input.setObjectName("login_repass_input")
        self.login_x_repass = QtWidgets.QLabel(Create)
        self.login_x_repass.setGeometry(QtCore.QRect(310, 170, 22, 22))
        self.login_x_repass.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.login_x_repass.setText("")
        self.login_x_repass.setPixmap(QtGui.QPixmap(":/pics/Nuvola_apps_error.svg"))
        self.login_x_repass.setScaledContents(True)
        self.login_x_repass.setObjectName("login_x_repass")

        self.retranslateUi(Create)
        QtCore.QMetaObject.connectSlotsByName(Create)

    def retranslateUi(self, Create):
        _translate = QtCore.QCoreApplication.translate
        Create.setWindowTitle(_translate("Create", "Create Account"))
        self.login_username_label.setText(_translate("Create", "Username:"))
        self.login_password_label.setText(_translate("Create", "Password:"))
        self.login_warning_username.setText(_translate("Create", "Invalid username."))
        self.login_warning_password.setText(_translate("Create", "Invalid password."))
        self.login_login_button.setText(_translate("Create", "Login"))
        self.login_login_cancel.setText(_translate("Create", "Cancel"))
        self.login_repass_label.setText(_translate("Create", "Retype Password:"))

