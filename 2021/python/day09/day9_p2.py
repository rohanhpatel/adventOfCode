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
            intList.append([int(string), False])
        heightMat.append(intList)
    return heightMat

def findBasin(mat, x, y):
    mat[x][y][1] = True
    res = 1
    if x != 0:
        if not mat[x-1][y][1] and mat[x-1][y][0] != 9:
            res += findBasin(mat, x-1, y)
    if x != len(mat) - 1:
        if not mat[x+1][y][1] and mat[x+1][y][0] != 9:
            res += findBasin(mat, x+1, y)
    if y != 0:
        if not mat[x][y-1][1] and mat[x][y-1][0] != 9:
            res += findBasin(mat, x, y-1)
    if y != len(mat[x]) - 1:
        if not mat[x][y+1][1] and mat[x][y+1][0] != 9:
            res += findBasin(mat, x, y+1)
    return res


def main():
    caveMat = readFile(sys.argv[1])
    basins = []
    for i in range(len(caveMat)):
        for j in range(len(caveMat[i])):
            cur = caveMat[i][j]
            existsLower = False
            if not existsLower and i != 0:
                existsLower = cur[0] >= caveMat[i-1][j][0]
            if not existsLower and i != len(caveMat) - 1:
                existsLower = cur[0] >= caveMat[i+1][j][0]
            if not existsLower and j != 0:
                existsLower = cur[0] >= caveMat[i][j-1][0]
            if not existsLower and j != len(caveMat[i]) - 1:
                existsLower = cur[0] >= caveMat[i][j+1][0]
            if not existsLower:
                # print("i:", str(i), "and j:", str(j))
                basins.append(findBasin(caveMat, i, j))

    basins.sort(reverse=True)
    res = 1
    for i in range(3):
        res *= basins[i]
    print(res)

main()
