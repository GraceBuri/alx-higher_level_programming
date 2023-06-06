#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number = 12345
last_digit = number % 10

result = f"Last digit of {number} is {last_digit}, "

if last_digit > 5:
    result += "and is greater than 5\n"
elif last_digit == 0:
    result += "and is 0\n"
else:
    result += f"and is less than 6 and not 0\n"

print(result)
