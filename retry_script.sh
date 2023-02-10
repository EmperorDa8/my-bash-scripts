#!/bin/bash

n=0
instruct=$1
while ! $instruct && [ $n -le 5 ]; do
    sleep $n
    ((n=n+1))
    echo 'Retry #$n'

done;
