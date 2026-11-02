#!/usr/bin/env python3

def add_one(num):
    num = num + 1
    print("Inside add_one function, num =", num)

x = 5
print("Before calling add_one, x =", x)
add_one(x)
print("After calling add_one, x =", x)