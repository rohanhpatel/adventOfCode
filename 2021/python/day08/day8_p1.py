import sys
import csv
import math
import numpy as np

datafile = open(sys.argv[1])
probs = []
for line in datafile:
    tmpSplit = line.split("|")
    tmpSplit2 = []
    for string in tmpSplit:
        tmpSplit2.append(string.split(" "))
    tmpSplit2[1][-1] = tmpSplit2[1][-1].strip('\n')
    uniquePats = []
    outputs = []
    for string in tmpSplit2[0]:
        uniquePats.append(set(list(string)))
    for string in tmpSplit2[1]:
        outputs.append(set(list(string)))
    probs.append((uniquePats, outputs))

uniqueSegs = 0
for p in probs:
    uniquePat = p[0]
    output = p[1]
    for val in output:
        if len(val) == 2 or len(val) == 3 or len(val) == 4 or len(val) == 7:
            uniqueSegs += 1

print(uniqueSegs)
