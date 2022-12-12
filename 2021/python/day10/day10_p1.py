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
        return 3
    elif c == ']':
        return 57
    elif c == '}':
        return 1197
    elif c == '>':
        return 25137
    return -1

def main():
    syntaxList = readFile(sys.argv[1])
    synScore = 0
    for line in syntaxList:
        string = ""
        for c in line:
            string += str(c)
            substring = string[len(string)-2:]
            if substring == "()" or substring == "[]" or substring == "{}" or substring == "<>":
                string = string[0:len(string)-2]
        for c in string:
            if c == ')' or c == ']' or c == '}' or c == '>':
                synScore += score(c)
                break

    print(synScore)

main()
