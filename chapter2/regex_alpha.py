#!/usr/bin/env python3
#
# Script to check if a given string contains only alphabets
#
# Example: ./regex_alpha.py yourstringhere

import re
import sys

# Compile re to check if string contains alphabets only
p = re.compile("^[A-Za-z]+$")

given_string = sys.argv[1]

if p.match(given_string):
    print("The provided string contains only alphabets")
else:
    print("The provided string contains non-alphabet characters")
