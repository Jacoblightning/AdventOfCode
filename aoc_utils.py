# I symlinked a file in the venv to this.
# That is how imports are working
# ln -s ../../../../aoc_utils.py .venv/lib/python3.12/site-packages/aoc_utils.py
import operator
import sys
from functools import reduce
from string import printable, ascii_letters

sys.setrecursionlimit(10000)

ASCII_NUMBERS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ASCII_NUMBERS_OR = "|".join(ASCII_NUMBERS)

ANY_TO_NUM = {}
ANY_TO_NUM.update({i:c for c,i in enumerate(ASCII_NUMBERS)})
ANY_TO_NUM.update({str(i):i for i in range(10)})
ANY_TO_NUM.update({i:i for i in range(10)})

SYMBOLS = set(printable)-set(ascii_letters)

def diff(x, y):
    return abs(int(x)-int(y))

def mulall(*args):
    if len(args) == 1:
        tored = map(int, args[0])
        return reduce(operator.mul, tored)
    tored = map(int, args)
    return reduce(operator.mul, tored)

def listsplit(list_):
    return list(map(str.split, map(str, list_)))

def get(list_, x, val):
    return list_[x] if len(list_) > int(x) else val

def rotate(list_):
    return list(zip(*list_))

def intify(data):
    if isinstance(data, str):
        return int(data)
    if isinstance(data, int):
        return data
    # Might be a list of lists so we map to intify,  not int
    if isinstance(data, list):
        return list(map(intify, data))
    if isinstance(data, dict):
        return {i:intify(j) for i, j in data.items()}