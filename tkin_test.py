# By: Kenny_G_Loggins
# Created on: 7/23/20, 11:52 AM
# File: tkin_test.py
# Project: Beginner_Loggin_non_secure

from login_non_secure import username_cache
from tkinter import *
import sqlite3

root = Tk()
root.title('tkinter test')
root.geometry('550x70')
img = PhotoImage(file='/home/kgl/Pictures/pug.png')
root.tk.call('wm', 'iconphoto', root._w, img)


# Create database or connect to one
userdb = sqlite3.connect('user_name_password.db')

# Create cursor
c = userdb.cursor()

'''
# Create Table
c.execute(CREATE TABLE addresses (user_name text, password1 text))
'''
def submit(event):

    # Create database or connect to one
    userdb = sqlite3.connect('user_name_password.db')

    # Create cursor
    c = userdb.cursor()

    if not query():
        # do_match.remove_grid()
        # Insert Into Table:
        c.execute('INSERT INTO addresses VALUES (:user_name, :password1)', {'user_name': u_name.get(),
                                                                            'password1': p_word.get()})
    else:
        do_match = Label(root, text="Username already exists, try again.")
        do_match.grid(row=0, column=3, padx=3)

    # Commit Changes
    userdb.commit()

    # Close Connection
    userdb.close()

    # Clear the ext Boxes
    u_name.delete(0, END)
    p_word.delete(0, END)


def query():

    # Create database or connect to one
    userdb = sqlite3.connect('user_name_password.db')

    # Create cursor
    c = userdb.cursor()

    c.execute("SELECT user_name, user_name FROM addresses")
    usernames = c.fetchall()
    print(usernames)
    lst = [name for name in usernames]
    tup = [tup1 for (tup1, tup2) in lst]
    repeat = [uname for uname in tup if uname == u_name.get()]
    # Commit Changes
    userdb.commit()

    # Close Connection
    userdb.close()

    print(repeat)
    return repeat


#create txt boxes
u_name = Entry(root, width=20)
u_name.grid(row=0, column=1, padx=10)

p_word = Entry(root, width=20)
p_word.grid(row=1, column=1, padx=10)

# Create txt box labels
u_name_label = Label(root, text='Username:')
u_name_label.grid(row=0, column=0)
p_word_label = Label(root, text='Password:')
p_word_label.grid(row=1, column=0)


# Create Submit Button
submit_btn = Button(root, text='Submit', command=submit)
root.bind('<Return>', submit)
submit_btn.grid(row=3, column=0, columnspan=2, ipadx=100)

# Commit Changes
userdb.commit()

# Close Connection
userdb.close()

root.mainloop()


'''
def user_and_pass():
    with open('logandpass.txt', 'a+') as login_and_password:
        login_and_password.write(username + '=' + password + '\n')


def username_check():
    if username_cache().count(entry_username.get()) > 0:
        label_wrong_username.grid(row=1, column=1)
    if username_cache().count(entry_username.get()) == 0:
        username = str(entry_username.get())
        label_wrong_username.grid_remove()



def password():
    label_username.grid_remove()
    entry_username.grid_remove()
    username_enter_button.grid_remove()
    label_password1 = Label(root, text='Enter in a valid password:')
    label_password1.grid(row=0, column=0)
    entry_password1 = Entry(root, width=80, borderwidth=3)
    entry_password1.grid(row=0, column=1)
    label_password2 = Label(root, text='Re-enter your password:')
    label_password2.grid(row=2, column=0)
    entry_password2 = Entry(root, width=80, borderwidth=3)
    entry_password2.grid(row=2, column=1)
    passwords_dmatch = Label(root, text='Passwords do not match, try again')
    if entry_password1.get() != entry_password2.get():
        passwords_dmatch.grid(row=3, column=1)
    if entry_password1.get() == entry_password2.get():
        passwords_dmatch.grid_remove()
        password = str(entry_password1.get())










label_username = Label(root, text='Please enter a Login Name: ')
entry_username = Entry(root, width=40, borderwidth=3)
entry_username.bind('<Return>', username_check)
username_enter_button = Button(root, text='Submit')
label_wrong_username = Label(root, text='Username has already been taken, please try again:')

# root.bind('<Return>', getinfo)
label_username.grid(row=0, column=0, pady=20, padx=10)
entry_username.grid(row=0, column=1)
username_enter_button.grid(row=0, column=2)
'''





####       ####
#### Notes ####
####       ####

'''myLabel1 = Label(root, text='Hello world!')  # can add .grid(row=0, column=0) at the end if wanted
myLabel2 = Label(root, text='yo this is a test!')

# rows and columns are relative. ex: column 1 starts where column 0 ends and 2 where 1 ends but only if there
# is something in those columns. else: 2 will start where 0 ends if there is nothing in 1 and something in 0
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)'''

'''myButton = Button(root, text='Click Me!', padx=20) # can add ', state=DISABLED' as an argument
# can also set ', command=function' as an argument to execute a function when the button is pressed
# or command=Lambda: function(argument)
# fg='blue', bg='red' for arguments as well. fg sets txt color and bg sets the button color

myButton.grid(row=0, column= 0)'''

# test to run a function on click which grabs user input and prints
'''def myClick():
    myLabel = Label(root, text='what did you type? ' + e.get())
    myLabel.pack()'''

'''button = Button(root, text='click me!', command=myClick)
button.pack()
e = Entry(root, width=50, bg='white', fg='black', borderwidth=5) # google extra arguments
e.pack()
e.insert(0, "Type Something")'''

# exit program button = Button(root, text='Exit', command=root.quit)

#frames (line around the edge of a window) = LabelFrame(root, text='login', padx=50, pady=50)