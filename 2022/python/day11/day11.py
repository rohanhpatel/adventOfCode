import sys
import os
import math

class Monkey:
    def __init__(self, number, itemList, operation, testParams):
        self.num = number
        self.items = itemList
        self.op = operation
        self.params = testParams 
    def throw(self):
        return self.items.pop(0)
    def catch(self, it):
        self.items.append(it)
    def test(self):
        div, m1, m2 = self.params
        if self.items[0] % div == 0:
            return m1
        else:
            return m2
    def inspect(self):
        old = self.items[0]
        # divide the worry level by 3
        self.items[0] = int(eval(self.op)/3)
    def r_inspect(self): # for part 2
        old = self.items[0]
        self.items[0] = eval(self.op)
    def value(self):
        return self.num

def parseFile(f):
    inpFile = open(f, 'r')
    allMonkeys = list()
    monkParam = list()
    testParams = list()
    for line in inpFile:
        actLine = line.strip().split(":")
        if actLine[0][0:6] == 'Monkey':
            monkeySplit = actLine[0].split(" ")
            monkParam.append(int(monkeySplit[-1]))
        elif actLine[0] == "Starting items":
            monkItems = list()
            listItems = actLine[1].split(",")
            for item in listItems:
                monkItems.append(int(item))
            monkParam.append(monkItems)
        elif actLine[0] == "Operation":
            monkOp = actLine[1].strip()[5:]
            monkParam.append(monkOp)
        elif actLine[0] == "Test":
            divNum = actLine[1].strip()[12:]
            testParams.append(int(divNum))
        elif actLine[0] == "If true":
            monkTrueNum = actLine[1].strip()[15:]
            testParams.append(int(monkTrueNum))
        elif actLine[0] == "If false":
            monkFalseNum = actLine[1].strip()[15:]
            testParams.append(int(monkFalseNum))
            monkParam.append(testParams.copy())
            monkey = Monkey(monkParam[0], monkParam[1], monkParam[2], monkParam[3])
            allMonkeys.append(monkey)
            monkParam = list()
            testParams = list()
    return allMonkeys

def throwMTM(m1, m2):
   item = m1.throw()
   m2.catch(item)

def part1():
    allMonkeys = parseFile(sys.argv[1])
    inspectCount = list()
    for i in range(len(allMonkeys)):
        inspectCount.append(0)
    for r in range(20):
        for m in range(len(allMonkeys)):
            monkey = allMonkeys[m]
            initLen = len(monkey.items)
            inspectCount[m] += initLen
            for i in range(initLen):
                monkey.inspect()
                mNum = monkey.test()
                target = None
                for trgt in allMonkeys:
                    if mNum == trgt.value():
                        target = trgt
                        break
                throwMTM(monkey, trgt)
    inspectCount.sort(reverse = True)
    print("Monkey business: " + str(inspectCount[0] * inspectCount[1]))

def part2():
    allMonkeys = parseFile(sys.argv[1])
    inspectCount = dict()
    for monkey in allMonkeys:
        inspectCount[monkey.value()] = 0
    for r in range(10000):
        for m in range(len(allMonkeys)):
            monkey = allMonkeys[m]
            initLen = len(monkey.items)
            if initLen > 0:
                inspectCount[m] += initLen
            for _ in range(initLen):
                monkey.r_inspect()
                mNum = monkey.test()
                target = None
                for trgt in allMonkeys:
                    if mNum == trgt.value():
                        target = trgt
                        break
                throwMTM(monkey, trgt)
        if r % 500 == 0:
            print(r)
    inspectCount.sort(reverse = True)
    print("Monkey business: " + str(inspectCount[0] * inspectCount[1]))

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
