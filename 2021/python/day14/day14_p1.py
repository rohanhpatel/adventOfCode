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
    curPolymer = polymer
    for s in range(1, steps+1):
        newPolymer = ""
        for i in range(len(curPolymer) - 1):
            substr = curPolymer[i:i+2]
            if substr in rules:
                newPolymer += substr[0] + rules[substr]
                if i == len(curPolymer) - 2:
                    newPolymer += substr[1]
        curPolymer = newPolymer
    # print(curPolymer)
    uniqueChars = set()
    for c in curPolymer:
        uniqueChars.add(c)
    charCount = dict()
    for c in uniqueChars:
        charCount[c] = 0
    for c in curPolymer:
        charCount[c] += 1
    print(charCount)
    minimum = min(charCount.values())
    maximum = max(charCount.values())
    print(maximum - minimum)

main()
