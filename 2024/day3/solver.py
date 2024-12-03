import re

with open("input.txt") as fd:
    puzzle = fd.read()


def p1(data):
    muls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)

    return sum([int(i[0])*int(i[1]) for i in muls])

def p2(data):
    running_sum = 0
    evaluate = True
    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)", data):
        num1, num2, do, dont = match.groups()

        if do:
            evaluate = True
        elif dont:
            evaluate = False
        # This works because we must have matched the mul statement if we didn't match do or don't
        elif evaluate:
            running_sum += int(num1) * int(num2)
    return running_sum

print(p1(puzzle))
print(p2(puzzle))

