import re

with open('input.txt') as fd:
    puzzle = fd.readlines()

lookup = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

def p1():
    results = []
    for line in puzzle:
        match = re.search(r"(\d).*(\d)", line)
        if match:
            result = match.group(1) + match.group(2)
        if not match:
            match = re.search(r"\d", line)
            result = match.group(0)*2
        results.append(int(result))
    return sum(results)

def p2():
    results = []
    for line in puzzle:
        match = re.search(r"((one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|\d).*((one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|\d)", line)
        if match:
            result = str(lookup[match.group(1)]) + str(lookup[match.group(11)])
        if not match:
            match = re.search(r"(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|\d", line)
            result = str(lookup[match.group(0)])*2
        results.append(int(result))
    return sum(results)


print(p1())
print(p2())
