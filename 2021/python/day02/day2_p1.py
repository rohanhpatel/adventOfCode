import sys
import csv
import math

datafile = open("input.txt")
filereader = csv.reader(datafile, delimiter=" ")
pos = [0, 0]
#storing data into a matrix
for line in filereader:
    dir = line[0]
    if dir == "forward":
        pos[0] += int(line[1])
    elif dir == "up":
        pos[1] -= int(line[1])
    elif dir == "down":
        pos[1] += int(line[1])

print(pos)
print(pos[0] * pos[1])
