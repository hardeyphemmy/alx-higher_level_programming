#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    if (length == 2):
        print("1 argument:")
    elif (length > 2):
        print("{} arguments:".format(length - 1))
    else:
        print("0 arguments.")

    for i in range(1, length):
        print("{}: {}".format(i, sys.argv[i]))
