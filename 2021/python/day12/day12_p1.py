import sys
import csv
import math
import numpy as np

def readFile(file):
    dataFile = open(file)
    graph = dict()
    for line in dataFile:
        edge = line.strip('\n').split('-')
        if not edge[0] in graph:
            graph[edge[0]] = [edge[1]]
        else:
            graph[edge[0]].append(edge[1])
        if edge[0] != "start" and edge[1] != "end":
            if not edge[1] in graph:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])
    return graph

def smallCave(cave):
    if cave.lower() == cave:
        return True
    return False

def findPaths(curNode, path, graph):
    # print("curNode is {}".format(curNode))
    path.append(curNode)
    if curNode == "end":
        return [path.copy()]
    allPaths = []
    for node in graph[curNode]:
        if not (smallCave(node) and node in path):
            tmpPathList = findPaths(node, path.copy(), graph)
            for p in tmpPathList:
                allPaths.append(p)
    return allPaths


def main():
    graph = readFile(sys.argv[1])
    # print(graph)
    # for key in graph:
    #     print("{} is a small cave: {}".format(key, smallCave(key)))
    pathList = findPaths("start", [], graph)
    # print("all paths are")
    # print(pathList)
    print(len(pathList))

main()
