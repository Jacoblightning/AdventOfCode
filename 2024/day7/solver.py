import os.path

# Helpful imports
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

# Tips:
# You want re.search, not re.match
# Consider re.finditer over looping through re.findall
# have a link. https://regex101.com/




def p1(data):
    pass
    return data

def p2(data):
    pass
    return data

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
