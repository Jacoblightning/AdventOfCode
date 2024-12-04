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

def near(lines, y, x):
    nearby = []
    for modx in range(-1, 2):
        for mody in range(-1, 2):
            try:
                if lines[mody+y][modx+x].isdigit():
                    nearby.append((x+modx, y+mody))
            except IndexError:
                continue
    return nearby

def findstart(lines, x, y):
    assert lines[y][x].isdigit()
    counter = x
    while str.isdigit(lines[y][counter]) and counter >= 0:
        counter -= 1
    return counter+1

def getnum(lines, x, y):
    assert lines[y][x].isdigit()

    counter = x
    try:
        while str.isdigit(lines[y][counter]):
            counter += 1
    except IndexError:
        pass
    return int(lines[y][x:counter])


# We call it lines instead of datalines so that they start with different letters.
# This is important so that when typing "d" for autocomplete, it will only show the one we want.
# If lines was called datalines and I typed "d", data would probably show up first in autocomplete.
def p1(data, lines):
    """ Part 1 Solution"""
    alldigits = set()
    startdigits = set()
    for yidx, y in enumerate(lines):
        for xidx, x in enumerate(y):
            if not x.isdigit() and x != ".":
                for i in near(lines, yidx, xidx):
                    alldigits.add(i)
    for x, y in alldigits:
        startdigits.add((findstart(lines, x, y), y))

    nums = [getnum(lines, x, y) for x, y in startdigits]

    return sum(nums)




def p2(data, lines):
    """ Part 2 Solution"""
    sum = 0
    startdigits = set()
    for yidx, y in enumerate(lines):
        for xidx, x in enumerate(y):
            if x == "*":
                nearby = near(lines, yidx, xidx)
                if len(nearby) >= 2:
                    gears = set()
                    for x, y in nearby:
                        gears.add((findstart(lines, x, y), y))
                    if len(gears) == 2:
                        intermediary = []
                        for x, y in gears:
                            intermediary.append(getnum(lines, x, y))
                        sum += mulall(intermediary)



    return sum

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
