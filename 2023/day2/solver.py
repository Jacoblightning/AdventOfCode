import operator
from functools import reduce
from aoc_utils import *

data = {}

maxnum = {"red":12,"green":13,"blue":14}

with open("input.txt") as fd:
    rawdata = fd.readlines()


for i, line in enumerate(rawdata, 1):
    data[i] = []
    gamedata = line.split(":")[1].split(";")
    for drawdata in gamedata:
        cubicdata = {}
        drawdata = drawdata.strip()
        cubedata = drawdata.split(",")
        for cube in cubedata:
            splitcube = cube.split()
            cubicdata[splitcube[1]] = int(splitcube[0])
        data[i].append(cubicdata)

def p1():
    goodgames = []
    for gameid, game in data.items():
        valid = True
        for draws in game:
            for color, number in draws.items():
                if number > maxnum[color]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            goodgames.append(gameid)
    return sum(goodgames)

def p2():
    fewgame = {}
    for gameid, game in data.items():
        fewest = {"red": 0, "green": 0, "blue": 0}
        for draws in game:
            for color, number in draws.items():
                if number > fewest[color]:
                    fewest[color] = number
        fewgame[gameid] = fewest

    psets = []
    for game in fewgame.values():
        psets.append(mulall(game.values()))

    return sum(psets)




print(p1())
print(p2())

