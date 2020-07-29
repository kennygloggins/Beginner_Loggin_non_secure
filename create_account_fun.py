# By: Kenny_G_Loggins
# Created on: 7/23/20, 11:52 AM
# File: create_account_fun.py
# Project: Beginner_Loggin_non_secure

from tkinter import *
import sqlite3
import bcrypt

userdb = sqlite3.connect('user_name_password.db')

c = userdb.cursor()


def create_submit(u_name, p_word, p_pass):
    q = query(u_name)
    p = passwords(p_word, p_pass)
    hashed = bcrypt.hashpw(p_word.encode('utf8'), bcrypt.gensalt())
    print(q, p)
    if q == 'good' and p == 'good':
        # Insert Into Table:
        with userdb:
            c.execute('INSERT INTO uandp VALUES (:user_name, :password1)', {'user_name': u_name,
                                                                            'password1': hashed})
        return 'good good'

    elif q == 'short' and p == 'short':
        return 'qshort pshort'
    elif q == 'short' and p == 'bad':
        return 'qshort pbad'
    elif q== 'short' and p == 'no match':
        return 'qshort pno match'
    elif q == 'good' and p == 'short':
        return 'qgood pshort'
    elif q == 'good' and p == 'no match':
        return 'qgood pno match'
    elif q == 'good' and p == 'bad':
        return 'qgood pbad'
    elif q == 'bad' and p == 'bad':
        return 'qbad pbad'
    elif q == 'bad' and p == 'no match':
        return 'qbad pno match'
    elif q == 'bad' and p == 'short':
        return 'qbad pshort'
    elif q == 'bad' and p == 'good':
        return 'qbad pgood'

def query(u_name):
    # Store entered username
    nameg = str(u_name)
    # Grab a list of names in tuple form from uandp
    c.execute("SELECT * FROM uandp WHERE user_name=?", (nameg,))
    usernames = c.fetchone()

    if not usernames and len(nameg) > 4:
        return 'good'
    elif not usernames and len(nameg) <= 4:
        return 'short'
    else:
        return 'bad'


def passwords(p_word, p_pass):
    # Grab both passwords and check if they are equal
    if p_word == p_pass and len(p_word) > 4:
        return 'good'
    elif p_word == p_pass and len(p_word) <= 4:
        return 'short'
    elif p_word != p_pass and len(p_word) <= 4:
        return 'short'
    elif p_word != p_pass and len(p_word) > 4:
        return 'no match'
    else:
        return 'bad'
