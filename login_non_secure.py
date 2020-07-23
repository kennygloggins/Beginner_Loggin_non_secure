# By: Kenny_G_Loggins
# Created on: 7/22/20, 11:17 PM
# File: login_non_secure.py
# Project: Beginner_Loggin_non_secure


# Purpose of this file is to practice my programing by making a login prompt.


def username():
    login_key = input('Please enter a Login Name: ')
    with open('logandpass.txt', 'r') as login_and_password:
        login_and_password.seek(0)
        for line in login_and_password:
            if line.find('='):
                txt_key, value = line.split('=')
                while txt_key == login_key:
                    login_key = input('That username has already been taken, please choose another:')
    return login_key


def password():
    password1 = input('Please enter in a password: ')
    password2 = input('Please re-enter in a password: ')
    while password1 != password2:
        password2 = input('Your passwords did no match, please try again: ')
    return password1


login = username()
password = password()

with open('logandpass.txt', 'a+') as login_and_password:
        login_and_password.write(login + '=' + password + '\n')
