#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    rem = (number % 10) - 10
else:
    rem = number % 10
print(f"Last digit of {number} is {rem} and ", end="")
if rem > 5:
    print("is greater than 5")
elif rem == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")
