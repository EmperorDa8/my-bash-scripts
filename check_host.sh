#!/bin/bash

if grep *127.0.0.1* /etc/hosts; then
	echo ' everthing is ok '
else 
	echo 'ERROR! 127.0.0.1 is not in /etc/hosts'
fi
