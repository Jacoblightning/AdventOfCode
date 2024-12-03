""" Starting file for AOC Challenges """

import os.path

# Helpful imports (We have a lot of imports so that we are prepared for any situation without needing to import more)
from collections import *
from itertools import *
from functools import partial, reduce, lru_cache
from operator import *
from datetime import *
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

# We call it lines instaed of datalines so that they start with different letters.
# This is important so that when typing "d" for autocomplete, it will only show the one we want.
# If lines was called datalines and I typed "d", data would probably show up first in autocomplete.
def p1(data, lines):
    """ Part 1 Solution"""
    pass
    return data

def p2(data, lines):
    """ Part 2 Solution"""
    pass
    return data

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
