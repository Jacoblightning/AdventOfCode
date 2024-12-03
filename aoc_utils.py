# I symlinked a file in the venv to this.
# That is how imports are working
# ln -s ../../../../aoc_utils.py .venv/lib/python3.12/site-packages/aoc_utils.py
import operator
import sys
from functools import reduce
sys.setrecursionlimit(10000)


def diff(x, y):
    return abs(int(x)-int(y))

def mulall(*args):
    if len(args) == 1:
        tored = map(int, args[0])
        return reduce(operator.mul, tored)
    tored = map(int, args)
    return reduce(operator.mul, tored)

def listsplit(list_):
    return [str(i).split() for i in list_]


def get(list_, x, val):
    if len(list_) > int(x):
        return list_[x]
    return val

def rotate(list_):
    newlist = []
    for j in range(len(list_[0])):
        newlist.append([get(i, j, None) for i in list_])
    return newlist

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