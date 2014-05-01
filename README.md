# url_workload #

## URL Collection ##

file name: uk-2007-05.urls.gz

size: 904MB

number of urls: 105,896,555

Link to the url collection: http://chato.cl/webspam/datasets/uk2007/links/

## Procedures to generate a URL workload ##

1. Download the URL collection.

2. Download YCSB

    $ cd url_workload

    $ wget https://github.com/downloads/brianfrankcooper/YCSB/ycsb-0.1.4.tar.gz

    $ tar xfvz ycsb-0.1.4

    $ mv ycsb-0.1.4 YCSB

   Then build YCSB

    $ cd YCSB

    $ mvn clean package

3. In YCSB_URL/scripts/, run gen_url_sample.py to generate a UNIFORMLY distributed url sample.

    $ python gen_url_sample.py (url collection file) (sample size) > (output file)

    e.g. $ python gen_url_sample.py uk-2007-05.urls 1000000 > ../url/url_1M.dat

   If a SEQUENTIAL chunk of urls is need, run YCSB_URL/scripts/gen_url_sample_seq.py

    e.g. $ python gen_url_sample_seq.py uk-2007-05.urls 1000000 80001000 > ../urls/url_seq_1M.dat

4. Run reverseHostname.py to get the host names reversed.

    e.g. $ python reverseHostname.py ../urls/url_1M.dat

   The script will generate url_1M_reverse.dat in ../urls/

5. Run gen_url_wload.sh

    $ bash gen_url_wload.sh

   Output files are in YCSB_URL/output_url/

