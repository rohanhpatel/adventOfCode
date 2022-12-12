import sys
import csv
import math

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

bingoInd = -1
lastNum = 0

print("starting")
for num in bingoNums:
    for b in range(len(bingoBoards)):
        board = bingoBoards[b]
        # update each board with num being "marked"
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j][0] == num and board[i][j][1] == False:
                    board[i][j][1] = True
        # now check each board to see if it has "bingo"
        for i in range(len(board)):
            bingo = True
            for j in range(len(board[i])):
                bingo = bingo and board[i][j][1]
            if bingo:
                bingoInd = b
                lastNum = num
                break
        for j in range(len(board[0])):
            bingo = True
            for i in range(len(board)):
                bingo = bingo and board[i][j][1]
            if bingo:
                bingoInd = b
                lastNum = num
                break
        if bingoInd >= 0:
            break
    if bingoInd >= 0:
        break

goodBoard = bingoBoards[bingoInd]
sum = 0

for i in range(len(goodBoard)):
    for j in range(len(goodBoard[i])):
        if not goodBoard[i][j][1]:
            sum += goodBoard[i][j][0]

print("Sum: " + str(sum))

print("Last Num: " + str(lastNum))

print("Result: " + str(lastNum * sum))
