#!/usr/bin/env python3

"""Calculates the factorial, iterative and resursive"""

__author__ = "Alexandre Pilleyre"
__copyright__ = "Copyright 2021, Alexandre Pilleyre"
__credits__ = ["Alexandre Pilleyre", "mclintprojects"]
# mclintprojects for providing IdeaBag2 app

__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Alexandre Pilleyre"
__email__ = ""  # TODO: fill
__status__ = "Dev"

def factorial_recur(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    return n * factorial_recur(n - 1)

def factorial_iter(n):
    factorial = n
    for i in reversed(range(1,n)):
        factorial *= i
    return factorial if n != 0 else 1

def main():
    pass

if __name__ == "__main__":
    main()