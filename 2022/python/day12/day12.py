import sys
import os
import math
from dill.source import getsource

def parseFile(f):
    inpFile = open(f, 'r')
    grid = list()
    for line in inpFile:
        chrList = list(line.strip())
        fullList = [[x, False] for x in chrList]
        grid.append(fullList.copy()) 
    return grid

def findStart(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j][0] == 'S':
                return (i, j)

def getElevation(grid, x, y):
    if grid[x][y][0] == 'S':
        return 0
    elif grid[x][y][0] == 'E':
        return 26
    else:
        return ord(grid[x][y][0]) - 96

def findNextPos(grid, curPos):
    move = dict()
    x = curPos[0]
    y = curPos[1]
    val = getElevation(grid, x, y)
    if x != 0:
        move[(x-1, y)] = getElevation(grid, x-1, y)
    if x != len(grid) - 1:
        move[(x+1, y)] = getElevation(grid, x+1, y)
    if y != 0:
        move[(x, y-1)] = getElevation(grid, x, y-1)
    if y != len(grid[0]) - 1:
        move[(x, y+1)] = getElevation(grid, x, y+1)
    allValues = list(move.items())
    siftedValues = list()
    for key, value in allValues:
        if value <= val + 1 and not grid[key[0]][key[1]][1]:
            siftedValues.append(value)
    siftedValues.sort(reverse = True)
    if len(siftedValues) != 0:
        for key in move:
            if move[key] == siftedValues[0] and not grid[key[0]][key[1]][1]:
                return list(key)
    else:
        return None

def part1():
    grid = parseFile(sys.argv[1])
    start = findStart(grid)
    print(start)
    curPos = list(start)
    curPath = list()
    numSteps = 0
    while grid[curPos[0]][curPos[1]][0] != 'E':
        grid[curPos[0]][curPos[1]][1] = True
        curPath.append(curPos.copy())
        res = findNextPos(grid, curPos)
        if res:
            curPos = res
        else:
            for i in range(len(curPath) - 1):
                pos = curPath[i]
                grid[pos[0]][pos[1]][1] = False
            curPos = list(start)
        numSteps += 1
        print("We are at ({x}, {y})".format(x = curPos[0], y = curPos[1]))
    print("Number of steps to get to E: " + str(numSteps))

def part2():
    pass

def main():
    if len(sys.argv) < 3:
        print("Not enough arguments")
        exit(1)
    part = int(sys.argv[2])
    if part == 1:
        part1()
    elif part == 2:
        part2()
    else:
        print("Not a valid part")

main()
