#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none$")
else:
    rang = range(int(sys.argv[1]), int(sys.argv[2]))
    print(f"{list(rang)}$")