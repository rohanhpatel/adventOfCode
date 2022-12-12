import sys
import csv
import math

def printBoard(board):
    for i in range(len(board)):
        print(board[i])

datafile = open(sys.argv[1])
firstLine = True
bingoNums = []
data = []
loopNum = 0
bingoBoards = []
curBingoBoard = []
# reading in the data
for line in datafile:
    if firstLine:
        bingoStr = line.split(",")
        for b in bingoStr:
            bingoNums.append(int(b))
        firstLine = False
    else:
        if loopNum == 0:
            curBingoBoard = []
        else:
            new_line = line.strip('\n')
            strArr = line.split(" ")
            bingoRow = []
            for string in strArr:
                if string != '':
                    bingoRow.append([int(string), False])
            curBingoBoard.append(bingoRow)
            if loopNum == 5:
                bingoBoards.append(curBingoBoard)
        loopNum += 1
        loopNum = loopNum % 6

# print("all boards")
# for board in bingoBoards:
#     print(board)

boardsWBingo = [-1] * len(bingoBoards)
n = 0
lastNum = 0
numInd = 0

for num in range(len(bingoNums)):
    # check to see if all except one board has bingo
    onlyOneMinus = 0
    for b in boardsWBingo:
        if b == -1:
            onlyOneMinus += 1
    if onlyOneMinus == 1:
        numInd = num
        break
    for b in range(len(bingoBoards)):
        board = bingoBoards[b]
        # update each board with num being "marked"
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j][0] == bingoNums[num] and board[i][j][1] == False:
                    board[i][j][1] = True
        # now check each board to see if it has "bingo"
        for i in range(len(board)):
            bingo = True
            for j in range(len(board[i])):
                bingo = bingo and board[i][j][1]
            if bingo:
                boardsWBingo[b] = n
                n += 1
                break
        if boardsWBingo[b] >= 0:
            continue
        for j in range(len(board[0])):
            bingo = True
            for i in range(len(board)):
                bingo = bingo and board[i][j][1]
            if bingo:
                boardsWBingo[b] = n
                n += 1
                break

boardInd = 0
for i in range(len(boardsWBingo)):
    if boardsWBingo[i] == -1:
        boardInd = i
        break

lastBoard = bingoBoards[boardInd]
lastBingo = False

while numInd < len(bingoNums):
    number = bingoNums[numInd]
    for i in range(len(lastBoard)):
        for j in range(len(lastBoard[i])):
            if lastBoard[i][j][0] == number and lastBoard[i][j][1] == False:
                lastBoard[i][j][1] = True
    # now check each board to see if it has "bingo"
    for i in range(len(lastBoard)):
        bingo = True
        for j in range(len(lastBoard[i])):
            bingo = bingo and lastBoard[i][j][1]
        if bingo:
            lastNum = number
            lastBingo = True
            break
    for j in range(len(lastBoard[0])):
        bingo = True
        for i in range(len(lastBoard)):
            bingo = bingo and lastBoard[i][j][1]
        if bingo:
            lastNum = number
            lastBingo = True
            break
    if lastBingo:
        break
    numInd += 1

sum = 0

for i in range(len(lastBoard)):
    for j in range(len(lastBoard[i])):
        if lastBoard[i][j][1] == False:
            sum += lastBoard[i][j][0]

print("Sum: " + str(sum))

print("Last Num: " + str(lastNum))

print("Result: " + str(lastNum * sum))
