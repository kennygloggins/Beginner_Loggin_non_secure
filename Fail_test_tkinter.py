# By: Kenny_G_Loggins
# Created on: 7/27/20, 9:24 PM
# File: Fail_test_tkinter.py
# Project: Beginner_Loggin_non_secure


import tkinter
import tkinter.ttk
from login_fun import login_submit

def home_widgets():
    '''
    # Create the label for the frame
    first_window_label = tkinter.ttk.Label(first_frame, text='Window 1')
    first_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.N))
    '''
    # Create the button for the frame
    login_button = tkinter.Button(first_frame, text='Login', command = call_second_frame_on_top)
    login_button.grid(row=0, column=1, pady=10, sticky=(tkinter.N))

    create_account_button = tkinter.Button(first_frame, text='Create Account', command = call_third_frame_on_top)
    create_account_button.grid(row=1, column=1, pady=10, sticky=(tkinter.N))

'''
    first_window_quit_button = tkinter.Button(first_frame, text = "Quit", command = quit_program)
    first_window_quit_button.grid(column=0, row=1, pady=10, sticky=(tkinter.N))
    first_window_next_button = tkinter.Button(first_frame, text = "Next", command = call_second_frame_on_top)
    first_window_next_button.grid(column=1, row=1, pady=10, sticky=(tkinter.N))
'''


def login_widgets():

    global match
    global dont_match_place
    global dont_match


    # Entry boxes
    u_name = tkinter.Entry(second_frame, width=30)
    u_name.grid(row=0, column=1, padx=1, pady=1, sticky=(tkinter.N))
    p_word = tkinter.Entry(second_frame, width=30)
    p_word.grid(row=2, column=1, padx=1, pady=1, sticky=(tkinter.N))
    dont_match_place = tkinter.Label(second_frame, text="-----------------------------------")
    dont_match = tkinter.Label(second_frame, text="Username or password doesn't match.")

    def check(a_name=0):
        if a_name == 1:
            dont_match_place.grid_forget()
            dont_match.grid(row=1, column=1, padx=1, pady=1, sticky=(tkinter.N))
        elif a_name == 2:
            dont_match.grid_forget()
            dont_match_place.grid(row=1, column=1, padx=1, pady=1, sticky=(tkinter.N))


    login_button = tkinter.Button(second_frame, text='Login', command=lambda:
                                  check(login_submit(u_name.get(), p_word.get())))
    login_button.grid(row=3, column=1, pady=5, sticky=(tkinter.N))

    '''if i == 1:
        dont_match_place.grid_forget()
        dont_match.grid(row=1, column=1, padx=1, pady=1, sticky=(tkinter.N))
    elif i == 0 or i == 2:
        dont_match.grid_forget()
        dont_match_place.grid(row=1, column=1, padx=1, pady=1, sticky=(tkinter.N))'''


        # dont_match.grid(row=1, column=1, padx=1, pady=1, sticky=(tkinter.N))


    create_account_button = tkinter.Button(second_frame, text='Create Account', command=call_third_frame_on_top)
    create_account_button.grid(row=4, column=1, pady=5, sticky=(tkinter.N))



    # Labels for entry boxes and warnings
    u_name_label = tkinter.Label(second_frame, text='Username:')
    u_name_label.grid(row=0, column=0, sticky=(tkinter.E))
    p_word_label = tkinter.Label(second_frame, text='Password:')
    p_word_label.grid(row=2, column=0, sticky=(tkinter.E))
    dont_match = tkinter.Label(second_frame, text="Username or password doesn't match.")
    dont_match_place = tkinter.Label(second_frame, text="   ")


    '''# Create the label for the frame
    second_window_label = tkinter.ttk.Label(second_frame, text='Window 2')
    second_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.N))

    # Create the button for the frame
    second_window_back_button = tkinter.Button(second_frame, text = "Back", command = call_first_frame_on_top)
    second_window_back_button.grid(column=0, row=1, pady=10, sticky=(tkinter.N))
    second_window_next_button = tkinter.Button(second_frame, text = "Next", command = call_third_frame_on_top)
    second_window_next_button.grid(column=1, row=1, pady=10, sticky=(tkinter.N))'''

def create_account_widgets():
    # Create the label for the frame
    third_window_label = tkinter.ttk.Label(third_frame, text='Window 3')
    third_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.N))

    # Create the button for the frame
    third_window_back_button = tkinter.Button(third_frame, text = "Back", command = call_second_frame_on_top)
    third_window_back_button.grid(column=0, row=1, pady=10, sticky=(tkinter.N))
    third_window_quit_button = tkinter.Button(third_frame, text = "Quit", command = quit_program)
    third_window_quit_button.grid(column=1, row=1, pady=10, sticky=(tkinter.N))

def call_first_frame_on_top():
    # This function can be called only from the second window.
    # Hide the second window and show the first window.
    second_frame.grid_forget()
    first_frame.grid(column=0, row=0, padx=5, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def call_second_frame_on_top():
    # This function can be called from the first and third windows.
    # Hide the first and third windows and show the second window.
    first_frame.grid_forget()
    third_frame.grid_forget()
    second_frame.grid(column=0, row=0, padx=5, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def call_third_frame_on_top():
    # This function can only be called from the second window.
    # Hide the second window and show the third window.
    second_frame.grid_forget()
    third_frame.grid(column=0, row=0, padx=5, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def quit_program():
    root_window.destroy()

###############################
# Main program starts here :) #
###############################

# Create the root GUI window.
root_window = tkinter.Tk()

# Define window size
window_width = 500
window_heigth = 500

# Create frames inside the root window to hold other GUI elements. All frames must be created in the main program, otherwise they are not accessible in functions.
first_frame=tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
first_frame['borderwidth'] = 5
# first_frame['relief'] = 'sunken'
first_frame.grid(column=0, row=0, padx=5, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

second_frame=tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
second_frame['borderwidth'] = 5
# second_frame['relief'] = 'sunken'
second_frame.grid(column=0, row=0, padx=5, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

third_frame=tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
third_frame['borderwidth'] = 5
# third_frame['relief'] = 'sunken'
third_frame.grid(column=0, row=0, padx=5, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# Create all widgets to all frames
create_account_widgets()
login_widgets()
home_widgets()

# Hide all frames in reverse order, but leave first frame visible (unhidden).
third_frame.grid_forget()
second_frame.grid_forget()

# Start tkinter event - loop
root_window.mainloop()