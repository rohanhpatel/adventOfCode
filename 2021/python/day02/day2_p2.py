import sys
import csv
import math

datafile = open("input.txt")
filereader = csv.reader(datafile, delimiter=" ")
pos = [0, 0, 0]
#storing data into a matrix
for line in filereader:
    dir = line[0]
    X = int(line[1])
    if dir == "forward":
        pos[0] += X
        pos[1] += X * pos[2]
    elif dir == "up":
        pos[2] -= X
    elif dir == "down":
        pos[2] += X

print(pos)
print(pos[0] * pos[1])
