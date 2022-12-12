import sys
import csv
import math

datafile = open(sys.argv[1])
tmp_lines = []
min_val = float('inf')
max_val = float('-inf')

for line in datafile:
    two_pts = line.split('->')
    tmp_line = []
    for i in range(2):
        string = two_pts[i].split(",")
        tup = (int(string[0]), int(string[1]))
        lowest = min(tup[0], tup[1])
        if lowest < min_val:
            min_val = lowest
        tmp_line.append(tup)
    tmp_lines.append(tmp_line)

lines = []
for ray in tmp_lines:
    pt1 = ray[0]
    pt2 = ray[1]
    x1 = pt1[0] - min_val
    y1 = pt1[1] - min_val
    x2 = pt2[0] - min_val
    y2 = pt2[1] - min_val
    highest = max(x1, y1, x2, y2)
    if highest > max_val:
        max_val = highest
    lines.append([(x1, y1), (x2, y2)])

graph = []
for _ in range(max_val + 1):
    graph.append([0] * (max_val + 1))

print(min_val)

for ray in lines:
    pt1 = ray[0]
    pt2 = ray[1]
    if pt1[0] != pt2[0] and pt1[1] != pt2[1]:
        step_x = 1
        step_y = 1
        if pt1[0] > pt2[0]:
            step_x = -1
        if pt1[1] > pt2[1]:
            step_y = -1
        num_steps = abs(pt1[0] - pt2[0]) + 1
        x = pt1[0]
        y = pt1[1]
        x_end = pt2[0] + step_x
        y_end = pt2[1] + step_y
        for _ in range(num_steps):
            graph[x][y] += 1
            x += step_x
            y += step_y
    elif pt1[0] == pt2[0]:
        x = pt1[0]
        step = 1
        if pt1[1] > pt2[1]:
            step = -1
        for y in range(pt1[1], pt2[1] + step, step):
            graph[x][y] += 1
    elif pt1[1] == pt2[1]:
        y = pt1[1]
        step = 1
        if pt1[0] > pt2[0]:
            step = -1
        for x in range(pt1[0], pt2[0] + step, step):
            graph[x][y] += 1

pts = 0
for r in range(len(graph)):
    for c in range(len(graph[r])):
        if graph[r][c] >= 2:
            pts += 1

print(pts)
