#!/usr/bin/env python3

import re
import sys

# Compile re to check if string contains alphabets only
p = re.compile("^[A-Za-z]+$")

given_string = sys.argv[1]

if p.match(given_string):
    print("The provided string contains only alphabets")
else:
    print("The provided string contains non-alphabet characters")
