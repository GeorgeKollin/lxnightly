from tkinter import *
from sys import exit
from os import path

if not (path.isfile("./src/a9eed7dbbb875d537a60baf6442c86cb")):
    print("Please, run Linux Nightly by double-clicking the desktop files in the root directory of the program.")
    sys.exit(1)

class InstallationWindow:
    def __init__(self):
        # Create window
        self.window = Tk()
        # The given message should be at least 50 characters long!
        # Window title
        self.window.title("Install Linux Nightly v3.5")
        # Header image (if it doesn't show up, replace file="./icons/lxheader.png" with file="./icons/lxheader.gif" on line 17)
        headimg = PhotoImage(file="./icons/lxheader.png")
        hdlbl = Label(self.window, image=headimg)
        hdlbl.photo = headimg
        hdlbl.grid(row=0, column=0, columnspan=2)
        # Window messages
        msgtoshow1 = Label(self.window, text="LINUX NIGHTLY V3.5.1343D7D\n\nLinux Nightly is a GUI program\nwritten for f.lux®. You can find\nmore information about f.lux® on\nits original website:")
        msgtoshow1.grid(row=1, column=0, pady=(5, 5), columnspan=2)
        txt1 = StringVar(value="https://justgetflux.com/")
        ent1 = Entry(self.window, text=txt1, state="readonly", width=24, fg="black")
        ent1.grid(row=2, column=0, columnspan=2)
        msgtoshow2 = Label(self.window, text="© 2020 Linux Nightly.\nAll rights reserved.\nView source code on:")
        msgtoshow2.grid(row=3, column=0, pady=(10, 5), columnspan=2)
        txt2 = StringVar(value="https://github.com/georgekollin/lxnightly/")
        ent2 = Entry(self.window, text=txt2, state="readonly", width=24, fg="black")
        ent2.grid(row=4, column=0, columnspan=2, pady=(0, 10))
        # "Exit" button
        closebtn = Button(self.window, text="Exit", command=self.noNormExit)
        closebtn.grid(row=5, column=0, sticky="NSEW")
        # "Install" button
        instbtn = Button(self.window, text="Install", command=self.normExit)
        instbtn.grid(row=5, column=1, sticky="NSEW")
        self.window.update()
        # Center window
        winwidth = self.window.winfo_width()
        winheight = self.window.winfo_height()
        scrwidth = self.window.winfo_screenwidth()
        scrheight = self.window.winfo_screenheight()
        padleft = int((scrwidth - winwidth) / 2)
        padtop = int((scrheight - winheight) / 2)
        gparam = "+" + str(padleft) + "+" + str(padtop)
        self.window.geometry(gparam)
        self.window.mainloop()
    # After "Install"
    def normExit(self):
        self.window.destroy()
        exit(0)
    # After "Exit"
    def noNormExit(self):
        self.window.destroy()
        exit(1)

InstallationWindow()

InstallationWindow()
