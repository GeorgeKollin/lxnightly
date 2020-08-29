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
        window.title("Install Linux Nightly v3.5")
        # Window messages
        msgtoshow = Label(window, text=labtxt)
        msgtoshow.grid(row=0, column=0, padx=25, pady=5)
        # "Close" button
        if (isdisabled == 0):
            closebtn = Button(window, text=btntxt, command=window.destroy)
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

try:
    errin = open("./src/SETUP_err", "r")
    errlist = [line.rstrip() for line in errin]
    errin.close()
    errstr = "               INSTALLATION FAILED!               \n"
    for i in range (0, len(errlist)):
        errstr += str(errlist[i]) + "\n"
except:
    errstr = "               INSTALLATION FAILED!               \nFailed to open \"./src/SETUP_err\"."
    for i in range (0, len(errlist)):
        errstr += str(errlist[i]) + "\n"

InstallationWindow(errstr, "Exit", 0)

    for i in range (0, len(errlist)):
        errstr += str(errlist[i]) + "\n"

InstallationWindow(errstr, "Exit", 0)
