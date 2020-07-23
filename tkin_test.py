# By: Kenny_G_Loggins
# Created on: 7/23/20, 11:52 AM
# File: tkin_test.py
# Project: Beginner_Loggin_non_secure


from tkinter import *

root = Tk()
root.title('tkinter test')


'''myLabel1 = Label(root, text='Hello world!')  # can add .grid(row=0, column=0) at the end if wanted
myLabel2 = Label(root, text='yo this is a test!')

# rows and columns are relative. ex: column 1 starts where column 0 ends and 2 where 1 ends but only if there
# is something in those columns. else: 2 will start where 0 ends if there is nothing in 1 and something in 0
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)'''

'''myButton = Button(root, text='Click Me!', padx=20) # can add ', state=DISABLED' as an argument
# can also set ', command=function' as an argument to execute a function when the button is pressed
# fg='blue', bg='red' for arguments as well. fg sets txt color and bg sets the button color

myButton.grid(row=0, column= 0)'''

# test to run a function on click which grabs user input and prints
def myClick():
    myLabel = Label(root, text='what did you type? ' + e.get())
    myLabel.pack()

button = Button(root, text='click me!', command=myClick)
button.pack()
e = Entry(root, width=50, bg='white', fg='black', borderwidth=5) # google extra arguments
e.pack()
e.insert(0, "Type Something")

root.mainloop()