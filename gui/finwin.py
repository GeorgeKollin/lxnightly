from tkinter import *
from sys import exit
from os import path

if not (path.isfile("./src/a9eed7dbbb875d537a60baf6442c86cb")):
    print("Please, run Linux Nightly by double-clicking the desktop files in the root directory of the program.")
    sys.exit(1)

class InstallationWindow:
    def __init__(self, labtxt = "[Empty]", btntxt = "[Empty]", isdisabled = 0):
        # Create window
        window = Tk()
        # The given message should be at least 50 characters long!
        # Window title
        window.title("Install Linux Nightly v3.0")
        # Window messages
        msgtoshow = Label(window, text=labtxt)
        msgtoshow.grid(row=0, column=0, padx=25, pady=5)
        # "Close" button
        if (isdisabled == 0):
            closebtn = Button(window, text=btntxt, bg="white", command=window.destroy)
            closebtn.grid(row=1, column=0)
        else:
            closebtn = Button(window, text=btntxt, state="disabled")
            closebtn.grid(row=1, column=0)
        window.update()
        # Center window
        winwidth = window.winfo_width()
        winheight = window.winfo_height()
        scrwidth = window.winfo_screenwidth()
        scrheight = window.winfo_screenheight()
        padleft = int((scrwidth - winwidth) / 2)
        padtop = int((scrheight - winheight) / 2)
        gparam = "+" + str(padleft) + "+" + str(padtop)
        window.geometry(gparam)
        window.mainloop()

InstallationWindow("   Linux Nightly has successfully installed all   \nof its files on your system! Click \"Finish\" to\nclose the setup guide.", "Finish", 0)