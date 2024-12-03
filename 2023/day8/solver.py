import os.path

# Helpful imports
from collections import *
from itertools import *
from functools import partial, reduce


def p1(data):
    pass

def p2(data):
    pass

def main():
    if os.path.exists("input.txt"):
        with open("input.txt") as fd:
            puzzle = fd.read()

        puzzlelines = puzzle.split("\n")

        print(p1(puzzlelines))
        print(p2(puzzlelines))
    else:
        print("Input file not found")


if __name__ == '__main__':
    main()
