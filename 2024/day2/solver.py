with open("input.txt") as fd:
    puzzle = fd.readlines()

data = [i.split() for i in puzzle]

# Bad code.
#TODO: Clean this up
def linesafe(line):
    # Right, we can sort
    if not (line == sorted(line) or line == sorted(line, reverse=True)):
        return False

    thissafe = True
    last = False
    second = False
    for i in line:
        if last is False:
            last = i
            # The next one will be the second number in the sequence
            second = True
            continue
        diff = abs(int(last) - int(i))
        if not 0 < diff < 4:
            thissafe = False
            break
        last = i
    return thissafe

def solve1():
    safe = 0
    for line in data:
        if linesafe(line):
            safe += 1
    return safe



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