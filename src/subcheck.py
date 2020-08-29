try:
    from subprocess import *
except:
    outfile = open("./src/sub_exc", "w")
    outfile.write("1")
    outfile.close()
