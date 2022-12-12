import sys
import csv
import math

def getRating(data, ox):
    length = len(data[0])
    tmp_data = data
    for i in range(length):
        if len(tmp_data) == 1:
            break
        compare = [0, 0]
        for str in tmp_data:
            compare[(int(str[i]))] += 1
        new_data = []
        if compare[0] > compare[1]:
            for d in tmp_data:
                if (ox and d[i] == "0") or (not ox and d[i] == "1"):
                    new_data.append(d)
        else:
            for d in tmp_data:
                if (ox and d[i] == "1") or (not ox and d[i] == "0"):
                    new_data.append(d)
        tmp_data = new_data.copy()
    return tmp_data[0]

datafile = open("input.txt")
data = []
for line in datafile:
    data.append(line.strip('\n'))

length = len(data[0])
oxygen = getRating(data, True)
co2 = getRating(data, False)

ox_rate = int(oxygen, 2)
co2_rate = int(co2, 2)

print(ox_rate * co2_rate)
