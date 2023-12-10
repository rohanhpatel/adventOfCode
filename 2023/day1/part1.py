import sys

def main():
    f = open(sys.argv[1], "r")
    tot = 0
    for line in f:
        actLine = line.strip()
        i = 0
        j = len(actLine) - 1
        digits = ["o", "o"]
        while True:
            if not actLine[i].isdigit():
                i += 1
            if actLine[i].isdigit():
                digits[0] = actLine[i]
            if not actLine[j].isdigit():
                j -= 1
            if actLine[j].isdigit():
                digits[1] = actLine[j]
            if actLine[j].isdigit() and actLine[i].isdigit():
                break
        tot += int("".join(digits))
    print(f"The total is {tot}")

if __name__ == "__main__":
    main()