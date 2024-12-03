from aoc_utils import *
from collections import Counter, defaultdict

with open("input.txt") as fd:
    puzzle = fd.readlines()

def solve1():
    return sum(map(diff, *map(sorted, rotate(listsplit(puzzle)))))

def solve2():
    data = listsplit(puzzle)
    data = intify(data)

    answer = defaultdict(int)

    rotated = rotate(data)

    firstline = rotated[0]
    secondline = Counter(rotated[1])

    for firstnum in firstline:
        answer[firstnum] += secondline[firstnum] * firstnum

    return sum(answer.values())

print(solve1())
print(solve2())