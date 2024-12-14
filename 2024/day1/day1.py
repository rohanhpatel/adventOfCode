import os
import sys

def parse():
    inp = open(sys.argv[1], "r")
    list1 = []
    list2 = []
    for line in inp:
        x, y = line.split() 
        list1.append(int(x))
        list2.append(int(y))

    list1.sort()
    list2.sort()

    return (list1, list2)

def part1():
    list1, list2 = parse()
    dist = 0
    for i in range(len(list1)):
        dist += abs(list1[i] - list2[i])

    print(f"DISTANCE: {dist}") 

def part2():
    list1, list2 = parse()
    sim = 0
    for elem in list1:
        sim += elem * list2.count(elem)
    
    print(f"SIMILARITY: {sim}")

if __name__ == "__main__":
    if sys.argv[2] == "1":
        part1()
    elif sys.argv[2] == "2":
        part2()
