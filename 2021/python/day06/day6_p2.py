import sys
import csv
import math

datafile = open(sys.argv[1])
fish = []
onlyLine = ""
for line in datafile:
    onlyLine = line
string = onlyLine.split(",")
for s in string:
    fish.append(int(s))

def numCreatedFish(fishDays, totDays):
    newDays = totDays - (fishDays + 1)
    if newDays < 0:
        return 0
    else:
        numFish = 1 + newDays // 7
        while newDays >= 0:
            newFish = numCreatedFish(8, newDays)
            numFish += newFish
            newDays -= 7
        return numFish


num_days = int(sys.argv[2])

uniqueFish = set()
for i in range(len(fish)):
    uniqueFish.add(fish[i])

fishVals = dict()
for f in uniqueFish:
    # print("On fish", str(i))
    createdFish = numCreatedFish(f, num_days)
    print("Number of fish made from", str(f), "is", str(createdFish))
    fishVals[f] = createdFish

tot_fish = len(fish)
for i in range(len(fish)):
    tot_fish += fishVals[fish[i]]

print(tot_fish)
