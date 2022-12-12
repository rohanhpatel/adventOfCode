import sys
import csv
import math

# only considering horizontal and vertical lines

datafile = open(sys.argv[1])
lines = []
min = [float('inf'), float('inf')]
max = [float('-inf'), float('-inf')]

for line in datafile:
    two_pts = line.split('->')
    tmp_line = []
    for i in range(2):
        string = two_pts[i].split(",")
        tup = (int(string[0]), int(string[1]))
        if tup[0] > max[0]:
            max[0] = tup[0]
        if tup[1] > max[1]:
            max[1] = tup[1]
        if tup[0] < min[0]:
            min[0] = tup[0]
        if tup[1] < min[1]:
            min[1] = tup[1]
        tmp_line.append(tup)
    lines.append(tmp_line)

graph = []
for i in range(max[1]-min[1] + 1):
    graph.append([0] * (max[0] - min[0] + 1))

for ray in lines:
    pt1 = ray[0]
    pt2 = ray[1]
    if pt1[0] != pt2[0] and pt1[1] != pt2[1]:
        continue
    elif pt1[0] == pt2[0]:
        x = pt1[0] - min[0]
        step = 1
        if pt1[1] > pt2[1]:
            step = -1
        for y in range(pt1[1] - min[1], pt2[1] - min[1] + step, step):
            graph[x][y] += 1
    elif pt1[1] == pt2[1]:
        y = pt1[1] - min[1]
        step = 1
        if pt1[0] > pt2[0]:
            step = -1
        for x in range(pt1[0] - min[0], pt2[0] - min[0] + step, step):
            graph[x][y] += 1

pts = 0
for r in range(len(graph)):
    for c in range(len(graph[r])):
        if graph[r][c] >= 2:
            pts += 1

print(pts)
