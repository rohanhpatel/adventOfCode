import sys
import csv
import math
import numpy as np

def readFile(file):
    dataFile = open(file)
    octMat = []
    for line in dataFile:
        strLine = list(line.strip('\n'))
        octLine = []
        for string in strLine:
            octLine.append([int(string), False])
        octMat.append(octLine)
    return octMat

def flash(mat, x, y):
    # print("Matrix at {}, {}:".format(x, y))
    # printOctMat(mat)
    if not mat[x][y][1]:
        mat[x][y][0] += 1
    if mat[x][y][0] > 9:
        flashes = 1
        mat[x][y][0] = 0
        mat[x][y][1] = True
        xNotLow = x != 0
        yNotLow = y != 0
        xNotHigh = x != len(mat) - 1
        yNotHigh = y != len(mat[x]) - 1
        if xNotLow:
            flashes += flash(mat, x-1, y)
            if yNotLow:
                flashes += flash(mat, x-1, y-1)
            if yNotHigh:
                flashes += flash(mat, x-1, y+1)
        if xNotHigh:
            flashes += flash(mat, x+1, y)
            if yNotLow:
                flashes += flash(mat, x+1, y-1)
            if yNotHigh:
                flashes += flash(mat, x+1, y+1)
        if yNotLow:
            flashes += flash(mat, x, y-1)
        if yNotHigh:
            flashes += flash(mat, x, y+1)
        return flashes
    return 0

def printOctMat(mat):
    for lst in mat:
        newList = []
        for elem in lst:
            newList.append(str(elem[0]))
        print(" ".join(newList))


def main():
    octMat = readFile(sys.argv[1])
    steps = int(sys.argv[2])
    synchron = -1
    s = 1
    while True:
        # increment all the octopi
        for i in range(len(octMat)):
            for j in range(len(octMat[i])):
                octMat[i][j][0] += 1
        # next, flashing happens
        for i in range(len(octMat)):
            for j in range(len(octMat[i])):
                if octMat[i][j][0] > 9:
                    numFlashes = flash(octMat, i, j)
                    if numFlashes == 100:
                        synchron = s
                        break
            if synchron > 0:
                break
        if synchron > 0:
            break
        # reset flashing flag
        for i in range(len(octMat)):
            for j in range(len(octMat[i])):
                octMat[i][j][1] = False
        s += 1
    # print("final matrix:")
    # printOctMat(octMat)
    # print("flashes:", totFlashes)
    print("Synchronized at step {}".format(synchron))


main()
