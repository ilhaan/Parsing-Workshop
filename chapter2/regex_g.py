#!/usr/bin/env python3
#
# Check if a given string is a g followed by zero or more rs.
#
# Example: ./regex_alpha.py yourstringhere

import re
import sys

# Compile re to check if string contains alphabets only
p = re.compile("^gr*")

given_string = sys.argv[1]

if p.match(given_string):
    print("Match!")
else:
    print("No match")
