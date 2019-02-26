#!/usr/bin/env python3
#
# Check if a given string is ac followed by one or more
# bs and then at least one q after the last b.
#
# Example: ./regex_acb.py yourstringhere

import re
import sys

# Compile re to check if string contains alphabets only
p = re.compile("acb*q+")

given_string = sys.argv[1]

if p.match(given_string):
    print("Match!")
else:
    print("No match")
