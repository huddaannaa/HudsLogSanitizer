from definitions import program
from get_parsers import indicators
from functions import bcolors, handler, head
from checker import checker
import argparse
import sys
import signal

parser = argparse.ArgumentParser(description="""

Hud-Log-Sanitizer (HLS v2.0)

This is a log sanitizer tool designed by Hud Seidu Daannaa,
to help data analyst and entities working in a log
defined environment. The goal is to boost data security by editing
log files (documents) for external/public use, outside
a given organization. The tool will convert a sample
log to a sanitized file.For usage refer to README.hud

""")

parser.add_argument('-l', '--lines', type=int, metavar='', help='Specify the number of line (events) to sanitize, if not specified, the tool will scan all lines in the specified document', default=0)
parser.add_argument('-f', '--logfile', type=str, metavar='', required=True, help='Specify the path of a log file to sanitize')
parser.add_argument('-c', '--check', action='store_false',  help='This option, provides the analyst with the components (fields) of the log file, by using the log event with the highest amount of data')
parser.add_argument('-n', '--numbers', action='store_true', help='This will switch/replace(randomize) all numbers in the log document')

args = parser.parse_args()

xfile_ = args.logfile
check = args.check
lines = args.lines
nums = args.numbers

signal.signal(signal.SIGINT, handler)

try:
    file_ = checker(xfile_, check)
    #
    #
    # #############################################################################################
    # #############################################################################################
    #
    # GET DATA FROM LOG FILE
    #
    #
    # file_='log'
    print "[+] Scanning log file: {}".format(file_)
    print "    ================="
    print ""
    print ""



    c = 0
    f = open(file_, 'r')
    for elds in f.readlines():
        c = c+1
        print ""
        # print "::::::::::::::::::::::::::::::::::::::::::::::::::::"

        print bcolors.OKBLUE + "" + bcolors.ENDC
        print bcolors.OKBLUE + "[+] For Log Event: {}".format(str(c))+ bcolors.ENDC
        print bcolors.OKBLUE + "[+] Configuring parsers for this event:" + bcolors.ENDC
        print bcolors.OKBLUE + "[=====]" + bcolors.ENDC

        for parserxx, partternxx in indicators.iteritems():
            print "    [%] ", parserxx,": ", partternxx

        print ""
        print bcolors.OKBLUE + "[+] Applying parsers:" + bcolors.ENDC
        print "    NOTE: These parsers will be applied to every"
        print "          instance of this document .."
        print ""
        # print "::::::::::::::::::::::::::::::::::::::::::::::::::::"
        print ""
        for parserx, partternx in indicators.iteritems():
            print bcolors.OKGREEN + "[+] For {}: ".format(parserx) + bcolors.ENDC

            if parserx == parserx:

                print "[X] Using parttern: ",partternx
                print "[X] Selecting topology: (^-^)"
                print ""
                print bcolors.OKBLUE + "OUTPUT:" + bcolors.ENDC
                print ""
                if parserx in program:
                    reslt = program[parserx](parserx, partternx, elds, file_, nums)

            else:pass
        print ""
        print "   "
        print "   "
        print "   "
        print "   "
        print "                  NOTE: This marks the end of the first event or document in the file"
        print "                        hence, the program will proceed to the next event or doc ...."
        print ""
        print ""
        print ""
	print ""

        if lines == c:
            head(lines, file_)
            sys.exit(1)
        elif lines == 0:pass
        else:pass

except Exception as er:
    print ""
    print "Please review all configs and README's"
    print er
    print ""
