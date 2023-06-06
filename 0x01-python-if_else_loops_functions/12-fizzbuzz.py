#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space.

    For multiples of three, print Fizz instead of the number.
    For multiples of five, print Buzz instead of the number.
    For multiples of three and five, print FizzBuzz instead of the number.
    """
    result = ""
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            result += "FizzBuzz "
        elif number % 3 == 0:
            result += "Fizz "
        elif number % 5 == 0:
            result += "Buzz "
        else:
            result += "{} ".format(number)
    print(result)
