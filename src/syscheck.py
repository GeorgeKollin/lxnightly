try:
    from sys import *
except:
    outfile = open("./src/sys_exc", "w")
    outfile.write("1")
    outfile.close()
