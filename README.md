# url_workload #

## URL Collection ##

file name: uk-2007-05.urls.gz

size: 904MB

number of urls: 105,896,555

Link to the url collection: http://chato.cl/webspam/datasets/uk2007/links/

## Procedures to generate a URL workload ##

1. Download the URL collection

2. Run YCSB_URL/scripts/gen_url_sample.py to generate a uniform url sample.

   python gen_url_sample.py <url collection file> <sample size> > <output file>
   
   e.g.
   
   python gen_url_sample.py uk-2007-05.urls 1000000 > ../url/url_1M.dat

   If a sequential chunk of urls

