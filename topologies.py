from vocabulary import *
from functions import *
import re
# from functions import bcolors
# TOPOPLOGY
#

# print bcolors.OKGREEN + "         |" + bcolors.ENDC
def stringsd(parserx, partternx, elds, file_, variable):

    # NOTE:
    # parserx is the name of the parser in the
    # and also the string is converted to a variable
    # in order to access the strings in vocabulary

    # partternsx contains the regex sample

    # elds is the event data from the log file, that is being
    # looped from main.py

    # file_ is the name of the original logfile, which will
    # either be a victim of text replace or will be used as
    # a name.

    # he switcher takes a pattern and a parserx name,
    # This function will use data form vocabulary as an import
    # here after applying the pattern match it returns a list
    # so we have to re loop through the list

    # the below is done to know what to replace
    data = re.findall(r'{}'.format(partternx), elds)

    # this loop, then loops and breaks open the result of the regex
    for field in data:
        # pass
        # this is were is cross checks with vocabulary
        # old in form the log
        # new is from parcerx which is in vocabulary
        # but parcerx is a variable that contains a string
        # housed in vocabulary
        # so in a way, this is the strings we have in vocabulary
	# parserx = strings
        parserx = eval(str(parserx))
        old = field.strip()
	
        if old in parserx:
            new = parserx[old]
            sed(old, new, file_)
            print "[***] Replaced: ",old," [//=] with: ", new
        else:
            print "[+] Analyzed: ", old

def numbersd(parserx, partternx, elds, file_, variable):

    if variable == True:
        data = re.findall(r'{}'.format(partternx), elds)
        for field in data:
            old = field.strip()
            #new = random_int_gen(str(old))
	    new = generate(old)[0]
            # Replace here
            sed(old, new, file_)
            print "[***] Replaced: ",old," [//=] with: ",new
    else:
	print ""
	print "The option has been turned off by the analyst, if it is turned on"
	print "it will generate randon numbers and replace every instance of digits"
	print "in the specified log document ...."
	print "NOTE: This is a special feature from the author: Hud, we can gracefully"
	print "call this mode, the aggressive mode."
	print ""

def ipd(parserx, partternx, elds, file_, variable):

    data = re.findall(r'{}'.format(partternx), elds)
    for field in data:
        old = str(field.strip())
        new = str(ip_gen())
        # Replace here
        sed(old, new, file_)
        print "[***] Replaced: ", old, " [//=] with: ", new
            
def usernamed(parserx, partternx, elds, file_, variable):

    data = re.findall(r'{}'.format(partternx), elds)
    for field in data:
        old = str(field.strip())
        new = generate('HUD123456')[1]
        # Replace here
        sed(old, new, file_)
        print "[***] Replaced: ", old, " [//=] with: ", new

def useridd(parserx, partternx, elds, file_, variable):

    data = re.findall(r'{}'.format(partternx), elds)
    for field in data:
        old = str(field.strip())
        new = generate('00000')[0]
        # Replace here
        sed(old, new, file_)
        print "[***] Replaced: ", old, " [//=] with: ", new

def useriddd(parserx, partternx, elds, file_, variable):

    data = re.findall(r'{}'.format(partternx), elds)
    for field in data:
        old = str(field.strip())
        new = generate('10000')[0]
        # Replace here
        sed(old, new, file_)
        print "[***] Replaced: ", old, " [//=] with: ", new

def deploymentidd(parserx, partternx, elds, file_, variable):

    data = re.findall(r'{}'.format(partternx), elds)
    for field in data:
        old = str(field.strip())
        new = generate('0000000-0000-0000-00000')[0]
        # Replace here
        sed(old, new, file_)
        print "[***] Replaced: ", old, " [//=] with: ", new

def serviced(parserx, partternx, elds, file_, variable):

    data = re.findall(r'{}'.format(partternx), elds)
    for field in data:
        old = str(field.strip())
        new = generate('h')[0]+"_"+generate('xxxxx')[0]
        # Replace here
        sed(old, new, file_)
        print "[***] Replaced: ", old, " [//=] with: ", new



