#!/usr/bin/env python3

"""Checks if a number is an happy number & get the 8 first happy numbers"""

__author__ = "Alexandre Pilleyre"
__copyright__ = "Copyright 2021, Alexandre Pilleyre"
__credits__ = ["Alexandre Pilleyre", "mclintprojects"]
# mclintprojects for providing IdeaBag2 app

__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Alexandre Pilleyre"
__email__ = ""  # TODO: fill
__status__ = "Dev"


def digits(n):
    d = []
    while n >= 10:
        d.append(n % 10)
        n //= 10
    d.append(n % 10)
    return d

def is_happy_number(n):
    number = n
    save = []
    while number != 1:
        number = sum([d ** 2 for d in digits(number)])
        if number not in save:
            save.append(number)
        elif number in save:
            return False
    return True

def eight_first_happy():
    num = 0
    numbers = []
    while len(numbers) < 8:
        if is_happy_number(num):
            numbers.append(num)
        num += 1
    return numbers


def main():
    print(is_happy_number(2))
    print(eight_first_happy())

if __name__ == "__main__":
    main()
