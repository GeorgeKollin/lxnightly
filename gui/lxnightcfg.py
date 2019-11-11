from tkinter import *
from sys import exit
from os import path
from subprocess import call

if not (path.isfile("./src/a9eed7dbbb875d537a60baf6442c86cb")):
    print("Please, run Linux Nightly by double-clicking the desktop files in the root directory of the program.")
    sys.exit(1)

class ConfigWin:
    def __init__(self):
        # Create window
        self.window = Tk()
        # Window title
        self.window.title("Linux Nightly v3.0 for f.lux")
        # Header image
        headimg = PhotoImage(file="./icons/lxheader.png")
        hdlbl = Label(self.window, image=headimg)
        hdlbl.photo = headimg
        hdlbl.grid(row=0, column=0, columnspan=4)
        # "Latitude" label
        latlbl = Label(self.window, text="Latitude of your\ncurrent position\n(Degrees - optional):")
        latlbl.grid(row=1, column=0, pady=5)
        # Initializing lists
        inlist = ["1"]
        # Get saved data from files for latitude
        try:
            infile = open("./conf/lat_deg", "r")
            inlist = [line.rstrip() for line in infile]
            infile.close()
        except:
            print("Failed to open \"./conf/lat_deg\".")
        # "Latitude" scale widget
        self.latin = Scale(self.window, from_=-90, to=90, troughcolor="white", orient=HORIZONTAL, resolution=1)
        self.latin.grid(row=1, column=1, pady=5)
        self.latin.set(inlist[0])
        # Get saved data from files for longitude
        try:
            valfile = open("./conf/lgtd_deg", "r")
            inlist = [line.rstrip() for line in valfile]
            valfile.close()
        except:
            print("Failed to open \"./conf/lgtd_deg\".")
        # "Longitude" label
        lgtdlbl = Label(self.window, text="Longitude of your\ncurrent position\n(Degrees):")
        lgtdlbl.grid(row=1, column=2, pady=5)
        # "Longitude" scale widget
        self.lgtdin = Scale(self.window, from_=-179, to=180, troughcolor="white", orient=HORIZONTAL, resolution=1)
        self.lgtdin.grid(row=1, column=3, pady=5)
        self.lgtdin.set(inlist[0])
        # "ZIP Code" label
        ziplbl = Label(self.window, text="ZIP Code of your\ncurrent location\n(optional):")
        ziplbl.grid(row=2, column=0, pady=5)
        ziplist = ["0"]
        # Get saved data from files for ZIP Code
        try:
            infile = open("./conf/zip_code", "r")
            ziplist = [line.rstrip() for line in infile]
            infile.close()
        except:
            print("Failed to open \"./conf/zip_code\".")
        # "ZIP Code" entry widget
        self.zipval = StringVar(value=str(ziplist[0]))
        self.zipin = Entry(self.window, width=9, bg="white", textvariable=self.zipval)
        self.zipin.grid(row=2, column=1, pady=5)
        # Get saved data from files for temperature
        try:
            valfile = open("./conf/tmprt_indx", "r")
            inlist = [line.rstrip() for line in valfile]
            valfile.close()
        except:
            print("Failed to open \"./conf/tmprt_indx\".")
        # "Screen colour temperature" label
        tmplbl = Label(self.window, text="Screen colour\ntemperature\n(Kelvin):")
        tmplbl.grid(row=2, column=2, pady=5)
        # "Screen colour temperature" scale widget
        self.tmpin = Scale(self.window, from_=2000, to=10000, troughcolor="white", orient=HORIZONTAL, resolution=100)
        self.tmpin.grid(row=2, column=3, pady=5)
        self.tmpin.set(inlist[0])
        self.inlist = ["0"]
        # Get saved data from theme configuration files
        try:
            valfile = open("./conf/thm_cfg", "r")
            self.inlist = [line.rstrip() for line in valfile]
            valfile.close()
        except:
            print("Failed to open \"./conf/thm_cfg\".")
        # "Change theme" label
        thmlbl = Label(self.window, text="Change desktop icon\ntheme (optional):")
        thmlbl.grid(row=3, column=0, pady=5)
        self.thmlistinit = StringVar()
        thmlistvar = (" Dark", " Light")
        self.thmlistinit.set(thmlistvar)
        # List of available icon themes
        self.thmlist = Listbox(self.window, width=8, height=2, listvariable=self.thmlistinit, bg="white")
        self.thmlist.grid(row=3, column=1, pady=5)
        # Generate <<ListboxSelect>> event to get current icon theme
        if ( "l" in self.inlist[0] ):
            self.thmlist.select_set(1)
            self.thmlist.event_generate("<<ListboxSelect>>")
        else:
            self.thmlist.select_set(0)
            self.thmlist.event_generate("<<ListboxSelect>>")
        randrlist = ["0"]
        # Get current randr option state from files
        try:
            infile = open("./conf/randr_en", "r")
            randrlist = [line.rstrip() for line in infile]
            infile.close()
        except:
            print("Failed to open \"./conf/randr_en\".")
        # Randr option checkbox
        self.randrin = IntVar()
        self.randrc = Checkbutton(self.window, text="[-r 1]\n(use randr)", variable=self.randrin)
        self.randrc.grid(row=3, column=2, pady=5)
        if (str(randrlist[0]) == "1"):
            self.randrc.select()
        nflist = ["0"]
        # Get current nofork option state from files
        try:
            infile = open("./conf/no_fork", "r")
            nflist = [line.rstrip() for line in infile]
            infile.close()
        except:
            print("Failed to open \"./conf/no_fork\".")
        # Nofork option checkbox (disabled by default)
        #self.nofin = IntVar()
        self.nofc = Checkbutton(self.window, text="[-nofork]", state="disabled")
        self.nofc.grid(row=3, column=3, pady=5)
        #if (str(nflist[0]) == "1"):
        #    self.nofc.select()
        self.cmdindx = []
        zip2list = ["0"]
        # Get current ZIP Code option state from files
        try:
            infile = open("./conf/zip_all", "r")
            zip2list = [line.rstrip() for line in infile]
            infile.close()
        except:
            print("Failed to open \"./conf/zip_all\".")
        # ZIP Code option checkbox
        self.iszipin = IntVar()
        self.iszipic = Checkbutton(self.window, text="Use ZIP Code instead of\nlatitude & longitude", variable=self.iszipin)
        self.iszipic.grid(row=4, column=0, columnspan=2)
        if (str(zip2list[0]) == "1"):
            self.iszipic.select()
        # "Show command line output" checkbox widget
        self.chckout = IntVar()
        self.ifcmd = Checkbutton(self.window, text="Show command line output", variable=self.chckout)
        self.ifcmd.grid(row=4, column=2, columnspan=2)
        # "Use daytime filter" checkbox widget
        self.fluxday = IntVar()
        self.forceday = Checkbutton(self.window, text="Use daytime filter (BETA) | Duration: 7 - 8 hours", variable=self.fluxday)
        self.forceday.grid(row=5, column=0, columnspan=4)
        # "Turn off f.lux" button
        self.closebtn = Button(self.window, text="Turn off f.lux", bg="white", command=self.killTask)
        self.closebtn.grid(row=6, column=0, pady=(5, 0), sticky="NSEW", columnspan=2)
        # "Exit" button
        self.extbtn = Button(self.window, text="Exit", bg="white", command=self.window.destroy)
        self.extbtn.grid(row=6, column=2, pady=(5, 0), sticky="NSEW", columnspan=2)
        # "Apply changes" button
        self.startbtn = Button(self.window, text="Apply changes & turn on f.lux", bg="white", command=self.fluxExec)
        self.startbtn.grid(row=7, column=0, columnspan=4, sticky="NSEW")
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

    def fluxExec(self):
        # Get local data
        latout = str(self.latin.get())
        if (latout == "0"):
            latout = "1"
        lgtdout = str(self.lgtdin.get())
        if (lgtdout == "0"):
            lgtdout = "1"
        thiszip = str(self.zipval.get())
        try:
            int(thiszip)
        except:
            thiszip = "0"
        tmprout = str(self.tmpin.get())
        try:
            thmout = str(self.thmlist.get(self.thmlist.curselection()))
        except:
            if ( "l" in self.inlist[0] ):
                self.thmlist.select_set(1)
                self.thmlist.event_generate("<<ListboxSelect>>")
            else:
                self.thmlist.select_set(0)
                self.thmlist.event_generate("<<ListboxSelect>>")
            thmout = str(self.thmlist.get(self.thmlist.curselection()))
        if ("Dark" in thmout):
            thmout = "d"
        else:
            thmout = "l"
        thisrandr = str(self.randrin.get())
        #thisnof = str(self.nofin.get())
        thiszipin = str(self.iszipin.get())
        thiscmd = str(self.chckout.get())
        thisday = str(self.fluxday.get())
        ################
        # Disable elements while waiting for f.lux response
        if ("1" in self.cmdindx):
            self.yscroll = Scrollbar(self.window, orient=VERTICAL)
            self.yscroll.grid(row=9, column=3, pady=5, sticky="NSW")
            self.cmdtxt = Text(self.window, wrap=WORD, width=40, height=5, state="disabled")
            self.cmdtxt.grid(row=9, column=0, padx=(5, 0), pady=5, sticky="E", columnspan=3)
        self.latin = Scale(self.window, from_=-90, to=90, orient=HORIZONTAL, resolution=1, state="disabled")
        self.latin.grid(row=1, column=1, pady=5)
        self.lgtdin = Scale(self.window, from_=-179, to=180, orient=HORIZONTAL, resolution=1, state="disabled")
        self.lgtdin.grid(row=1, column=3, pady=5)
        self.zipin = Entry(self.window, width=9, state="disabled")
        self.zipin.grid(row=2, column=1, pady=5)
        self.tmpin = Scale(self.window, from_=2000, to=10000, orient=HORIZONTAL, resolution=100, state="disabled")
        self.tmpin.grid(row=2, column=3, pady=5)
        self.thmlist = Listbox(self.window, width=8, height=2, listvariable=self.thmlistinit, state="disabled")
        self.thmlist.grid(row=3, column=1, pady=5)
        self.randrc = Checkbutton(self.window, text="[-r 1]\n(use randr)", state="disabled")
        self.randrc.grid(row=3, column=2, pady=5)
        #self.nofc = Checkbutton(self.window, text="[-nofork]", state="disabled")
        #self.nofc.grid(row=3, column=3, pady=5)
        self.iszipic = Checkbutton(self.window, text="Use ZIP Code instead of\nlatitude & longitude", state="disabled")
        self.iszipic.grid(row=4, column=0, columnspan=2)
        self.ifcmd = Checkbutton(self.window, text="Show command line output", state="disabled")
        self.ifcmd.grid(row=4, column=2, columnspan=2)
        self.forceday = Checkbutton(self.window, text="Use daytime filter (BETA) | Duration: 7 - 8 hours", state="disabled")
        self.forceday.grid(row=5, column=0, columnspan=4)
        self.closebtn = Button(self.window, text="Turn off f.lux", state="disabled")
        self.closebtn.grid(row=6, column=0, pady=(5, 0), sticky="NSEW", columnspan=2)
        self.extbtn = Button(self.window, text="Exit", state="disabled")
        self.extbtn.grid(row=6, column=2, pady=(5, 0), sticky="NSEW", columnspan=2)
        self.startbtn = Button(self.window, text="Please, wait for 25 seconds...", state="disabled")
        self.startbtn.grid(row=7, column=0, columnspan=4, sticky="NSEW")
        ###################################################
        # Open files to save new data
        try:
            outfile = open("./conf/lat_deg", "w")
            outfile.write(latout)
            outfile.close()
        except:
            print("Failed to open \"./conf/lat_deg\".")
        try:
            outfile = open("./conf/lgtd_deg", "w")
            outfile.write(lgtdout)
            outfile.close()
        except:
            print("Failed to open \"./conf/lgtd_deg\".")
        try:
            outfile = open("./conf/zip_code", "w")
            outfile.write(thiszip)
            outfile.close()
        except:
            print("Failed to open \"./conf/zip_code\".")
        try:
            outfile = open("./conf/tmprt_indx", "w")
            outfile.write(tmprout)
            outfile.close()
        except:
            print("Failed to open \"./conf/tmprt_indx\".")
        try:
            outfile = open("./conf/thm_cfg", "w")
            outfile.write(thmout)
            outfile.close()
        except:
            print("Failed to open \"./conf/thm_cfg\".")
        try:
            outfile = open("./conf/randr_en", "w")
            outfile.write(thisrandr)
            outfile.close()
        except:
            print("Failed to open \"./conf/randr_en\".")
        #try:
        #    outfile = open("./conf/no_fork", "w")
        #    outfile.write(thisnof)
        #    outfile.close()
        #except:
        #    print("Failed to open \"./conf/no_fork\".")
        try:
            outfile = open("./conf/zip_all", "w")
            outfile.write(thiszipin)
            outfile.close()
        except:
            print("Failed to open \"./conf/zip_all\".")
        #############################
        # Apply new theme to desktop icons
        if (thmout == "d"):
            call(["./src/dark.sh"])
        else:
            call(["./src/light.sh"])
        # Apply nightmode filter
        if (thisday == "0"):
            call(["./conf/exec2.sh"])
        else:
            call(["./conf/exec.sh"])
        execlist = ["0"]
        # Get f.lux exit code
        try:
            execin = open("./conf/flux_exit.txt", "r")
            execlist = [line.rstrip() for line in execin]
            execin.close()
        except:
            print("Failed to open \"./conf/flux_exit.txt\".")
        toexe = StringVar()
        toexe.set(str("\n".join(execlist)))
        # Get f.lux command line output
        try:
            execin = open("./conf/exec_out.txt", "r")
            execlist = [line.rstrip() for line in execin]
            execin.close()
        except:
            print("Failed to open \"./conf/exec_out.txt\".")
        execout = str("\n".join(execlist))
        self.window.update()
        # Pause program for 25 seconds
        call(["./src/pleasewait.sh"])
        self.cmdindx.append(thiscmd)
        # "Show command line output" window extension
        if (thiscmd == "1"):
            cmdlbl = Label(self.window, text="Command line output:")
            cmdlbl.grid(row=8, column=0, columnspan=4, pady=(10, 10))
            self.yscroll = Scrollbar(self.window, orient=VERTICAL, troughcolor="white")
            self.yscroll.grid(row=9, column=3, pady=5, sticky="NSW")
            self.cmdtxt = Text(self.window, bg="white", wrap=WORD, width=40, height=5, yscrollcommand=self.yscroll.set)
            self.cmdtxt.grid(row=9, column=0, padx=(5, 0), pady=5, sticky="E", columnspan=3)
            self.yscroll["command"] = self.cmdtxt.yview
            self.cmdtxt.insert(INSERT, execout)
            exelbl = Label(self.window, text="F.lux exit status:")
            exelbl.grid(row=10, column=0, pady=5, columnspan=2)
            exetxt = Entry(self.window, textvariable=toexe, width=10, bg="white", state="readonly")
            exetxt.grid(row=10, column=2, pady=5, columnspan=2)
            copyr = Label(self.window, text="© 2019 Linux Nightly.\nAll rights reserved.\nView source code on:")
            copyr.grid(row=11, column=0, pady=(10, 5), columnspan=4)
            txtgit = StringVar(value="https://github.com/georgekollin/lxnightly/")
            entgit = Entry(self.window, text=txtgit, state="readonly", width=45)
            entgit.grid(row=12, column=0, columnspan=4, pady=(0, 10))
        # Enable window elements after filter application
        self.latin = Scale(self.window, from_=-90, to=90, troughcolor="white", orient=HORIZONTAL, resolution=1)
        self.latin.grid(row=1, column=1, pady=5)
        self.latin.set(latout)
        self.lgtdin = Scale(self.window, from_=-179, to=180, troughcolor="white", orient=HORIZONTAL, resolution=1)
        self.lgtdin.grid(row=1, column=3, pady=5)
        self.lgtdin.set(lgtdout)
        zipvar = StringVar(value=thiszip)
        self.zipin = Entry(self.window, width=9, bg="white", textvariable=zipvar)
        self.zipin.grid(row=2, column=1, pady=5)
        self.tmpin = Scale(self.window, from_=2000, to=10000, troughcolor="white", orient=HORIZONTAL, resolution=100)
        self.tmpin.grid(row=2, column=3, pady=5)
        self.tmpin.set(tmprout)
        self.thmlist = Listbox(self.window, width=8, height=2, listvariable=self.thmlistinit, bg="white")
        self.thmlist.grid(row=3, column=1, pady=5)
        if (thmout == "l"):
            self.thmlist.select_set(1)
            self.thmlist.event_generate("<<ListboxSelect>>")
        else:
            self.thmlist.select_set(0)
            self.thmlist.event_generate("<<ListboxSelect>>")
        if (thisrandr == "0"):
            self.randrc = Checkbutton(self.window, text="[-r 1]\n(use randr)", variable=self.randrin)
            self.randrc.grid(row=3, column=2, pady=5)
        else:
            self.randrc = Checkbutton(self.window, text="[-r 1]\n(use randr)", variable=self.randrin)
            self.randrc.grid(row=3, column=2, pady=5)
            self.randrc.select()
        #if(thisnof == "0"):
        #    self.nofc = Checkbutton(self.window, text="[-nofork]", variable=self.nofin)
        #    self.nofc.grid(row=3, column=3, pady=5)
        #else:
        #    self.nofc = Checkbutton(self.window, text="[-nofork]", variable=self.nofin)
        #    self.nofc.grid(row=3, column=3, pady=5)
        #    self.nofc.select()
        if (thiszipin == "0"):
            self.iszipic = Checkbutton(self.window, text="Use ZIP Code instead of\nlatitude & longitude", variable=self.iszipin)
            self.iszipic.grid(row=4, column=0, columnspan=2)
        else:
            self.iszipic = Checkbutton(self.window, text="Use ZIP Code instead of\nlatitude & longitude", variable=self.iszipin)
            self.iszipic.grid(row=4, column=0, columnspan=2)
        if ("1" in self.cmdindx):
            self.ifcmd = Checkbutton(self.window, text="Show command line output", state="disabled")
            self.ifcmd.grid(row=4, column=2, columnspan=2, pady=5)
        else:
            self.ifcmd = Checkbutton(self.window, text="Show command line output", variable=self.chckout)
            self.ifcmd.grid(row=4, column=2, columnspan=2, pady=5)
        if (thisday == "0"):
            self.forceday = Checkbutton(self.window, text="Use daytime filter (BETA) | Duration: 7 - 8 hours", variable=self.fluxday)
            self.forceday.grid(row=5, column=0, columnspan=4)
        else:
            self.forceday = Checkbutton(self.window, text="Use daytime filter (BETA) | Duration: 7 - 8 hours", variable=self.fluxday)
            self.forceday.grid(row=5, column=0, columnspan=4)
            self.forceday.select()
        self.closebtn = Button(self.window, text="Turn off f.lux", bg="white", command=self.killTask)
        self.closebtn.grid(row=6, column=0, pady=(5, 0), sticky="NSEW", columnspan=2)
        self.extbtn = Button(self.window, text="Exit", bg="white", command=self.window.destroy)
        self.extbtn.grid(row=6, column=2, pady=(5, 0), sticky="NSEW", columnspan=2)
        self.startbtn = Button(self.window, text="Apply changes & turn on f.lux", bg="white", command=self.fluxExec)
        self.startbtn.grid(row=7, column=0, columnspan=4, sticky="NSEW")
        #################################################
    # Terminate all f.lux sessions
    def killTask(self):
        call(["./src/daymode.sh"])

ConfigWin()