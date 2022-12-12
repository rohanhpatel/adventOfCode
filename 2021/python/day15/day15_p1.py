import sys
import csv
import math
import numpy as np

def readFile(inputFile):
    dataFile = open(inputFile)
    octMat = []
    for line in dataFile:
        strLine = list(line.strip('\n'))
        octLine = []
        for string in strLine:
            octLine.append([int(string), float('inf')])
        octMat.append(octLine)
    return octMat

def calcMinDistance(mat, x, y):
    if x == 0 and y == 0:
        mat[x][y][1] = 0
    else:
        edgeVal = mat[x][y][0]
        surroundList = list()
        if x != 0:
            surroundList.append(mat[x-1][y][1])
        if y != 0:
            surroundList.append(mat[x][y-1][1])
        minimum = min(surroundList) + edgeVal
        if minimum < mat[x][y][1]:
            mat[x][y][1] = minimum
    if x == len(mat) - 1 and y == len(mat) - 1:
        return
    if x != len(mat) - 1:
        calcMinDistance(mat, x+1, y)
    if y != len(mat) - 1:
        calcMinDistance(mat, x, y+1)

#def shortestPath(mat):
#    vertexList = []
#    mat[0][0][1] = 0
#    while True:
#        # find min. dist. node not in vertexList
#        minDist = float('inf')
#        x = 0
#        y = 0
#        for i in range(len(mat)):
#            for j in range(len(mat[i])):
#                if not [i, j] in vertexList:
#                    if mat[i][j][1] < minDist:
#                        x = i
#                        y = j
#                        minDist = mat[i][j][1]
#        # add vertex to vertexList
#        vertexList.append([x, y])
#        # now update values around
#        if x != 0:
#            mat[x-1][y][1] = minDist + mat[x-1][y][0]
#        if x != len(mat) - 1:
#            mat[x+1][y][1] = minDist + mat[x+1][y][0]
#        if y != 0:
#            mat[x][y-1][1] = minDist + mat[x][y-1][0]
#        if y != len(mat[x]) - 1:
#            mat[x][y+1][1] = minDist + mat[x][y+1][0]
#        allChecked = True
#        # check to see if all values have distance values less than infinity
#        for i in range(len(mat)):
#            for j in range(len(mat[i])):
#                if mat[i][j][1] == float('inf'):
#                    allChecked = False
#                    break
#            if not allChecked:
#                break
#        if allChecked:
#            break
#    return mat[-1][-1][1]

def main():
    dataMat = readFile(sys.argv[1])
    smallestRisk = calcMinDistance(dataMat, 0, 0)
    print("smallest risk:")
    print(dataMat[-1][-1][1])

main()
