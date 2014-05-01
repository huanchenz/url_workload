#!/bin/bash

# Fixed folder hierachy
YCSB_DIR="../../YCSB"
URL_DIR="../urls"
OUT_YCSB_DIR="../output_ycsb"
OUT_URL_DIR="../output_url"
SCRIPT_DIR="."

# Configurable arguments
RECORD_COUNT=1000000
OPERATION_COUNT=1000000

# Property file arguments
URL_INPUT="url_1M_reverse.dat"
URL_SAMPLE_SIZE=1000000
LOAD_YCSB="loada_1M.dat"
TXN_YCSB="txnsa_1M.dat"
LOAD_URL="loada_url_1M.dat"
TXN_URL="txnsa_url_1M.dat"

# Workload specification
WORKLOAD="workloada"

# URL MAP Program
URLMAP="urlMap.py"
URLMAP_RANDOM="urlMap_random.py"
URLMAP_ARGS="urlMapArgs.property"

function set_property ()
{
    echo $URL_DIR/$URL_INPUT > $1
    echo $URL_SAMPLE_SIZE >> $1
    echo $OUT_YCSB_DIR/$LOAD_YCSB >> $1
    echo $OUT_YCSB_DIR/$TXN_YCSB >> $1
    echo $OUT_URL_DIR/$LOAD_URL >> $1
    echo $OUT_URL_DIR/$TXN_URL >> $1
}

$YCSB_DIR/bin/ycsb load basic -P $YCSB_DIR/workloads/$WORKLOAD -p recordcount=$RECORD_COUNT -s > $OUT_YCSB_DIR/$LOAD_YCSB

$YCSB_DIR/bin/ycsb run basic -P $YCSB_DIR/workloads/$WORKLOAD -p operationcount=$OPERATION_COUNT -s > $OUT_YCSB_DIR/$TXN_YCSB

set_property $SCRIPT_DIR/$URLMAP_ARGS

#python $SCRIPT_DIR/$URLMAP $SCRIPT_DIR/$URLMAP_ARGS

python $SCRIPT_DIR/$URLMAP_RANDOM $SCRIPT_DIR/$URLMAP_ARGS
