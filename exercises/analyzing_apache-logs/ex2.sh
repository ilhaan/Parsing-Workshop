#!/usr/bin/env bash 

safari="$(awk 'NF>1{print $NF}' apache_logs.txt | grep "Safari*" | wc -l )"
firefox="$(awk 'NF>1{print $NF}' apache_logs.txt | grep "Firefox*" | wc -l )"
echo $safari
echo $firefox
