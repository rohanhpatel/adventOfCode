import sys
import math

def parseFile(f):
    inpFile = open(f, 'r')
    datastream = inpFile.read().strip()
    return datastream

def part1():
    data = parseFile(sys.argv[1])
    markInd = -1
    for i in range(4, len(data)):
        marker = data[i-4:i]
        markList = list()
        for c in marker:
            markList.append(c)
        markSet = set(markList)
        if len(markSet) == 4:
            markInd = i
        if markInd > 0:
            break
    print("The index is: " + str(markInd))

def part2():
    data = parseFile(sys.argv[1])
    markInd = -1
    for i in range(14, len(data)):
        marker = data[i-14:i]
        markList = list()
        for c in marker:
            markList.append(c)
        markSet = set(markList)
        if len(markSet) == 14:
            markInd = i
        if markInd > 0:
            break
    print("The index is: " + str(markInd))

part2()
