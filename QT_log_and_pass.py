# By: Kenny_G_Loggins
# Created on: 7/28/20
# File: QT_log_and_pass.py
# Project: Beginner_Loggin_non_secure


from create_account_fun import create_submit
from login_fun import login_submit
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

'''
userdb = sqlite3.connect('user_name_password.db')
c = userdb.cursor()
# Create Table
c.execute('CREATE TABLE uandp (user_name text, password1 text)')
# Commit Changes
userdb.commit()
# Close Connection outside of tkinter loop
userdb.close()
'''

class Ui_MainWindow(object):

    login_warning = False
    create_warning = True

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 317)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 511, 281))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setObjectName("page")
        self.login_lap_cancel = QtWidgets.QPushButton(self.page)
        self.login_lap_cancel.setGeometry(QtCore.QRect(265, 120, 120, 50))
        self.login_lap_cancel.setObjectName("login_lap_cancel")
        self.login_lap_button = QtWidgets.QPushButton(self.page)
        self.login_lap_button.setGeometry(QtCore.QRect(130, 120, 120, 50))
        self.login_lap_button.setObjectName("login_lap_button")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.create_x_repass = QtWidgets.QLabel(self.page_2)
        self.create_x_repass.setGeometry(QtCore.QRect(370, 180, 22, 22))
        self.create_x_repass.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.create_x_repass.setText("")
        self.create_x_repass.setPixmap(QtGui.QPixmap(""))
        self.create_x_repass.setScaledContents(True)
        self.create_x_repass.setObjectName("create_x_repass")
        self.create_warning_username = QtWidgets.QLabel(self.page_2)
        self.create_warning_username.setGeometry(QtCore.QRect(205, 78, 152, 20))
        self.create_warning_username.setScaledContents(False)
        self.create_warning_username.setAlignment(QtCore.Qt.AlignCenter)
        self.create_warning_username.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.create_warning_username.setObjectName("create_warning_username")
        self.create_repass_label = QtWidgets.QLabel(self.page_2)
        self.create_repass_label.setGeometry(QtCore.QRect(70, 173, 131, 36))
        self.create_repass_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.create_repass_label.setScaledContents(True)
        self.create_repass_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.create_repass_label.setObjectName("create_repass_label")
        self.create_password_input = QtWidgets.QLineEdit(self.page_2)
        self.create_password_input.setGeometry(QtCore.QRect(205, 103, 152, 36))
        self.create_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.create_password_input.setAlignment(QtCore.Qt.AlignCenter)
        self.create_password_input.setObjectName("create_password_input")
        self.create_password_input.setPlaceholderText('> 4 characters')
        self.create_login_button = QtWidgets.QPushButton(self.page_2)
        self.create_login_button.setGeometry(QtCore.QRect(180, 240, 99, 38))
        self.create_login_button.setObjectName("create_login_button")
        self.create_login_cancel = QtWidgets.QPushButton(self.page_2)
        self.create_login_cancel.setGeometry(QtCore.QRect(285, 240, 99, 38))
        self.create_login_cancel.setObjectName("create_login_cancel")
        self.create_repass_input = QtWidgets.QLineEdit(self.page_2)
        self.create_repass_input.setEnabled(True)
        self.create_repass_input.setGeometry(QtCore.QRect(205, 173, 152, 36))
        self.create_repass_input.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.create_repass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.create_repass_input.setAlignment(QtCore.Qt.AlignCenter)
        self.create_repass_input.setObjectName("create_repass_input")
        self.create_x_password = QtWidgets.QLabel(self.page_2)
        self.create_x_password.setGeometry(QtCore.QRect(370, 110, 22, 22))
        self.create_x_password.setText("")
        self.create_x_password.setPixmap(QtGui.QPixmap(""))
        self.create_x_password.setScaledContents(True)
        self.create_x_password.setObjectName("create_x_password")
        self.create_username_input = QtWidgets.QLineEdit(self.page_2)
        self.create_username_input.setGeometry(QtCore.QRect(205, 33, 152, 36))
        self.create_username_input.setAlignment(QtCore.Qt.AlignCenter)
        self.create_username_input.setObjectName("create_username_input")
        self.create_username_input.setPlaceholderText('> 4 characters')
        self.create_warning_password = QtWidgets.QLabel(self.page_2)
        self.create_warning_password.setGeometry(QtCore.QRect(205, 145, 152, 20))
        self.create_warning_password.setScaledContents(False)
        self.create_warning_password.setAlignment(QtCore.Qt.AlignCenter)
        self.create_warning_password.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.create_warning_password.setObjectName("create_warning_password")
        self.login_x_username = QtWidgets.QLabel(self.page_2)
        self.login_x_username.setGeometry(QtCore.QRect(370, 40, 22, 22))
        self.login_x_username.setText("")
        self.login_x_username.setPixmap(QtGui.QPixmap(""))
        self.login_x_username.setScaledContents(True)
        self.login_x_username.setObjectName("login_x_username")
        self.create_password_label = QtWidgets.QLabel(self.page_2)
        self.create_password_label.setGeometry(QtCore.QRect(90, 103, 111, 36))
        self.create_password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.create_password_label.setObjectName("create_password_label")
        self.create_username_label = QtWidgets.QLabel(self.page_2)
        self.create_username_label.setGeometry(QtCore.QRect(90, 33, 111, 36))
        self.create_username_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.create_username_label.setObjectName("create_username_label")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.login_login_cancel = QtWidgets.QPushButton(self.page_3)
        self.login_login_cancel.setGeometry(QtCore.QRect(270, 223, 99, 38))
        self.login_login_cancel.setObjectName("login_login_cancel")
        self.login_password_input = QtWidgets.QLineEdit(self.page_3)
        self.login_password_input.setGeometry(QtCore.QRect(195, 133, 152, 36))
        self.login_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_password_input.setAlignment(QtCore.Qt.AlignCenter)
        self.login_password_input.setObjectName("login_password_input")
        self.login_warning_username = QtWidgets.QLabel(self.page_3)
        self.login_warning_username.setGeometry(QtCore.QRect(195, 98, 152, 20))
        self.login_warning_username.setScaledContents(False)
        self.login_warning_username.setAlignment(QtCore.Qt.AlignCenter)
        self.login_warning_username.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.login_warning_username.setObjectName("login_warning_username")
        self.login_x_pass = QtWidgets.QLabel(self.page_3)
        self.login_x_pass.setGeometry(QtCore.QRect(360, 140, 22, 22))
        self.login_x_pass.setText("")
        self.login_x_pass.setPixmap(QtGui.QPixmap(""))
        self.login_x_pass.setScaledContents(True)
        self.login_x_pass.setObjectName("login_x_pass")
        self.login_login_button = QtWidgets.QPushButton(self.page_3)
        self.login_login_button.setGeometry(QtCore.QRect(160, 223, 99, 38))
        self.login_login_button.setObjectName("login_login_button")
        self.login_username_label = QtWidgets.QLabel(self.page_3)
        self.login_username_label.setGeometry(QtCore.QRect(80, 53, 111, 36))
        self.login_username_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_username_label.setObjectName("login_username_label")
        self.login_password_label = QtWidgets.QLabel(self.page_3)
        self.login_password_label.setGeometry(QtCore.QRect(80, 133, 111, 36))
        self.login_password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_password_label.setObjectName("login_password_label")
        self.login_username_input = QtWidgets.QLineEdit(self.page_3)
        self.login_username_input.setGeometry(QtCore.QRect(195, 53, 152, 36))
        self.login_username_input.setAlignment(QtCore.Qt.AlignCenter)
        self.login_username_input.setObjectName("login_username_input")
        self.login_warning_password = QtWidgets.QLabel(self.page_3)
        self.login_warning_password.setGeometry(QtCore.QRect(195, 175, 152, 20))
        self.login_warning_password.setScaledContents(False)
        self.login_warning_password.setAlignment(QtCore.Qt.AlignCenter)
        self.login_warning_password.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.login_warning_password.setObjectName("login_warning_password")
        self.login_x_username_2 = QtWidgets.QLabel(self.page_3)
        self.login_x_username_2.setGeometry(QtCore.QRect(360, 60, 22, 22))
        self.login_x_username_2.setText("")
        self.login_x_username_2.setPixmap(QtGui.QPixmap(""))
        self.login_x_username_2.setScaledContents(True)
        self.login_x_username_2.setObjectName("login_x_username_2")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Init widget index
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Button Navigation
        self.login_login_button.clicked.connect(self.login_goget)
        self.login_lap_button.clicked.connect(self.login_window)
        self.login_lap_cancel.clicked.connect(self.create_window)
        self.create_login_button.clicked.connect(self.create_goget)
        self.login_login_cancel.clicked.connect(self.lap_window)
        self.create_login_cancel.clicked.connect(self.lap_window)

        # Tab order and focus for login window
        self.login_username_input.setTabOrder(self.login_username_input, self.login_password_input)
        self.login_password_input.setTabOrder(self.login_password_input, self.login_login_button)
        self.login_login_button.setTabOrder(self.login_login_button, self.login_login_cancel)
        self.login_login_cancel.setTabOrder(self.login_login_cancel, self.login_username_input)


        # Tab order and focus for create account window
        self.create_username_input.setTabOrder(self.create_username_input, self.create_password_input)
        self.create_password_input.setTabOrder(self.create_password_input, self.create_repass_input)
        self.create_repass_input.setTabOrder(self.create_repass_input, self.create_login_button)
        self.create_login_button.setTabOrder(self.create_login_button, self.create_login_cancel)
        self.create_login_cancel.setTabOrder(self.create_login_cancel, self.create_username_input)

        # Set focus
        self.create_username_input.setFocus()
        self.login_username_input.setFocus()
        self.login_lap_button.setFocus()

    # Set widget index and clear warnings
    def lap_window(self):
        _translate = QtCore.QCoreApplication.translate
        if self.login_warning == True:
            self.login_warning_username.setText(_translate("Dialog", ""))
            self.login_x_username_2.setPixmap(QtGui.QPixmap(""))
            self.login_warning_password.setText(_translate("Dialog", ""))
            self.login_x_pass.setPixmap(QtGui.QPixmap(""))
        if self.create_warning == True:
            self.login_x_username.setPixmap(QtGui.QPixmap(""))
            self.create_warning_username.setText(_translate("Dialog", ""))
            self.create_x_password.setPixmap(QtGui.QPixmap(""))
            self.create_x_repass.setPixmap(QtGui.QPixmap(""))
            self.create_warning_password.setText(_translate("Dialog", ""))
        self.stackedWidget.setCurrentIndex(0)


    def create_window(self):
        _translate = QtCore.QCoreApplication.translate
        if self.login_warning == True:
            self.login_warning_username.setText(_translate("Dialog", ""))
            self.login_x_username_2.setPixmap(QtGui.QPixmap(""))
            self.login_warning_password.setText(_translate("Dialog", ""))
            self.login_x_pass.setPixmap(QtGui.QPixmap(""))
        self.stackedWidget.setCurrentIndex(1)

    def login_window(self):
        _translate = QtCore.QCoreApplication.translate
        if self.create_warning == True:
            self.login_x_username.setPixmap(QtGui.QPixmap(""))
            self.create_warning_username.setText(_translate("Dialog", ""))
            self.create_x_password.setPixmap(QtGui.QPixmap(""))
            self.create_x_repass.setPixmap(QtGui.QPixmap(""))
            self.create_warning_password.setText(_translate("Dialog", ""))
        self.stackedWidget.setCurrentIndex(2)

    def login_goget(self):
        # Grab the user's input and test if it's valid through login_fun.py
        _translate = QtCore.QCoreApplication.translate
        u_name = self.login_username_input.text()
        p_word = self.login_password_input.text()
        i = login_submit(u_name, p_word)

        # Handles the conditions for the error messages
        if i.count('ubad') > 0 or i.count('ublank') > 0:
            self.login_warning_username.setText(_translate("Dialog", "Invalid username."))
            self.login_x_username_2.setPixmap(QtGui.QPixmap("Nuvola_apps_error.svg"))
            self.login_warning = True
        else:
            self.login_warning_username.setText(_translate("Dialog", ""))
            self.login_x_username_2.setPixmap(QtGui.QPixmap(""))
            self.login_warning = False

        if i.count('pbad') > 0 or i.count('pblank') > 0:
            self.login_warning_password.setText(_translate("Dialog", "Invalid password."))
            self.login_x_pass.setPixmap(QtGui.QPixmap("Nuvola_apps_error.svg"))
            self.login_warning = True
        else:
            self.login_warning_password.setText(_translate("Dialog", ""))
            self.login_x_pass.setPixmap(QtGui.QPixmap(""))
            self.login_warning = False

        # Everything entered was valid, exit.
        if i == 'good good':
            exit()

    def create_goget(self):
        # Grab the user's input and test if it's valid through create_account_fun.py
        _translate = QtCore.QCoreApplication.translate
        u_name = self.create_username_input.text()
        p_word = self.create_password_input.text()
        p_pass = self.create_repass_input.text()
        i = create_submit(u_name, p_word, p_pass)
        print(u_name, p_word, p_pass)  # for debugging

        # Handles the conditions for the error messages
        if i.count('qgood') > 0:
            self.login_x_username.setPixmap(QtGui.QPixmap(""))
            self.create_warning_username.setText(_translate("Dialog", ""))
            self.create_warning = False
        elif i.count('qshort') > 0:
            self.login_x_username.setPixmap(QtGui.QPixmap("Nuvola_apps_error.svg"))
            self.create_warning_username.setText(_translate("Dialog", "Name too short."))
            self.create_warning = True
        else:
            self.login_x_username.setPixmap(QtGui.QPixmap("Nuvola_apps_error.svg"))
            self.create_warning_username.setText(_translate("Dialog", "Invalid username."))
            self.create_warning = True

        if i.count('pgood') > 0:
            self.create_x_password.setPixmap(QtGui.QPixmap(""))
            self.create_x_repass.setPixmap(QtGui.QPixmap(""))
            self.create_warning_password.setText(_translate("Dialog", ""))
            self.create_warning = False
        elif i.count('pshort') > 0:
            self.create_x_password.setPixmap(QtGui.QPixmap("Nuvola_apps_error.svg"))
            self.create_x_repass.setPixmap(QtGui.QPixmap("Nuvola_apps_error.svg"))
            self.create_warning_password.setText(_translate("Dialog", "Pass too short."))
            self.create_warning = True
        elif i.count('pno'):
            self.create_x_password.setPixmap(QtGui.QPixmap("Nuvola_apps_error.svg"))
            self.create_x_repass.setPixmap(QtGui.QPixmap("Nuvola_apps_error.svg"))
            self.create_warning_password.setText(_translate("Dialog", "Don't match."))
            self.create_warning = True
        else:
            self.create_x_password.setPixmap(QtGui.QPixmap("Nuvola_apps_error.svg"))
            self.create_x_repass.setPixmap(QtGui.QPixmap("Nuvola_apps_error.svg"))
            self.create_warning_password.setText(_translate("Dialog", "Invalid password."))
            self.create_warning = True

        # Everything entered was valid, goes to login page
        if i == 'good good':
            self.stackedWidget.setCurrentIndex(2)

    # Display labels
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Break"))
        self.login_lap_cancel.setText(_translate("MainWindow", "Create"))
        self.login_lap_button.setText(_translate("MainWindow", "Login"))
        self.create_warning_username.setText(_translate("MainWindow", ""))
        self.create_repass_label.setText(_translate("MainWindow", "Retype Password:"))
        self.create_login_button.setText(_translate("MainWindow", "Create"))
        self.create_login_cancel.setText(_translate("MainWindow", "Cancel"))
        self.create_warning_password.setText(_translate("MainWindow", ""))
        self.create_password_label.setText(_translate("MainWindow", "Password:"))
        self.create_username_label.setText(_translate("MainWindow", "Username:"))
        self.login_login_cancel.setText(_translate("MainWindow", "Cancel"))
        self.login_warning_username.setText(_translate("MainWindow", ""))
        self.login_login_button.setText(_translate("MainWindow", "Login"))
        self.login_username_label.setText(_translate("MainWindow", "Username:"))
        self.login_password_label.setText(_translate("MainWindow", "Password:"))
        self.login_warning_password.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
