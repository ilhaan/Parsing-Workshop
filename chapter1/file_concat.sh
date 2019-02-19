#!/usr/bin/env bash 

if [ $# -eq 0 ]; then 
	echo "Filenames not provided"
	exit 1 
fi 

cat $1 > merged.txt 
cat $2 >> merged.txt 
