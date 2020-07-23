# By: Kenny_G_Loggins
# Created on: 7/22/20, 11:17 PM
# File: login_non_secure.py
# Project: Beginner_Loggin_non_secure


# Purpose of this file is to practice my programing by making a login prompt.


def username():
    login_key = input('Please enter a Login Name: ')
    with open('logandpass.txt', 'r') as login_and_password:
        for line in login_and_password:
            txt_key, value = line.split('=')
            if txt_key == login_key:
                print('That username has already been taken, please choose another.')
                username()
    return login_key


def password():
    password1 = input('Please enter in a password: ')
    password2 = input('Please re-enter in a password: ')
    if password1 != password2:
        print('The passwords did not match, please try again.')
        password()
    else:
        return password1


login = username()
password = password()
