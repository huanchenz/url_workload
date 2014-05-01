# argv[1]: url list
# argv[2]: url sample size
# argv[3]: start point

import sys

url_sample_size = int(sys.argv[2])
start_point = int(sys.argv[3])

f_urls = open (sys.argv[1], 'r')
count = -start_point
total_count = 0
for line in f_urls :
    count += 1
    if count > 0 :
        print line.strip()
        total_count += 1
    if total_count >= url_sample_size :
        break
