#!/usr/bin/env python3

with open("jumping_frog.txt", 'r') as fileread:
    for line in fileread:
        counts = {}
        linelower = line.lower()
        line_list = linelower.split()
        for word in line_list:
            if word not in counts:
                counts[word] = 0
            counts[word] += 1
        if 2 in counts.values():
                print(line)
