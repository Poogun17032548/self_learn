#!/usr/bin/env python3
import sys
import re

patt = "ism"
if len(sys.argv) == 1:
    print("none$")
else:
    for i in range(1, len(sys.argv)):
        s = sys.argv[i]
        match = re.match(f".*?({patt})", s)
        if match == None:
            print(f"{s}{patt}$")

#".*?()" = comsume before the first occurrence of the pattern, and capture the pattern in a group.
#re.match(pattern, string) = match the pattern at the beginning of the string. If the pattern is not found at the beginning, it returns None.