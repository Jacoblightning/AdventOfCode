from collections import Counter
from curses.ascii import isdigit

from aoc_utils import *

with open("input.txt") as fd:
    puzzle = fd.readlines()

data = listsplit(puzzle)

def linesafe(line):
    if not (line == sorted(line) or line == sorted(line, reverse=True)):
        return False

    for cnt, i in enumerate(line):
        if cnt == 0: continue

        diff_ = diff(line[cnt-1], i)

        if not 0 < diff_ < 4:
            return False
    return True

def solve1():
    return Counter(linesafe(line) for line in data)[True]



def solve2():
    safe = 0
    # Brute force it!!
    for line in data:
        if linesafe(line):
            safe += 1
        else:
            for i in range(len(line)):
                subline = line[:i] + line[i + 1:]
                if linesafe(subline):
                    safe += 1
                    break
    return safe


print(solve1())
print(solve2())