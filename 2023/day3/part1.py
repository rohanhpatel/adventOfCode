import sys

def nearSymbol(row, start, end, mat):
    for i in range(row-1, row+2):
        if i < 0 or i >= len(mat):
            continue
        for j in range(start-1, end+1):
            if j < 0 or j >= len(mat[i]):
                continue
            if mat[i][j] != '.' and not mat[i][j].isdigit():
                return True
    return False

def main():
    f = open(sys.argv[1], "r")
    tot = 0
    mat = list()
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
                if nearSymbol(i, start, end, mat):
                    tot += num
            j += 1
    print(f"The total is {tot}")

if __name__ == "__main__":
    main()