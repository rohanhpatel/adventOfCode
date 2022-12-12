import sys
import math
import os

def parseFile(f):
    inpFile = open(f, 'r')
    instructions = list()
    for line in inpFile:
        instructions.append(line.strip().split(" "))
    return instructions

def part1():
    instrs = parseFile(sys.argv[1])
    x = 1
    instrNum = 0
    cycleNum = 1
    start = -1
    keyCycles = [20, 60, 100, 140, 180, 220]
    signalStrength = list()
    while True:
        # start of cycle
        inst = instrs[instrNum]
        # check x value
        if cycleNum in keyCycles:
            signalStrength.append(cycleNum * x)
            if cycleNum == keyCycles[-1]:
                break
        # complete rest of the cycle
        if inst[0] == 'noop':
            instrNum += 1
        if inst[0] == 'addx':
            if start == -1:
                start = cycleNum
            elif cycleNum - start == 1:
                    x += int(inst[1])
                    instrNum += 1
                    start = -1
        # start next cycle
        cycleNum += 1
    print("The sum of signal strengths is: " + str(sum(signalStrength)))


def part2():
    instrs = parseFile(sys.argv[1])
    x = 1
    instrNum = 0
    cycleNum = 1
    start = -1
    crt = ""
    while instrNum < len(instrs):
        # start of cycle
        inst = instrs[instrNum]
        # do the drawing
        pixelPos = (cycleNum - 1) % 40
        if abs(pixelPos - x) <= 1:
            crt += '#'
        else:
            crt += '.'
        if cycleNum % 40 == 0:
            crt += "\n"
        # complete rest of the cycle
        if inst[0] == 'noop':
            instrNum += 1
        if inst[0] == 'addx':
            if start == -1:
                start = cycleNum
            elif cycleNum - start == 1:
                    x += int(inst[1])
                    instrNum += 1
                    start = -1
        # start next cycle
        cycleNum += 1
    print(crt)

part2()
