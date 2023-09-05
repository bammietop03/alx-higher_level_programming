#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last = number % 10
else:
    last = -(abs(number) % 10)

if last > 5:
    message = "and is greater than 5"
elif last < 6 and last != 0:
    message = "and is less than 6 and not 0"
else:
    message = "and is 0"

print(f"Last digit of {number} is {last} {message}")
