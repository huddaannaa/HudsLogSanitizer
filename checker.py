from shutil import copyfile
from functions import bcolors
import os
import sys
import time
import re

def checker(xfile_, check):

    print ""
    print ""
    print "[+]  =========================="
    print "[+]  =========================="
    print "[+]",bcolors.WARNING + " == Hud's Log Sanitizer ===" + bcolors.ENDC
    print "[+]  =========================="
    print "[+]  =========================="
    print ""
    print ""
    print "[+] Check directory to save the sanitized (document):"

    try:os.mkdir('sanitized')
    except:pass
    print ""
    print ""

    try:
        print "[+] Checking log file"
        time.sleep(1)
        fz = open(xfile_, 'r')
        print "[*] Log file OK!"
        print ""
    except:
        print "[+] Please check file <Because it seems to be invalid !!!>"
        print "[+] This program will gracefully exit"
        print ""
        sys.exit(1)
    print ""

    # creating a copy of the file
    copyfile(xfile_, "sanitized/{}".format(os.path.basename(xfile_)))
    count = 0

    # hence new file is:
    file_ = "sanitized/{}".format(os.path.basename(xfile_))

    if check != True:
        print "[+] These are the respective components of the logs in {}".format(file_)
        print "[+] These should be used to configure the strings section of this tool"
        print " "
        pack={}
        fz = open(file_, 'r')
        for elds in fz.readlines():
            pack[len(elds.split())]=elds.split()
        c=0
        if max([int(n) for n in pack.keys()]) in pack:

            print "_______ _________"
            print "|Index | Fields |"
            print "______  _________"
            for nn in pack[max([int(n) for n in pack.keys()])]:
                #print nn
                for jj in re.findall(r'\b\w+\b',nn):
                    c=c+1
                    print "|",c, "   | " ,jj
            print "______________________"
        sys.exit(1)
    else:
        print ""
        print "[+] Alright No checks on log components its means they are already known"
        print "[+] and hence the necessary adjustments have been made in vocabulary.py"
        pass

    print ""
    print ""
    print ""

    return file_
