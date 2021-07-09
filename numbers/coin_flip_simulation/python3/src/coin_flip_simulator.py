#!/usr/bin/env python3

"""Simulates coin flip"""

__author__ = "Alexandre Pilleyre"
__copyright__ = "Copyright 2021, Alexandre Pilleyre"
__credits__ = ["Alexandre Pilleyre", "mclintprojects"]
# mclintprojects for providing IdeaBag2 app

__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Alexandre Pilleyre"
__email__ = ""  # TODO: fill
__status__ = "Dev"

import random

def coin_flip(times=1):
    # Maybe round is not a good choice for equal repartition
    flips = [round(random.random()) for i in range(times)]
    tails = len(list(filter(lambda x : x == 1, flips)))
    heads = len(list(filter(lambda x : x == 0, flips)))
    return tails, heads, flips

def main():
    tails, heads, flips = coin_flip(100000)
    print(f"Tails: {tails}")
    print(f"heads: {heads}")
    print(f"Ratio: {tails/heads}")

if __name__ == "__main__":
    main()
