from topologies import *
from get_parsers import *
from functions import topos
import sys
def hud():return 0

program={}
for progs in indicators:

    xxx = progs+'d'

    if xxx in topos():
        try:
	    program[progs] = eval(xxx)
        except:pass
            #print ""
            #print "(+) | WARNING | Please check 'parce.hud' and comment out patterns without topologies using '#' "
            #print ""
            #sys.exit(1)
    else:
	program[progs] = eval('hud')

   
# NOTE THIS IS FOR EXCEPTIONS, IF YOU WANT TO MODIFY
# DEFINITIONS IN PROGRAM(THIS IS A DICTIONARY THAT CONTAINS)
# MAPPINGS BETWEEN PARSER, PATTERNS AND TOPOLOGIES
# (custom define topologies below)
# HENCE:
#
# AN EXAMPLE IS:
#

#XXXXXXXX
#program['userid'] = useridd
#program['useridd'] = useridd

#
# where:
#	the key is the defined parcer/pattern
#	the value is the function defined in topologies
#
# IMPORTANT: 	This file does automatic mapping, the exception
#		section, redefines or overides the automatic mapping
#
#
for progs, fncs in program.iteritems():
    if program[progs] == hud:
	print ""
	print "[+] PLEASE REFER TO THE **definitions.py FILE"
	print "[+] AND HEARD TO THE XXXXXXXX SECTION OF THE FILE"
	print "[+] HENCE, PLEASE READ THE INSTRUCTIONS IN readme.hud"
	print "[+] OR COMMENTS IN THE FILE definitions.py"
	print "[+] NOTE: YOU CAN ALSO DEFINE A TOPOLOGY IN topologies.py"
	print "[+] WITH THE NAME OF THE PARCER IN parce.hud APPENDED WITH A d"
	print "[+] AN EXAMPLE IS: IF A PARCER IS blue THE RESPECTIVE TOPOLOGY"
	print "[+] WILL BE blued IN topologies.py"
	print ""
	sys.exit(1)
    else:
	check = 1

if check is 1:
    print ""
    print "[*] All configurations are set, This tool has a pass to commence operation" 
    print ""
