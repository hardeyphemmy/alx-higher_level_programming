#!/usr/bin/python3
import sys

length = len(sys.argv)
if (length == 1):
    print("1 argument:")
elif (length > 1):
    print("{} arguments:".format(length - 1))
else:
    print("0 arguments.")

for i in range(1, length):
    print("{}: {}".format(i, sys.argv[i]))
