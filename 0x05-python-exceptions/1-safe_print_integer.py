#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except (ValueError, IndexError):
        print("Error: ValueError or IndexError occurred")
        return False
    return value


if __name__ == "__main__":
    value = 89
has_been_print = safe_print_integer(89)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
