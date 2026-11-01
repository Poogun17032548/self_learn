#!/usr/bin/env python3
import sys

input_str = sys.argv
if len(input_str) < 2: 
    print("none$") 
else:
    print(input_str[1].upper())