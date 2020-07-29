# By: Kenny_G_Loggins
# Created on: 7/27/20, 3:54 PM
# File: Fail_root_tkinter.py
# Project: Beginner_Loggin_non_secure

import tkinter.ttk
from tkinter import *
import sqlite3
import bcrypt
from create_account_fun import create_account
from login_fun import login


# Create database or connect to one
userdb = sqlite3.connect('user_name_password.db')

# Create cursor
c = userdb.cursor()

root = Tk()
root.title('tkinter test')
root.geometry('550x140')
img = PhotoImage(file='/home/kgl/Pictures/pug.png')
root.tk.call('wm', 'iconphoto', root._w, img)


def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 4 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


center(root)


'''
# Create Table
c.execute('CREATE TABLE uandp (user_name text, password1 text)')
'''


def woot(root):
    # global login_button
    # global create_account_button

    login_button = Button(root, text='Login', command=lambda:
                   [login_button.grid_forget(), create_account_button.grid_forget(), login(root)])
    login_button.grid(row=0, column=1)
    create_account_button = Button(root, text='Create Account', command=lambda:
                            [login_button.grid_forget(), create_account_button.grid_forget(), create_account(root)])
    create_account_button.grid(row=1, column=1)


woot(root)

root.mainloop()

# Commit Changes
userdb.commit()

# Close Connection outside of tkinter loop
userdb.close()
