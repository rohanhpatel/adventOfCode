import sys
import math

class Directory:
    def __init__(self, val, parent):
        self.value = val
        self.children = list()
        self.files = list()
        self.parent = parent
    def addChild(self, child):
        self.children.append(child)
    def addFile(self, f, f_size):
        self.files.append((f, f_size))
    def getSize(self):
        size = 0
        for child in self.children:
            size += child.getSize()
        for fil in self.files:
            size += fil[1]
        return size
    def hasChild(self, val):
        for child in self.children:
            if child.value == val:
                return True
        return False
    def getChild(self, val):
        for child in self.children:
            if child.value == val:
                return child
    def __str__(self):
        string = self.value + "\n"
        childList = list()
        if len(self.children) != 0:
            for child in self.children:
                childList.append(child.value)
            string += "children: " + ", ".join(childList) + "\n"
        if len(self.files) != 0:
            for fil in self.files:
                string += str(fil[1]) + " " + fil[0] + "\n"
        return string

def parseFile(f):
    inpFile = open(f, 'r')
    parentDir = None
    curDir = None
    inp = inpFile.read().split('\n')
    for i in range(len(inp)):
        actLine = inp[i].strip().split()
        if len(actLine) == 0:
            break
        if actLine[0] == '$':
            if actLine[1] == 'cd':
                dir_ = actLine[2]
                if dir_ != "..":
                    if not curDir:
                        curDir = Directory(dir_, None)
                    else:
                        curDir = curDir.getChild(dir_)
                else:
                    curDir = curDir.parent
            elif actLine[1] == 'ls':
                i += 1
                actLine = inp[i].strip().split()
                while len(actLine) > 0 and actLine[0] != '$' and i < len(inp):
                    if actLine[0] == 'dir':
                        childDir = Directory(actLine[1], curDir)
                        if not curDir.hasChild(actLine[1]):
                            curDir.addChild(childDir)
                    else:
                        curDir.addFile(actLine[1], int(actLine[0]))
                    i += 1
                    actLine = inp[i].strip().split()                
    topDir = curDir
    while topDir.parent != None:
        topDir = topDir.parent
    return topDir

def part1Helper(root):
    size = 0
    if root.getSize() < 100000:
        size += root.getSize()
    for child in root.children:
        size += part1Helper(child)
    return size

def printAllDirs(root):
    print(root)
    for child in root.children:
        printAllDirs(child)

def part1():
    root = parseFile(sys.argv[1]) 
    combinedSize = part1Helper(root)
    print("Total size of dirs < 100000 is: " + str(combinedSize))

def part2Helper(root, unused):
    if unused + root.getSize() < 30000000:
        return -1
    elif root.children == list():
        return root.getSize()
    else:
        curSize = root.getSize()
        sizeList = list()
        for child in root.children:
            res = part2Helper(child, unused)
            if res != -1:
                sizeList.append(res)
        if len(sizeList) == 0:
            smallest = curSize + 1
        else:
            smallest = min(sizeList)
        if smallest < curSize:
            return smallest
        return curSize

def part2():
    root = parseFile(sys.argv[1])
    curUnused = 70000000 - root.getSize()
    smallestDirSize = part2Helper(root, curUnused)
    print("smallest dir size necessary is: " + str(smallestDirSize))

part2()
