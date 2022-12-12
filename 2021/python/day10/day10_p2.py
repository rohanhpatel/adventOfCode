import sys
import csv
import math
import numpy as np

def readFile(file):
    dataFile = open(file)
    data = []
    for line in dataFile:
        data.append(list(line.strip("\n")))
    return data

def score(c):
    if c == ')':
        return 1
    elif c == ']':
        return 2
    elif c == '}':
        return 3
    elif c == '>':
        return 4
    return -1

def getComplement(c):
    if c == '(':
        return ')'
    elif c == '[':
        return ']'
    elif c == '{':
        return '}'
    elif c == '<':
        return '>'
    return '-'


def main():
    syntaxList = readFile(sys.argv[1])
    synScore = 0
    endingLines = []
    for line in syntaxList:
        string = ""
        for c in line:
            string += str(c)
            substring = string[len(string)-2:]
            if substring == "()" or substring == "[]" or substring == "{}" or substring == "<>":
                string = string[0:len(string)-2]
        addToList = True
        for c in string:
            if c == ')' or c == ']' or c == '}' or c == '>':
                addToList = False
                break
        if addToList:
            endingLines.append(string)

    finScores = []
    for string in endingLines:
        endString = ""
        autoScore = 0
        stringList = list(string)
        for i in range(len(stringList) - 1, -1, -1):
            cur = stringList[i]
            comp = getComplement(cur)
            autoScore = autoScore * 5 + score(comp)
        finScores.append(autoScore)
    finScores.sort()
    mid = int((len(finScores) - 1)/2)
    print(finScores[mid])

main()
