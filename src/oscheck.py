try:
    from os import *
except:
    outfile = open("./src/os_exc", "w")
    outfile.write("1")
    outfile.close()
