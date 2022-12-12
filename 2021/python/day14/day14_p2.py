import sys
import csv
import math
import numpy as np

def readFile(file):
    dataFile = open(file)
    firstLine = True
    startPoly = ""
    rules = dict()
    for line in dataFile:
        goodLine = line.strip('\n')
        if firstLine:
            startPoly = goodLine
            firstLine = False
        elif goodLine != '':
            strs = goodLine.split(" -> ")
            rules[strs[0]] = strs[1]
    return (startPoly, rules)

def main():
    polymer, rules = readFile(sys.argv[1])
    steps = int(sys.argv[2])
    curPolymer = dict()
    for i in range(len(polymer) - 1):
        substr = polymer[i:i+2]
        curPolymer[substr] = 1
    for s in range(steps):
        # print("curPolymer:")
        # print(curPolymer)
        newPolymer = dict()
        for pair in curPolymer:
            str1 = pair[0] + rules[pair]
            str2 = rules[pair] + pair[1]
            if str1 not in newPolymer:
                newPolymer[str1] = curPolymer[pair]
            else:
                newPolymer[str1] += curPolymer[pair]
            if str2 not in newPolymer:
                newPolymer[str2] = curPolymer[pair]
            else:
                newPolymer[str2] += curPolymer[pair]
        curPolymer = newPolymer.copy()
    uniqueChars = set()
    for pair in curPolymer:
        uniqueChars.add(pair[0])
        uniqueChars.add(pair[1])
    charCount = dict()
    for c in uniqueChars:
        charCount[c] = 0
    for pair in curPolymer:
        charCount[pair[0]] += curPolymer[pair]
        charCount[pair[1]] += curPolymer[pair]
    for c in charCount:
        if charCount[c] % 2 == 1:
            charCount[c] += 1
        charCount[c] = int(charCount[c]/2)
    # print("charCount:")
    # print(charCount)
    minimum = min(charCount.values())
    maximum = max(charCount.values())
    print(maximum - minimum)

main()
