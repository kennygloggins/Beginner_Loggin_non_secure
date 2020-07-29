# By: Kenny_G_Loggins
# Created on: 7/27/20, 3:57 PM
# File: login_fun.py
# Project: Beginner_Loggin_non_secure


import sqlite3
import bcrypt

userdb = sqlite3.connect('user_name_password.db')

c = userdb.cursor()


def login_submit(u_name, p_word):
    u = user_name(u_name)
    p = password(u_name, p_word)
    if len(u_name) == 0 and len(p_word) == 0:
        return 'ublank pblank'
    elif u == 'good' and p == 'good':
        return 'ugood pgood'
    elif u == 'bad' and p == 'good':
        return 'ubad pgood'
    elif u == 'bad' and p == 'bad':
        return 'ubad pbad'



def user_name(u_name):
    # Make sure input is a string
    nameg = str(u_name)
    # Find if nameg is in the database
    c.execute("SELECT * FROM uandp WHERE user_name=?", (nameg,))
    if c.fetchone():
        return 'good'
    else:
        return 'bad'

def password(u_name, p_word):
    check = False
    # Mage sure input is a string
    nameg = str(u_name)
    # Find password that goes with the username
    c.execute("SELECT password1 FROM uandp WHERE user_name=?", (nameg,))
    tup_password = c.fetchone()
    user_input = p_word
    print(tup_password)
    try:
        upassword = tup_password[0]
        check = bcrypt.checkpw(user_input.encode('utf8'), upassword)
    except TypeError:
        pass

    if check:
        return 'good'
    else:
        return 'bad'
