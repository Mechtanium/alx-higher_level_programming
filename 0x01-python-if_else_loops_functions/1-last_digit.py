#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print(f"Last digit of {number} is", end=" ")

if number > 0:
    number %= 10
elif number < 0:
    number %= 10
    if number != 0:
        number -= 10
else:
    number = 0

if number > 5:
    print(f"{number} and is greater than 5")
elif number == 0:
    print(f"{number} and is 0")
else:
    print(f"{number} and is less than 6 and not 0")
