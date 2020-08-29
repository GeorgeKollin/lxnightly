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
        # "CHOOSE ICON THEME" label
        headlbl = Label(self.window, text="CHOOSE ICON THEME (For desktop shortcuts): ")
        headlbl.grid(row=0, column=0, padx=25, pady=5, columnspan=2)
        # List of available themes
        thmtuple = (" Dark icon theme (recommended for light background)", " Light icon theme (recommended for dark background)")
        thmcont = StringVar()
        thmcont.set(thmtuple)
        self.thmbox = Listbox(self.window, width=51, height=2, listvariable=thmcont, bg="white", fg="black")
        self.thmbox.grid(row=1, column=0, padx=25, pady=5, columnspan=2)
        self.thmbox.bind("<<ListboxSelect>>", self.showContinue)
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
    # Print previews and "Confirm & install" button when a listbox element is selected
    def showContinue(self, listevent):
        prelbl = Label(self.window, text="Preview: ")
        prelbl.grid(row=2, column=0)
        try:
            answ = str(self.thmbox.get(self.thmbox.curselection()))
        except:
            self.thmbox.select_set(0)
            self.thmbox.event_generate("<<ListboxSelect>>")
            answ = str(self.thmbox.get(self.thmbox.curselection()))
        if (answ.startswith(" Dark")):
            try:
                thmout = open("./conf/thm_cfg", "w")
                thmout.write("d")
                thmout.close()
            except:
                print("Failed to open \"./conf/thm_cfg\"")
            sampleimg = PhotoImage(file="./icons/darktheme.gif")
            samplelbl = Label(self.window, image=sampleimg)
            samplelbl.photo = sampleimg
            samplelbl.grid(row=2, column=1, pady=5)
        else:
            try:
                thmout = open("./conf/thm_cfg", "w")
                thmout.write("l")
                thmout.close()
            except:
                print("Failed to open \"./conf/thm_cfg\"")
            sampleimg = PhotoImage(file="./icons/lighttheme.gif")
            samplelbl = Label(self.window, image=sampleimg)
            samplelbl.photo = sampleimg
            samplelbl.grid(row=2, column=1, pady=5)
        contbtn = Button(self.window, text="Confirm and install", command=self.window.destroy)
        contbtn.grid(row=3, column=0, columnspan=2, pady=5)

InstallationWindow()

                thmout = open("./conf/thm_cfg", "w")
                thmout.write("l")
                thmout.close()
            except:
                print("Failed to open \"./conf/thm_cfg\"")
            sampleimg = PhotoImage(file="./icons/lighttheme.gif")
            samplelbl = Label(self.window, image=sampleimg)
            samplelbl.photo = sampleimg
            samplelbl.grid(row=2, column=1, pady=5)
        contbtn = Button(self.window, text="Confirm and install", bg="white", command=self.window.destroy)
        contbtn.grid(row=3, column=0, columnspan=2, pady=5)

InstallationWindow()
