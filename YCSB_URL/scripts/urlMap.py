# args[0]: url list
# args[1]: size of url sample space
# args[2]: initialization (load) file
# args[3]: workload (txn) file
# args[4]: initialization (load) output file
# args[5]: workload (txn) output file

import sys

f_args = open (sys.argv[1])
count = 0
args = {}
for line in f_args :
    args[count] = line.strip()
    count += 1

num_urls = args[1]

f_urls = open (args[0], 'r')
count = 0
urls = {}
for line in f_urls :
    urls[count] = line.strip()
    count += 1
f_urls.close()

key_url_map = dict()
count = 0

f_load = open (args[2], 'r')
f_load_out = open (args[4], 'w')
for line in f_load :
    cols = line.split()
    if cols[0] == "INSERT":
        key_url_map[cols[2][4:]] = urls[count]
        count += 1
        f_load_out.write (cols[0] + " " +  key_url_map[cols[2][4:]] + "\n")
f_load.close()
f_load_out.close()

f_txn = open (args[3], 'r')
f_txn_out = open (args[5], 'w')
for line in f_txn :
    cols = line.split()
    if (cols[0] == "SCAN") or (cols[0] == "INSERT") or (cols[0] == "READ") or (cols[0] == "UPDATE"):
        if cols[2][4:] in key_url_map:
            starturl = key_url_map[cols[2][4:]]
        if cols[0] == "SCAN" :
            numurl = cols[3]
            f_txn_out.write (cols[0] + " " + starturl + " " + numurl + "\n")
        else :
            f_txn_out.write (cols[0] + " " + starturl + "\n")
f_txn.close()
f_txn_out.close()

