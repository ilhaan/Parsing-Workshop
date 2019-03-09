#!/usr/bin/env bash 

num="$(grep 200 apache_logs.txt | wc -l)"
total="$(cat apache_logs.txt | wc -l)"
echo "$num/$total * 100" | bc -l 
