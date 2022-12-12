import sys
import math

def getCalList(fileName):
    inputFile = open(fileName, "r")
    fullList = list()
    curNum=0
    for line in inputFile:
        if line != "\n":
            curNum += int(line.strip())
        else:
            fullList.append(curNum)
            curNum = 0
    fullList.append(curNum)
    return fullList

def part1():
    fullList = getCalList(sys.argv[1])
    print(max(fullList))

def part2():
    fullList = getCalList(sys.argv[1])
    fullList.sort(reverse=True)
#    print(fullList)
    total = 0
    for i in range(3):
        total += fullList[i]
    print(total)
    

#part1()
part2()
