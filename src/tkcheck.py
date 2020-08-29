try:
    from tkinter import *
except:
    outfile = open("./src/tk_exc", "w")
    outfile.write("1")
    outfile.close()
