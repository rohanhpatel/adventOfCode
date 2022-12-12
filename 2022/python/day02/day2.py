import sys
import math

def getMappings():
    letterMap = dict()
    charArr = ['A', 'B', 'C', 'X', 'Y', 'Z']
    for i in range(len(charArr)):
        curChar = charArr[i]
        if i%3 == 0:
            letterMap[curChar] = 'rock'
        elif i%3 == 1:
            letterMap[curChar] = 'paper'
        else:
            letterMap[curChar] = 'scissors'
    beatsOut = dict()
    beatsOut['rock'] = 'paper'
    beatsOut['paper'] = 'scissors'
    beatsOut['scissors'] = 'rock'
    valueMap = dict()
    valueMap['rock'] = 1
    valueMap['paper'] = 2
    valueMap['scissors'] = 3
    return (letterMap, beatsOut, valueMap)

def parseFile(fileName):
    inpFile = open(fileName, "r")
    allInput = list()
    for line in inpFile:
        allInput.append(line.strip().split(" "))
    return allInput

def getResults(yourChoice, oppChoice, valueMap, winsAgainst):
    gameScore = valueMap[yourChoice]
    if yourChoice == oppChoice:
        gameScore += 3
    elif oppChoice == winsAgainst[yourChoice]:
        gameScore += 0
    else:
        gameScore += 6
    return gameScore

def part1(fileName):
    charMap, winsAgainst, valueMap = getMappings()
    fullInput = parseFile(fileName)
    totalScore = 0
    for game in fullInput:
        oppChoice = charMap[game[0]]
        yourChoice = charMap[game[1]]
        totalScore += getResults(yourChoice, oppChoice, valueMap, winsAgainst)
    return totalScore

def part2(fileName):
    charMap, winsAgainst, valueMap = getMappings() #don't use X, Y, or Z from charMap to identify RPS
    fullInput = parseFile(fileName)
    totalScore = 0
    for game in fullInput:
        gameScore = 0
        oppChoice = charMap[game[0]]
        yourChoice = 'something'
        if game[1] == 'X': # you need to lose
            yourChoice = winsAgainst[winsAgainst[oppChoice]]
        elif game[1] == 'Y': # you need to draw
            yourChoice = oppChoice
        elif game[1] == 'Z': # you need to win
            yourChoice = winsAgainst[oppChoice]
        totalScore += getResults(yourChoice, oppChoice, valueMap, winsAgainst)
    return totalScore

print(part2(sys.argv[1]))
