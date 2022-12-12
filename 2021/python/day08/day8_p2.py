import sys
import csv
import math
import numpy as np

def setEquals(s1, s2):
    return s1.issuperset(s2) and s1.issubset(s2)

def convert(wireMap, s):
    retSet = set()
    for x in s:
        for key, val in wireMap.items():
            if x == val:
                retSet.add(key)
    return retSet

def decode(s):
    nums = defineNumSets()
    for i in range(len(nums)):
        if setEquals(s, nums[i]):
            return i
    return -1

def defineNumSets():
    zero = {'a', 'b', 'c', 'e', 'f', 'g'}
    one = {'c', 'f'}
    two = {'a', 'c', 'd', 'e', 'g'}
    three = {'a', 'c', 'd', 'f', 'g'}
    four = {'b', 'c', 'd', 'f'}
    five = {'a', 'b', 'd', 'f', 'g'}
    six = {'a', 'b', 'd', 'e', 'f', 'g'}
    seven = {'a', 'c', 'f'}
    eight = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    nine = {'a', 'b', 'c', 'd', 'f', 'g'}
    return [zero, one, two, three, four, five, six, seven, eight, nine]

def readFile(file):
    datafile = open(file)
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
    return probs

def solveProb(unique, outVals):
    nums = defineNumSets()
    allChars = set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    wireMap = dict()
    numMap = dict()
    # init dictionary
    for c in allChars:
        wireMap[c] = set()
    for n in range(10):
        numMap[n] = set()
    fiveList = []
    sixList = []
    done = False # done when each value is length 1, correct mapping
    ind = 0
    for curPat in unique:
        if len(curPat) == 2 or len(curPat) == 3 or len(curPat) == 4 or len(curPat) == 7: # the pattern is a 1, 7, 4, or 8 respectively
            if len(curPat) == 2:
                numMap[1] = curPat
            elif len(curPat) == 3:
                numMap[7] = curPat
            elif len(curPat) == 4:
                numMap[4] = curPat
            elif len(curPat) == 7:
                numMap[8] = curPat
        elif len(curPat) == 5: # the pattern is either a 2, 3, or 5
            fiveList.append(curPat)
        elif len(curPat) == 6:
            sixList.append(curPat)
    # --------------------------------------
    # now onto actually solving the problem
    # --------------------------------------
    # we know that 7 has the 'a' wire additional to 1, so we can get the wiring for 'a' immediately
    for x in numMap[7].difference(numMap[1]):
        wireMap['a'] = x
    # we get 9 and 'g' can be deduced by removing 4 from 9, and then removing mapping for 'a'
    ind = 0
    for i in range(len(sixList)):
        finalSet = sixList[i].difference(numMap[4]).difference(set(wireMap['a']))
        if finalSet != set() and len(finalSet) == 1:
            for x in finalSet:
                wireMap['g'] = x
            numMap[9] = sixList[i]
            ind = i
            break
    sixList.pop(ind)
    # we can get 3 and 'd', by removing 'a' and 'g' and 1 from 3
    for i in range(len(fiveList)):
        finalSet = fiveList[i].difference(numMap[1]).difference(set(wireMap['a'])).difference(set(wireMap['g']))
        if finalSet != set() and len(finalSet) == 1:
            for x in finalSet:
                wireMap['d'] = x
            numMap[3] = fiveList[i]
            ind = i
            break
    fiveList.pop(ind)
    # we can get 'b' by removing 3 from 9
    for x in numMap[9].difference(numMap[3]):
        wireMap['b'] = x
    # we can get 'e' by removing 3 from the elements in fiveList
    for i in range(len(fiveList)):
        finalSet = fiveList[i].difference(numMap[3])
        for x in finalSet:
            if x != wireMap['b']:
                wireMap['e'] = x
                numMap[2] = fiveList[i]
                ind = i
    fiveList.pop(ind)
    numMap[5] = fiveList[0]
    # we can get 'f' by removing 2 and 'b' from 8
    for x in numMap[8].difference(numMap[2]).difference(set(wireMap['b'])):
        wireMap['f'] = x
    # we can get 'c' by removing 5 and 'e' from 8
    for x in numMap[8].difference(numMap[5]).difference(set(wireMap['e'])):
        wireMap['c'] = x
    # now we convert the output values into numbers and return the integer
    outStr = ""
    # print("wireMap:", str(wireMap))
    for out in outVals:
        # print("out:", str(out))
        convSet = convert(wireMap, out)
        # print("convSet:", str(convSet))
        outStr += str(decode(convSet))
    return int(outStr)


def main():
    probs = readFile(sys.argv[1])
    finalRes = 0
    for p in probs:
        p[0].pop(-1)
        p[1].pop(0)
        finalRes += solveProb(p[0], p[1])
    print(finalRes)


main()
