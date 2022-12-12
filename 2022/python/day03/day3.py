import sys
import math

def part1():
    inpFile = open(sys.argv[1], "r")
    totalPriority = 0
    for line in inpFile:
        actLine = line.strip()
        halfInd = int(len(actLine)/2)
        first = actLine[:halfInd]
        second = actLine[halfInd:]
        firstSet = set()
        secondSet = set()
        for c in first:
            firstSet.add(c)
        for c in second:
            secondSet.add(c)
        commonChar = ''
        for c in firstSet:
            if c in secondSet:
                commonChar = c
                break
        modifier = 0
        if ord(commonChar) < 97: #it's an uppercase character
           modifier = 26
        totalPriority += ord(commonChar.lower()) - 96 + modifier
    print("sum of priorities: " + str(totalPriority))


def part2():
    inpFile = open(sys.argv[1], 'r')
    totalPriority = 0
    lineNum = 0
    lineArr = list()
    for line in inpFile:
        lineArr.append(line.strip())
        if lineNum % 3 == 2:
            setList = list()
            for sack in lineArr:
                tmpSet = set()
                for c in sack:
                    tmpSet.add(c)
                setList.append(tmpSet)
            singSet = setList[0].intersection(setList[1], setList[2])
            commonChar = ''
            for i in singSet:
                commonChar = i
            mod = 0
            if ord(commonChar) < 97:
                mod = 26
            totalPriority += ord(commonChar.lower()) - 96 + mod
            lineArr = list()
        lineNum += 1
    print("sum of priorities: " + str(totalPriority))
            
part2()
