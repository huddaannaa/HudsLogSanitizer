import re
import random
import subprocess
import sys
import string


def handler(signum, frame):
    print ("[] Since you pressed CTRL+C ")
    print ("[] This program will terminate gracefully ...")
    print """

# Copyright (c) 2020, Hud Seidu Daannaa
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of www.daannaa.space nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""
    sys.exit(1989)


def generate(o):
    
    # the first output is lower and the second is upper

    def random_numbers(ln):
        d=''
        for x in range(len(str(ln))):
            d = d+str(random.randint(1,9))
        return d

    def random_block_letters(lnx):
        dx=''
        for x in range(len(str(lnx))):
            dx = dx + random.choice([n for n in string.ascii_uppercase])
        return dx
    
    wrd=''
    for i in o:
        try:wrd=wrd+random_numbers(int(i))
        except ValueError:wrd=wrd+random_block_letters(str(i))
            
    return wrd.lower(), wrd.upper()
# signal.signal(signal.SIGINT, handler)


def ip_gen():
    c = random.randint(1,254)
    d = random.randint(1,254)
    ipd = "192.168.{0}.{1}".format(c,d)
    return ipd


def random_int_gen(hud):
    # import random
    # This funtion take a number either str/int and then generates
    # a random number using the same lenth as the originl.
    return random.randint(int('1'*len(str(hud))),int('9'*len(str(hud))))


def read(file_):
    # thisis a function that
    # produces list from a file
    f = open(file_, 'rt')
    a =''
    for n in f.readlines():
        a = a+n
    f.close()
    return a.split('\n')


def replacex(old, new, file_):
    fin = open(file_, "rt")
    fout = open("{}.sanitized".format(file_), "wt")
    for line in fin:
        fout.write(line.replace(old, new))
    # fin.close()
    # fout.close()

    
def replace(old, new, file_):
    o = open("output","w")
    data = open(file_).read()
    o.write( re.sub(old, new, data))
    o.close()


def sed(old, new, log_file):
    try:
        command = "sed -i 's/{0}/{1}/g' {2}".format(old, new, log_file)
        out, err = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
    except Exception as vm_state_err:
        print ('[+] Could not replace {0} to {1} in the {2} file')


def topos():
    try:
        command = "cat topologies.py | grep ':' | grep 'def' | awk '{print $2}'| cut  -d'(' -f1"
        out, err = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
	reez=[]
	for nn in out.split('\n'):
	    if len(nn) != 0:
	        reez.append(nn.strip())
	    else:pass	
	return reez
    except Exception as vm_state_err:
        print ('Can not get topo list')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def head(lines, log_file):
    try:
	# mv winlog.log temp; head -n4 temp > winlog.log
	command = "mv {0} temp; head -n{1} temp > {0};rm -rf temp".format(log_file, lines)
        # command = "head -n{0} {1} > {1}".format(str(lines), log_file)
        out, err = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
    except Exception as err:
        print ('[+] Could not use head command')

    # try:
    #     commandx = "rm -rf {}".format(log_file)
    #     outx, errx = subprocess.Popen(commandx, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
    # except Exception as err:
    #     print ('[+] Could not use rm command')
