#!/bin/bash

#mkdir "bash_files"
for file in *.sh; do
    mv $file ~/bash_files
    echo 'this $file is moved'
done
