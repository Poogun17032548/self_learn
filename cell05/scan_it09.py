#!/usr/bin/env python3
import sys
import re
if len(sys.argv) < 3:
    print("none$")
else:
    words = sys.argv[1]
    seo = sys.argv[2]
    match = re.findall(words, seo)
    print(len(match))
