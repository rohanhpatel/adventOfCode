import sys
import csv
import math

datafile = open("input.txt")
data = []
for line in datafile:
    data.append(line.strip('\n'))

length = len(data[0])
gamma_s = ""
eps_s = ""
for i in range(length):
    compare = [0, 0]
    for str in data:
        compare[(int(str[i]))] += 1
    if compare[0] > compare[1]:
        gamma_s += "0"
        eps_s += "1"
    else:
        gamma_s += "1"
        eps_s += "0"

gamma = int(gamma_s, 2)
eps = int(eps_s, 2)

print(gamma * eps)
