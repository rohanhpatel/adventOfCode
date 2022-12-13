import sys
import os
import math
from dill.source import getsource

def listFromStr(string):
    if len(string) == 2:
        return list()
    noParen = string[1:len(string)-1]
    argList = noParen.split(',')
    fullList = list()
    i = 0
    while i < len(argList):
        elem = argList[i]
        if elem[0] == '[':
            j = i
            score = 0
            while j < len(argList):
                charList = list(argList[j])
                k = 0
                while charList[k] == '[':
                    score += 1
                    k += 1
                k = -1
                while charList[k] == ']':
                    score -= 1
                    k -= 1
                if score == 0:
                    break
                j += 1
            smString = ','.join(argList[i:j+1])
            fullList.append(listFromStr(smString))
            i = j
        else:
            fullList.append(int(elem))
        i += 1
    return fullList

def parseFile(f):
    inpFile = open(f, 'r')
    pairs = list()
    tmpList = list()
    for line in inpFile:
        actLine = line.strip()
        if len(actLine) == 0:
            pairs.append(tmpList.copy())
            tmpList = list()
        else:
            tmpList.append(listFromStr(actLine))
    pairs.append(tmpList.copy())
    return pairs

def comparePair(pair):
    left = pair[0]
    right = pair[1]
    if type(left) == type(right):
        if type(left) == int:
            if left == right:
                return 0
            elif left < right: 
                return 1
            else:
                return -1
        elif type(left) == list:
            i = 0
            while i < len(left) and i < len(right):
                res = comparePair([left[i], right[i]])
                if res != 0:
                    return res
                else:
                    i += 1
            if i == len(left) and i == len(right):
                return 0
            elif i == len(left):
                return 1
            else:
                return -1
    else:
        tmpLeft = list()
        tmpRight = list()
        if type(left) == int:
            tmpLeft.append(left)
        else:
            tmpLeft = left.copy()
        if type(right) == int:
            tmpRight.append(right)
        else:
            tmpRight = right.copy()
        i = 0
        while i < len(tmpLeft) and i < len(tmpRight):
            res = comparePair([tmpLeft[i], tmpRight[i]])
            if res != 0:
                return res
            else:
                i += 1
        if i == len(tmpLeft) and i == len(tmpRight):
            return 0
        elif i == len(tmpLeft):
            return 1
        else:
            return -1
def part1():
    pairs = parseFile(sys.argv[1])
    total = 0
    for p in range(len(pairs)):
        # time to compare the two elements in pair
        res = comparePair(pairs[p])
        if res == 1:
            total += p+1
    print("Sum of indices: " + str(total))

def packetSort(allPackets):
    if len(allPackets) == 1:
        return allPackets
    halfInd = int(len(allPackets)/2)
    left = allPackets[:halfInd]
    right = allPackets[halfInd:]
    tmpLeft = packetSort(left)
    tmpRight = packetSort(right)
    combined = merge(tmpLeft, tmpRight)
    return combined

def merge(left, right):
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    else:
        li = 0
        ri = 0
        combined = list()
        while li < len(left) and ri < len(right):
            result = comparePair([left[li], right[ri]])
            if result == 1: # left is "smaller" than right
                combined.append(left[li])
                li += 1
            elif result == -1:
                combined.append(right[ri])
                ri += 1
        if li == len(left):
            combined += right[ri:]
        elif ri == len(right):
            combined += left[li:]
        return combined

def part2():
    pairs = parseFile(sys.argv[1])
    allPackets = list()
    dividerPackets = [ [[2]], [[6]] ]
    allPackets += dividerPackets
    for pair in pairs:
        allPackets += pair
    sortedPackets = packetSort(allPackets)
    indices = [0, 0]
    for p in range(len(sortedPackets)):
        packet = sortedPackets[p]
        if packet == [[2]]:
            indices[0] = p + 1
        elif packet == [[6]]:
            indices[1] = p + 1
            break
    print("Decoder key: " + str(indices[0] * indices[1]))

def main():
    if len(sys.argv) < 3:
        print("Not enough arguments")
        exit(1)
    part = int(sys.argv[2])
    if part == 1:
        part1()
    elif part == 2:
        part2()
    else:
        print("Not a valid part")

main()
