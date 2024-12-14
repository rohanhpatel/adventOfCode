import sys

def parse():
    inp = open(sys.argv[1], "r")
    reports = []
    for line in inp:
        reports.append([int(x) for x in line.split()])

    return reports

def part1():
    reports = parse()
    safe = 0
    for rep in reports:
        inc = 0
        if rep[1] > rep[0]:
            inc = 1
        if rep[1] < rep[0]:
            inc = -1
        if inc == 0:
            continue
        notSafe = False
        for i in range(len(rep) - 1):
            if inc == 1 and rep[i] > rep[i+1]:
                notSafe = True
            if inc == -1 and rep[i] < rep[i+1]:
                notSafe = True
            if abs(rep[i] - rep[i+1]) < 1 or abs(rep[i] - rep[i+1]) > 3:
                notSafe = True
            if notSafe:
                break
        if not notSafe:
            safe += 1

    print(f"SAFE REPORTS: {safe}")

def part2():
    reports = parse()
    safe = 0
    for rep in reports:
        for j in range(len(rep)):
            tmpRep = rep.copy()
            del tmpRep[j]
            inc = 0
            if tmpRep[1] > tmpRep[0]:
                inc = 1
            if tmpRep[1] < tmpRep[0]:
                inc = -1
            if inc == 0:
                continue
            notSafe = False
            for i in range(len(tmpRep) - 1):
                if inc == 1 and tmpRep[i] > tmpRep[i+1]:
                    notSafe = True
                if inc == -1 and tmpRep[i] < tmpRep[i+1]:
                    notSafe = True
                if abs(tmpRep[i] - tmpRep[i+1]) < 1 or abs(tmpRep[i] - tmpRep[i+1]) > 3:
                    notSafe = True
                if notSafe:
                    break
            if not notSafe:
                safe += 1
                break
    
    print(f"SAFE REPORTS WITH PROBLEM DAMP: {safe}")

if __name__ == "__main__":
    if sys.argv[2] == "1":
        part1()
    elif sys.argv[2] == "2":
        part2()
