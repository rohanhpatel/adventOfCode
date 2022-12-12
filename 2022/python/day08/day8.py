import sys
import math

def parseFile(f):
    inpFile = open(f, 'r')
    treeMat = list()
    for line in inpFile:
        actLine = line.strip()
        row = list()
        for c in actLine:
            row.append(int(c))
        treeMat.append(row)
    return treeMat

def isTreeVisible(mat, i, j):
    fourDirs = [True, True, True, True]
    # first check top
    i_ = i - 1
    while i_ >= 0:
        if mat[i_][j] >= mat[i][j]:
            fourDirs[0] = False
            break
        i_ -= 1
    # check bottom
    i_ = i + 1
    while i_ < len(mat):
        if mat[i_][j] >= mat[i][j]:
            fourDirs[1] = False
            break
        i_ += 1
    # check left
    j_ = j - 1
    while j_ >= 0:
        if mat[i][j_] >= mat[i][j]:
            fourDirs[2] = False
            break
        j_ -= 1
    # check right
    j_ = j + 1
    while j_ < len(mat[0]):
        if mat[i][j_] >= mat[i][j]:
            fourDirs[3] = False
            break
        j_ += 1
    return any(fourDirs)


def part1():
    mat = parseFile(sys.argv[1])
    numVis = (len(mat) - 1) * 4
    for i in range(1, len(mat) - 1):
        for j in range(1, len(mat[0]) - 1):
            if isTreeVisible(mat, i, j):
                numVis += 1
    print("Number of visible trees: " + str(numVis))

def getScenicScore(mat, i, j):
    scoreList = [0, 0, 0, 0]
    # get top mult
    i_ = i - 1
    while i_ >= 0:
        if mat[i_][j] >= mat[i][j]:
            break
        i_ -= 1
    if i_ == -1:
        scoreList[0] = i
    else:
        scoreList[0] = i - i_
    i_ = i + 1
    while i_ < len(mat):
        if mat[i_][j] >= mat[i][j]:
            break
        i_ += 1
    if i_ == len(mat):
        scoreList[1] = len(mat) - 1 - i
    else:
        scoreList[1] = i_ - i
    j_ = j - 1
    while j_ >= 0:
        if mat[i][j_] >= mat[i][j]:
            break
        j_ -= 1
    if j_ == -1:
        scoreList[2] = j
    else:
        scoreList[2] = j - j_
    j_ = j + 1
    while j_ < len(mat[0]):
        if mat[i][j_] >= mat[i][j]:
            break
        j_ += 1
    if j_ == len(mat[0]):
        scoreList[3] = len(mat[0]) - 1 - j
    else:
        scoreList[3] = j_ - j
    score = 1
    for s in scoreList:
        score *= s
    return score

def part2():
    mat = parseFile(sys.argv[1])
    maxScenicScore = -1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            scenicScore = getScenicScore(mat, i, j)
            if scenicScore > maxScenicScore:
                maxScenicScore = scenicScore
    print("The highest scenic score possible is: " + str(maxScenicScore))

part2()
