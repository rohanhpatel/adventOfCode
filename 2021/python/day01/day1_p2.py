import sys
import csv
import math

datafile = open("input.txt")
data = []
#storing data into a list
for line in datafile:
    data.append(int(line))

cur = [data[0], data[1], data[2]]
nxt = [data[1], data[2]]
i = 3
res = 0
while (i < len(data)):
    nxt.append(data[i])
    if (sum(nxt) > sum(cur)):
        res += 1
    cur = nxt.copy()
    nxt.pop(0)
    i += 1

print(res)
