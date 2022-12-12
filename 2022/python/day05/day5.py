import sys
import math

def parseFile(f):
    inpFile = open(f, 'r')
    readingStacks = True
    stacks = list()
    actStacks = dict()
    directions = list()
    actDirections = list()
    for line in inpFile:
        if line == "\n":
            readingStacks = False
            # parse the stacks
            guideline = stacks[-1]
            for ln in stacks:
                for c in range(len(guideline)):
                    if guideline[c] != ' ' and (ln[c] != ' ' and ln[c] != '[' and ln[c] != ']') and guideline[c] != ln[c]:
                        if int(guideline[c]) not in actStacks:
                            actStacks[int(guideline[c])] = list()
                        actStacks[int(guideline[c])].append(ln[c])
        if readingStacks:
            stacks.append(line[:len(line)-1])
        if not readingStacks and line != "\n": # we must be reading the directions
            directions.append(line.strip().split(" "))
    # now parse the directions
    for ln in directions:
        actDirections.append((int(ln[1]), int(ln[3]), int(ln[5])))
    return (actStacks, actDirections)

def part1():
    stacks, directions = parseFile(sys.argv[1])
    for direct in directions:
        numMoves = direct[0]
        start = direct[1]
        end = direct[2]
        for _ in range(numMoves):
            movingItem = stacks[start][0]
            stacks[end].insert(0, movingItem)
            del stacks[start][0]
    finalString = ''
    sortedKeys = list(stacks.keys())
    sortedKeys.sort()
    for key in sortedKeys:
        finalString += stacks[key][0]
    print("The final string is: " + finalString)


def part2():
    stacks, directions = parseFile(sys.argv[1])
    for direct in directions:
        numMoves = direct[0]
        start = direct[1]
        end = direct[2]
        movingList = stacks[start][:numMoves]
        stacks[start] = stacks[start][numMoves:]
        stacks[end] = movingList + stacks[end]
    finalString = ''
    sortedKeys = list(stacks.keys())
    sortedKeys.sort()
    for key in sortedKeys:
        finalString += stacks[key][0]
    print("The final string is: " + finalString)

part2()
