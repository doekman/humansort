#!/usr/bin/env python3

'''
Command-line program that sorts standard input as a human would expect. 
Usage: cat input.txt | ./human_sort.py
'''

import re, sys

regex = re.compile(r'(?:\d+|[^\d]+)')
max_int_pos = len(str(sys.maxsize))
pad_int = '{:0'+str(max_int_pos)+'d}'

def human_sort_key(string):
    parts = regex.findall(string)
    return [pad_int.format(int(part)) if part.isdigit() else str.lower(part) for part in parts]


lines = []

try: 
    while True: 
        lines.append(input())
except EOFError: 
    lines.sort(key=human_sort_key)

for line in lines: print(line)
