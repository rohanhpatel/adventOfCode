import sys
import csv
import math
import numpy as np

def readFile(file):
    dataFile = open(file)
    foldCommands = False
    dots = []
    commands = []
    for line in dataFile:
        if line == "\n":
            foldCommands = True
        elif not foldCommands:
            strPt = line.strip('\n').split(',')
            dots.append([int(strPt[0]), int(strPt[1])])
        elif foldCommands:
            impLine = line[11:]
            strComm = impLine.strip('\n').split('=')
            commands.append([strComm[0], int(strComm[1])])
    return (dots, commands)

def printDots(dots):
    xBounds = [float('inf'), float('-inf')]
    yBounds = [float('inf'), float('-inf')]
    for pt in dots:
        if pt[0] < xBounds[0]:
            xBounds[0] = pt[0]
        if pt[0] > xBounds[1]:
            xBounds[1] = pt[0]
        if pt[1] < yBounds[0]:
            yBounds[0] = pt[1]
        if pt[1] > yBounds[1]:
            yBounds[1] = pt[1]
    for y in range(yBounds[0], yBounds[1] + 1):
        lineString = ""
        for x in range(xBounds[0], xBounds[1] + 1):
            newPt = [x, y]
            if newPt not in dots:
                lineString += '.'
            else:
                lineString += '#'
        print(lineString)


def main():
    dots, commands = readFile(sys.argv[1])
    curDots = dots
    for com in commands:
        newDots = []
        if com[0] == 'x':
            for pt in curDots:
                if pt[0] > com[1]:
                    newX = pt[0] - 2 * (pt[0] - com[1])
                    newPt = [newX, pt[1]]
                    if not newPt in newDots:
                        newDots.append(newPt)
                elif not pt in newDots:
                    newDots.append(pt)
        if com[0] == 'y':
            for pt in curDots:
                if pt[1] > com[1]:
                    newY = pt[1] - 2 * (pt[1] - com[1])
                    newPt = [pt[0], newY]
                    if not newPt in newDots:
                        newDots.append(newPt)
                elif not pt in newDots:
                    newDots.append(pt)
        curDots = newDots

    printDots(curDots)
    # print(curDots)

main()
