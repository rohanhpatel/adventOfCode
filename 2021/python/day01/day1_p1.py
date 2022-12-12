import sys
import csv
import math

datafile = open("input.txt")
data = []
#storing data into a list
for line in datafile:
    data.append(int(line))

cur = data[0]
i = 1
res = 0
while (i < len(data)):
    nxt = data[i]
    if nxt > cur:
        res += 1
    cur = nxt
    i += 1

print(res)
