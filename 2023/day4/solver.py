""" Starting file for AOC Challenges """

import os.path

# Helpful imports (We have a lot of imports so that we are prepared for any situation without needing to import more)
from collections import *
from itertools import *
from functools import partial, reduce, lru_cache
from operator import *
from datetime import *
from string import *
from io import *
from ctypes import *
import re
# Uncomment if needed
#from hashlib import sha1, sha256, sha512, md5

from aoc_utils import *

# Tips:
# You want re.search, not re.match
# Consider re.finditer over looping through re.findall
# have a link. https://regex101.com/

# We call it lines instead of datalines so that they start with different letters.
# This is important so that when typing "d" for autocomplete, it will only show the one we want.
# If lines was called datalines and I typed "d", data would probably show up first in autocomplete.
def p1(data, lines):
    """ Part 1 Solution"""
    nums = [i.split("|") for i in lines][:-1]

    rot = rotate(nums)
    ours = [i.split() for i in rot[1]]
    winning = [j.split() for j in [i.split(":")[1] for i in rot[0]]]
    total = 0
    for ours, winning in zip(ours, winning):
        ourwinning = 0
        for our in ours:
            if our in winning:
                ourwinning += 1
        if ourwinning > 0:
            total += 2 ** (ourwinning-1)
    return total

def p2(data, lines):
    """ Part 2 Solution"""
    pass
    return

def main():
    """ Run Solutions"""
    # Redundancy check
    if os.path.exists("input.txt"):
        with open("input.txt") as fd:
            # Read input into puzzle
            puzzle = fd.read()

        # Split puzzle by lines
        puzzlelines = puzzle.split("\n")

        print(p1(puzzle, puzzlelines))
        print(p2(puzzle, puzzlelines))
    else:
        print("Input file not found")


if __name__ == '__main__':
    main()
