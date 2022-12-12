import sys
import csv
import math
import numpy as np

def summation(n):
    return int(n * (n+1) / 2)

datafile = open(sys.argv[1])
crabSubs = []
onlyLine = ""
for line in datafile:
    onlyLine = line
string = onlyLine.split(",")
for s in string:
    crabSubs.append(int(s))

low = min(crabSubs)
high = max(crabSubs)

print("low:", str(low))
print("high:", str(high))

outcomes = []
for num in range(low, high + 1):
    fuelUse = 0
    for i in range(len(crabSubs)):
        fuelUse += summation(abs(crabSubs[i] - num))
    outcomes.append(fuelUse)

# print(outcomes)
smallestPos = np.argmin(outcomes)
print("horizontal position to align to:", str(smallestPos))
print("fuel needed:", str(outcomes[smallestPos]))
