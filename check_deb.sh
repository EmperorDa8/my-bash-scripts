#!/bin/bash

lines="--------------------------------"

echo 'starting at ' $(date)*
echo $lines

echo 'UPTIME'
uptime
echo $lines


echo 'Free space'
free
echo $lines


echo 'running process'
ps
echo $lines


echo 'login users'
who
echo $lines


echo  'closing at :' $(date)*


