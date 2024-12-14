import sys
import re

def parse():
    inp = open(sys.argv[1], "r")
    lines = []
    for line in inp:
        lines.append(line.strip())

    return lines

def part1():
    lines = parse()
    pattern = r"mul\(\d+,\d+\)"
    total = 0
    for line in lines:
        matches = re.findall(pattern, line)
        for match in matches:
            one, two = [int(x) for x in match[4:-1].split(",")]
            total += one * two

    print(f"TOTAL: {total}") 

def part2():
    lines = parse()
    do = r"do\(\)"
    dont = r"don't\(\)"
    enabled = True
    mul = r"mul\(\d+,\d+\)"
    total = 0
    for line in lines:
        doSplit = re.split(do, line)
        fullSplit = [re.split(dont, x) for x in doSplit]
        for i in range(len(fullSplit)):
            if i == 0 and enabled == False:
                enabled = True
                continue
            matches = re.findall(mul, fullSplit[i][0])
            for match in matches:
                one, two = [int(x) for x in match[4:-1].split(",")]
                total += one * two
            if i == len(fullSplit) - 1 and len(fullSplit[i]) > 1:
                enabled = False
            else:
                enabled = True

    print(f"TOTAL WITH DO AND DONT: {total}")


if __name__ == "__main__":
    if sys.argv[2] == "1":
        part1()
    elif sys.argv[2] == "2":
        part2()
