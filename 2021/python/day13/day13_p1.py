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

def main():
    dots, commands = readFile(sys.argv[1])
    # for com in commands:
    # print("before:")
    # print(dots)
    # print(len(dots))
    com = commands[0]
    newDots = []
    if com[0] == 'x':
        for pt in dots:
            if pt[0] > com[1]:
                newX = pt[0] - 2 * (pt[0] - com[1])
                newPt = [newX, pt[1]]
                if not newPt in newDots:
                    newDots.append(newPt)
            elif not pt in newDots:
                newDots.append(pt)
    if com[0] == 'y':
        for pt in dots:
            if pt[1] > com[1]:
                newY = pt[1] - 2 * (pt[1] - com[1])
                newPt = [pt[0], newY]
                if not newPt in newDots:
                    newDots.append(newPt)
            elif not pt in newDots:
                newDots.append(pt)

    # print("after:")
    # print(newDots)
    print(len(newDots))

main()
