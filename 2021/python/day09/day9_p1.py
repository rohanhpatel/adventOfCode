import sys
import csv
import math
import numpy as np

def readFile(file):
    dataFile = open(file)
    heightMat = []
    for line in dataFile:
        strList = list(line.strip('\n'))
        intList = []
        for string in strList:
            intList.append(int(string))
        heightMat.append(intList)
    return heightMat

def main():
    caveMat = readFile(sys.argv[1])
    totalRisk = 0
    for i in range(len(caveMat)):
        for j in range(len(caveMat[i])):
            cur = caveMat[i][j]
            existsLower = False
            if not existsLower and i != 0:
                existsLower = cur >= caveMat[i-1][j]
            if not existsLower and i != len(caveMat) - 1:
                existsLower = cur >= caveMat[i+1][j]
            if not existsLower and j != 0:
                existsLower = cur >= caveMat[i][j-1]
            if not existsLower and j != len(caveMat[i]) - 1:
                existsLower = cur >= caveMat[i][j+1]
            if not existsLower:
                totalRisk += 1 + cur
    print(totalRisk)

main()
