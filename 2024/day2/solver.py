with open("input.txt") as fd:
    puzzle = fd.readlines()

data = [i.split() for i in puzzle]

def linesafe(line):
    # Right, we can sort
    if not (line == sorted(line) or line == sorted(line, reverse=True)):
        return False

    for cnt, i in enumerate(line):
        if cnt == 1: continue

        diff = abs(int(line[cnt-1]) - int(i))

        if not 0 < diff < 4:
            return False
    return True

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