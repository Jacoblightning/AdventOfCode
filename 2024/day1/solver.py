from collections import Counter, defaultdict

with open("input.txt") as fd:
    puzzle = fd.readlines()

def solve1():
    data = [i.split() for i in puzzle]

    firstline = [i[0] for i in data]
    secondline = [i[1] for i in data]

    sortfirst = sorted(firstline)
    sortsecond = sorted(secondline)

    bysize = zip(sortfirst, sortsecond)

    diffs = []

    # I probably could use itertools, but I don't want to
    diffs = [abs(int(i)-int(j)) for i, j in bysize]

    return sum(diffs)

def solve2():
    data = [i.split() for i in puzzle]

    answer = defaultdict(int)

    firstline = [int(i[0]) for i in data]
    secondline = Counter([int(i[1]) for i in data])

    for firstnum in firstline:
        answer[firstnum] += secondline[firstnum] * firstnum

    return sum(answer.values())

print(solve1())
print(solve2())