#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 100):
        num = (abs(number))
        if num % 3 == 0:
            print("Fizz ", end="")
        elif num % 5 == 0:
            print("Buzz ", end="")
        elif num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end="")
        else:
            print("{} ".format(num), end="")


if __name__ == "__main__":
    fizzbuzz()
