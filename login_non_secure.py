# By: Kenny_G_Loggins
# Created on: 7/22/20, 11:17 PM
# File: login_non_secure.py
# Project: Beginner_Loggin_non_secure

# Purpose of this file is to practice my programing by making a login prompt.

# Strips usernames separated by '=' from a file and stores them in list 'user_lst'
def username_cache():
    user_lst = []
    with open('logandpass.txt', 'r') as login_and_password:
        login_and_password.seek(0)
        for line in login_and_password:
            if line.find('='):
                txt_key, value = line.split('=')
                user_lst.append(txt_key)
        return user_lst


# Prompts user for a username, checks input against 'user_lst' by calling username_cache()
def username():
    login_key = input('Please enter a Login Name: ')
    while username_cache().count(login_key) > 0:
        login_key = input('Username has already been taken, please try again:')
    return login_key


# Prompts user for a password and checks if they typed it in the same, twice
def password():
    password1 = input('Please enter in a password: ')
    password2 = input('Please re-enter in a password: ')
    while password1 != password2:
        password2 = input('Your passwords did no match, please try again: ')
    return password1


# Runs both functions
login = username()
password = password()


# Adds the valid username and password separated by '=' to 'logandpass.txt'
with open('logandpass.txt', 'a+') as login_and_password:
        login_and_password.write(login + '=' + password + '\n')
