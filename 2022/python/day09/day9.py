import sys
import math
import os

def parseFile(f):
    inpFile = open(f, 'r')
    headDirs = list()
    for line in inpFile:
        lst = line.strip().split(" ")
        headDirs.append((lst[0], lst[1]))
    return headDirs

def isTailTouchingHead(head, tail):
    x_diff = abs(head[0] - tail[0])
    y_diff = abs(head[1] - tail[1])
    return x_diff <= 1 and y_diff <= 1

def dirToTuple(direction):
    if direction == 'U':
        return (0, 1)
    elif direction == 'R':
        return (1, 0)
    elif direction == 'L':
        return (-1, 0)
    elif direction == 'D':
        return (0, -1)

def moveRope(head, tail, direction):
    dirTuple = dirToTuple(direction)
    newHead = [0, 0]
    for i in range(len(head)):
        newHead[i] = head[i] + dirTuple[i]
    newTail = tail.copy()
    if not isTailTouchingHead(newHead, newTail):
        if newTail[0] > newHead[0]:
            newTail[0] = newTail[0] - 1
        elif newTail[0] < newHead[0]:
            newTail[0] = newTail[0] + 1
        if newTail[1] > newHead[1]:
            newTail[1] = newTail[1] - 1
        elif newTail[1] < newHead[1]:
            newTail[1] = newTail[1] + 1
    return (newHead.copy(), newTail.copy())

def moveRope(rope, direction):
    dirTuple = dirToTuple(direction)
    for i in range(len(dirTuple)):
        rope[0][i] += dirTuple[i]
    for i in range(len(rope)-1):
        if not isTailTouchingHead(rope[i], rope[i+1]):
            if rope[i+1][0] > rope[i][0]:
                rope[i+1][0] = rope[i+1][0] - 1
            elif rope[i+1][0] < rope[i][0]:
                rope[i+1][0] = rope[i+1][0] + 1
            if rope[i+1][1] > rope[i][1]:
                rope[i+1][1] = rope[i+1][1] - 1
            elif rope[i+1][1] < rope[i][1]:
                rope[i+1][1] = rope[i+1][1] + 1
    return rope

def part1():
    directions = parseFile(sys.argv[1])
    head = [0, 0]
    tail = [0, 0]
    tailPos = list()
    tailPos.append(tail.copy())
    # for this, +1 to first coord = right, and +1 to second coord = up
    for direction, mv in directions:
        moves = int(mv)
        for i in range(moves):
            head, tail = moveRope(head, tail, direction)
            add = True
            for item in tailPos:
                if tail[0] == item[0] and tail[1] == item[1]:
                    add = False
                    break
            if add:
                tailPos.append(tail.copy())
    print("Number of unique places visited: " + str(len(tailPos)))
        

def part2():
    directions = parseFile(sys.argv[1])
    rope = list()
    tailPos = list()
    for i in range(10):
        rope.append([0, 0])
    tailPos.append(rope[9].copy())
    # head is rope[0] and tail is rope[9]
    for direction, mv in directions:
        moves = int(mv)
        for i in range(moves):
            rope = moveRope(rope, direction)
            add = True
            for item in tailPos:
                if rope[9][0] == item[0] and rope[9][1] == item[1]:
                    add = False
                    break
            if add:
                tailPos.append(rope[9].copy())
    print("Number of unique places the tail visited: " + str(len(tailPos)))

part2()
