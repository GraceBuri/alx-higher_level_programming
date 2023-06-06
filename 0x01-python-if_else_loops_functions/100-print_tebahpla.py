#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in reverse order alternating upper- and lower-case."""
for c in range(ord('Z'), ord('A') - 1, -1):
    if (ord('Z') - c) % 2 == 0:
        print("{}".format(chr(c)), end="")
    else:
        print("{}".format(chr(c).lower()), end="")
