#!/usr/bin/python3

def raise_exception():
    try:
        raise TypeError("Exception raised")
    except TypeError as te:
        print(te)


if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
