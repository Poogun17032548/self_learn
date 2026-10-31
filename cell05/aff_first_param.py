#/usr/bin/env python3
import sys
arg = sys.argv
if len(arg) <= 1:
    print("none$")
else:
    print(f"{arg[1]}$")