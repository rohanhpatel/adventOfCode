import sys
import os
import math
from dill.source import getsource

def manualModulo(div, bigNum):
    num = bigNum
    while num > div:
        power = int(math.log(num, div))
        powNum = int(math.pow(div, power))
        while num >= powNum:
            num -= powNum
    return num == 0 

def recurMod(num, mod):
    if num < 10:
        return num % mod 
    else:
        lead = int(str(num)[0])
        rest = int(str(num)[1:])
        val1 = (lead % mod) * 10
        val2 = recurMod(rest, mod)
        return (val1 + val2) % mod

class Monkey:
    def __init__(self, params):
        self.num = params['num']
        self.items = params['items']
        self.op = params['op']
        self.params = params['test_params']
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
        # divide the worry level by 3
        old = self.items[0]
        self.items[0] = int(eval(self.op)/3)
    def r_inspect(self): # for part 2
        old = self.items[0]
        self.items[0] = int(eval(self.op))
    def value(self):
        return self.num
    def __str__(self):
        string = ""
        string += "Monkey " + str(self.value()) + ":" + '\n'
        string += "Items: " + ", ".join([str(x) for x in self.items]) + "\n"
        string += "Operation: new = " + self.op  + "\n"
        string += "Test parameters: " + ", ".join([str(x) for x in self.params]) + "\n"
        return string

def parseFile(f):
    inpFile = open(f, 'r')
    allMonkeys = list()
    monkParams = dict()
    testParams = list()
    for line in inpFile:
        actLine = line.strip().split(":")
        if actLine[0][0:6] == 'Monkey':
            monkeySplit = actLine[0].split(" ")
            monkParams['num'] = int(monkeySplit[-1])
        elif actLine[0] == "Starting items":
            monkItems = list()
            listItems = actLine[1].split(",")
            for item in listItems:
                monkItems.append(int(item))
            monkParams['items'] = monkItems
        elif actLine[0] == "Operation":
            expression = actLine.copy()[1].strip()[6:]
            monkParams['op'] = expression
        elif actLine[0] == "Test":
            divNum = actLine[1].strip()[12:]
            testParams.append(int(divNum))
        elif actLine[0] == "If true":
            monkTrueNum = actLine[1].split(" ")[-1]
            testParams.append(int(monkTrueNum))
        elif actLine[0] == "If false":
            monkFalseNum = actLine[1].split(" ")[-1]
            testParams.append(int(monkFalseNum))
            monkParams['test_params'] = testParams.copy()
            monkey = Monkey(monkParams.copy())
            allMonkeys.append(monkey)
            monkParams = dict()
            testParams = list()
#    for monkey in allMonkeys:
#        print(monkey)
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
    print(inspectCount)
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
            for i in range(initLen):
#                print("On monkey " + str(monkey.value()) + " and item " + str(i))
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

#print(manualModulo(23, 48))
#print(manualModulo(23, 46))
#print(manualModulo(23, 1801159097806))
#print("recursive mod")
#print(recurMod(23, 1801159097806) % 23)
main()
