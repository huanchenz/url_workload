# argv[1]: url collection
# argv[2]: url sample size

import sys

url_list_size = 105000000
url_sample_size = int(sys.argv[2])
gap = url_list_size / url_sample_size

f_urls = open (sys.argv[1], 'r')
count = 0
total_count = 0
for line in f_urls :
    count += 1
    if count == gap :
        print line.strip()
        count = 0
        total_count += 1
    if total_count >= url_sample_size :
        break
