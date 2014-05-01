# argv[1]: url sample file

import string
import sys

fn = sys.argv[1]
fin = open(fn, 'r')
fout = open(fn[:-4] + "_reverse.dat", 'w')

for line in fin:
    if line.startswith('http://'):
        line = line[7:]
    elif line.startswith('https://'):
        line = line[8:]
    else:
        # discard anomaly lines
        print "ERROR! line: ", line
        continue

    # print '-', line
    hostname, sep, directory = line.partition('/')
    # print hostname
    hnparts = hostname.split('.')
    # print hnparts
    r_hostname = ''
    for part in hnparts:
        r_hostname = part + '.' + r_hostname
    # remove the '.' at then end
    r_hostname = r_hostname[:-1]
    # print r_hostname

    res = r_hostname + sep + directory
    #print res[:-1]
    fout.write(res)

fin.close()
fout.close()
