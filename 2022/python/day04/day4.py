import sys
import math

def part1():
    inpFile = open(sys.argv[1], 'r')
    fullyContain = 0
    for line in inpFile:
        pairs = line.strip().split(',')
        actPairs = list()
        for pair in pairs:
            pairList = list()
            fullRange = pair.split("-")
            start = int(fullRange[0])
            while start <= int(fullRange[1]):
                pairList.append(start)
                start += 1
            actPairs.append(pairList)
        set1 = set(actPairs[0])
        set2 = set(actPairs[1])
        diffSet = set1.intersection(set2)
        if diffSet == set1 or diffSet == set2:
            fullyContain += 1
    print("Number of assignment pairs where one range fully contains the other: " + str(fullyContain))

def part2():
    inpFile = open(sys.argv[1], 'r')
    overlapping = 0
    for line in inpFile:
        pairs = line.strip().split(',')
        actPairs = list()
        for pair in pairs:
            pairList = list()
            fullRange = pair.split("-")
            start = int(fullRange[0])
            while start <= int(fullRange[1]):
                pairList.append(start)
                start += 1
            actPairs.append(pairList)
        set1 = set(actPairs[0])
        set2 = set(actPairs[1])
        diffSet = set1.intersection(set2)
        if len(diffSet) != 0:
            overlapping += 1
    print("Number of overlapping assignment pairs: " + str(overlapping))
    
part1()
