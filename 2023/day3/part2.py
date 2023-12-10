import sys

def nearGear(row, start, end, mat):
    for i in range(row-1, row+2):
        if i < 0 or i >= len(mat):
            continue
        for j in range(start-1, end+1):
            if j < 0 or j >= len(mat[i]):
                continue
            if mat[i][j] == "*":
                return (i, j)
    return None

def main():
    f = open(sys.argv[1], "r")
    mat = list()
    gearDict = dict()
    for line in f:
        mat.append(line.strip())
    for i in range(len(mat)):
        j = 0
        start = -1
        end = -1
        while j < len(mat[i]):
            if mat[i][j].isdigit():
                start = j
                j += 1
                while j < len(mat[i]) and mat[i][j].isdigit():
                    j += 1
                end = j
                num = int(mat[i][start:end])
                coords = nearGear(i, start, end, mat)
                if coords != None:
                    if coords in gearDict:
                        gearDict[coords].append(num)
                    else:
                        gearDict[coords] = [num]
            j += 1
    totGearRatio = 0
    for key in gearDict:
        if len(gearDict[key]) == 2:
            totGearRatio += gearDict[key][0] * gearDict[key][1]
    print(f"The total is {totGearRatio}")

if __name__ == "__main__":
    main()