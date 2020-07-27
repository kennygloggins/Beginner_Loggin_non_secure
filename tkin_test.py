# By: Kenny_G_Loggins
# Created on: 7/23/20, 11:52 AM
# File: tkin_test.py
# Project: Beginner_Loggin_non_secure

from tkinter import *
import sqlite3
import bcrypt


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


def submit(event=None):

    global do_match

    q = query()
    p = passwords()
    password = p_word.get()
    hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())


    if q is None and not p:
        # Insert Into Table:
        with userdb:
            c.execute('INSERT INTO uandp VALUES (:user_name, :password1)', {'user_name': u_name.get(),
                                                                                    'password1': hashed})
        # Clear the ext Boxes
        u_name.delete(0, END)
        p_word.delete(0, END)
        p_word2.delete(0, END)


def query():

    global name_length

    # Store entered username
    nameg = str(u_name.get())
    # Grab a list of names in tuple form from uandp
    c.execute("SELECT * FROM uandp WHERE user_name=?", (nameg,))
    usernames = c.fetchone()
    print(usernames)

    if not usernames and len(nameg) > 4:
        name_length.grid_forget()
        do_match.grid_forget()
        return usernames
    elif len(nameg) <= 4:
        do_match.grid_forget()
        name_length.grid(row=0, column=3, sticky=W)
        return usernames
    else:
        name_length.grid_forget()
        do_match.grid(row=0, column=3, sticky=W)
        return usernames

def passwords():

    global do_matchp
    global password_length

    # Grab both passwords and check if they are equal
    if p_word.get() == p_word2.get() and len(p_word.get()) > 4:
        password_length.grid_forget()
        do_matchp.grid_forget()
        return False
    elif p_word.get() == p_word2.get() and len(p_word.get()) <= 4:
        do_matchp.grid_forget()
        password_length.grid(row=2, column=3, sticky=W)
        return True
    else:
        password_length.grid_forget()
        do_matchp.grid(row=2, column=3, sticky=W)
        return True


# Create txt boxes
u_name = Entry(root, width=30)
u_name.grid(row=0, column=1, padx=1, pady=1)

p_word = Entry(root, width=30)
p_word.grid(row=2, column=1, padx=1, pady=1)

p_word2 = Entry(root, width=30)
p_word2.grid(row=4, column=1, padx=1, pady=1)

# Create txt box labels
u_name_label = Label(root, text='Username:')
u_name_label.grid(row=0, column=0, sticky=E)
u_name_label = Label(root, text='Username must be at least 5 characters')
u_name_label.grid(row=1, column=1)
p_word_label = Label(root, text='Password:')
p_word_label.grid(row=2, column=0, sticky=E)
p_word_label2 = Label(root, text='Password must be at least 5 characters')
p_word_label2.grid(row=3, column=1)
p_word2_label = Label(root, text='Re-enter Password:')
p_word2_label.grid(row=4, column=0, sticky=E)
do_match = Label(root, text="Username already exists, try again.")
do_matchp = Label(root, text="Passwords don't match, try again.")
password_length = Label(root, text="Password is too short.")
name_length = Label(root, text="Username is too short.")


# Create Submit Button
submit_btn = Button(root, text='Submit', command=submit)
root.bind('<Return>', submit)
submit_btn.grid(row=5, column=1, columnspan=1, ipadx=80)

root.mainloop()

# Commit Changes
userdb.commit()

# Close Connection outside of tkinter loop
userdb.close()