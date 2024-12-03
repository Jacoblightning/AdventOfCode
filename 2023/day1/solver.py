import re

from aoc_utils import ASCII_NUMBERS_OR, ANY_TO_NUM

with open('input.txt') as fd:
    puzzle = fd.readlines()

def p1():
    results = []
    for line in puzzle:
        match = re.search(r"(\d).*(\d)", line)
        if match:
            result = match.group(1) + match.group(2)
        else:
            match = re.search(r"\d", line)
            result = match.group(0)*2
        results.append(int(result))
    return sum(results)

def p2():
    results = []
    for line in puzzle:
        match = re.search(r"({}|\d).*({}|\d)".format(ASCII_NUMBERS_OR, ASCII_NUMBERS_OR), line)
        if match:
            result = str(ANY_TO_NUM[match.group(1)]) + str(ANY_TO_NUM[match.group(2)])
        else:
            match = re.search(r"{}|\d".format(ASCII_NUMBERS_OR), line)
            result = str(ANY_TO_NUM[match.group(0)])*2
        results.append(int(result))
    return sum(results)


print(p1())
print(p2())
