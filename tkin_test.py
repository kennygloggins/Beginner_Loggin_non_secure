# By: Kenny_G_Loggins
# Created on: 7/23/20, 11:52 AM
# File: tkin_test.py
# Project: Beginner_Loggin_non_secure

from tkinter import *
import sqlite3

# Create database or connect to one
userdb = sqlite3.connect('user_name_password.db')

# Create cursor
c = userdb.cursor()

root = Tk()
root.title('tkinter test')
root.geometry('535x150')
img = PhotoImage(file='/home/kgl/Pictures/pug.png')
root.tk.call('wm', 'iconphoto', root._w, img)


'''
# Create Table
c.execute(CREATE TABLE addresses (user_name text, password1 text))
'''


def submit(event=None):

    global do_match

    q = query()
    p = passwords()

    if q is None:
        do_match.grid_forget()
        if q is None and not p:
            # Insert Into Table:
            with userdb:
                c.execute('INSERT INTO addresses VALUES (:user_name, :password1)', {'user_name': u_name.get(),
                                                                                    'password1': p_word.get()})
            # Clear the ext Boxes
            u_name.delete(0, END)
            p_word.delete(0, END)
            p_word2.delete(0, END)

    else:
        do_match.grid(row=0, column=3, padx=3)


def query():

    # Store entered username
    nameg = str(u_name.get())
    # Grab a list of names in tuple form from addresses
    c.execute("SELECT * FROM addresses WHERE user_name=?", (nameg,))
    usernames = c.fetchone()
    print(usernames)

    if len(nameg) > 4:
        return usernames


def passwords():

    global do_matchp

    # Grab both passwords and check if they are equal
    if p_word.get() == p_word2.get() and len(p_word.get()) > 4:
        do_matchp.grid_forget()
        return False
    else:
        do_matchp.grid(row=2, column=3, padx=3)
        return True


# Create txt boxes
u_name = Entry(root, width=30)
u_name.grid(row=0, column=1, padx=5, pady=5)

p_word = Entry(root, width=30)
p_word.grid(row=2, column=1, padx=5, pady=5)

p_word2 = Entry(root, width=30)
p_word2.grid(row=4, column=1, padx=5, pady=5)

# Create txt box labels
u_name_label = Label(root, text='Username:')
u_name_label.grid(row=0, column=0)
u_name_label = Label(root, text='Username must be at least 5 characters')
u_name_label.grid(row=1, column=1)
p_word_label = Label(root, text='Password:')
p_word_label.grid(row=2, column=0)
p_word_label2 = Label(root, text='Password must be at least 5 characters')
p_word_label2.grid(row=3, column=1)
p_word2_label = Label(root, text='Re-enter Password:')
p_word2_label.grid(row=4, column=0)
do_match = Label(root, text="Username already exists, try again.")
do_matchp = Label(root, text="Passwords don't match, try again.")


# Create Submit Button
submit_btn = Button(root, text='Submit', command=submit)
root.bind('<Return>', submit)
submit_btn.grid(row=5, column=1, columnspan=1, ipadx=120)

root.mainloop()

# Commit Changes
userdb.commit()

# Close Connection
userdb.close()

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