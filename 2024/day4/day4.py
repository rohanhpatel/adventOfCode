import sys

def parse():
    inp = open(sys.argv[1], "r")
    table = []
    for line in inp:
        table.append(line.strip())

    return table

def part1():
    table = parse()
    xmas = 0
    # search forward and backward
    for line in table:
        xmas += line.count("XMAS")
        xmas += line.count("SAMX")
    # search up and down and diagonals
    for i in range(len(table) - 3): 
        for j in range(len(table[i])):
            if table[i][j] == "S" or table[i][j] == "X":
                word = ""
                for k in range(4):
                    word += table[i+k][j]
                if word == "SAMX" or word == "XMAS":
                    xmas += 1
                if j + 3 < len(table[i]):
                    word = ""
                    for k in range(4):
                        word += table[i+k][j+k]
                    if word == "SAMX" or word == "XMAS":
                        xmas += 1
                if j >= 3:
                    word = ""
                    for k in range(4):
                        word += table[i+k][j-k]
                    if word == "SAMX" or word == "XMAS":
                        xmas += 1

    print(f"NUMBER OF XMAS FOUND: {xmas}")


def part2():
    table = parse()
    xmas = 0
    for i in range(1, len(table) - 1):
        for j in range(1, len(table[i]) - 1):
            if table[i][j] == "A":
                # form words and check
                word1 = table[i-1][j-1] + table[i][j] + table[i+1][j+1]
                word2 = table[i-1][j+1] + table[i][j] + table[i+1][j-1]
                if (word1 == "SAM" or word1 == "MAS") and (word2 == "SAM" or word2 == "MAS"):
                    xmas += 1

    print(f"NUMBER OF X-MASs FOUND: {xmas}")

if __name__ == "__main__":
    if sys.argv[2] == "1":
        part1()
    elif sys.argv[2] == "2":
        part2()
