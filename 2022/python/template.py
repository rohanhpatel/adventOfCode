import sys
import os
import math
from dill.source import getsource

def parseFile(f):
    inpFile = open(f, 'r')
    pass

def part1():
    pass

def part2():
    pass

def main():
    if len(sys.argv) < 3:
        print("Not enough arguments")
        exit(1)
    part = int(sys.argv[2])
    if part == 1:
        part1()
    elif part == 2:
        part2()
    else:
        print("Not a valid part")

main()
