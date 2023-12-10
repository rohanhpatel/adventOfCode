import sys

def isValidDigit(s, ind, forward=True):
    digitList = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for i in range(3, 6):
        start = ind
        end = ind + i
        diff = 0
        if not forward:
            diff = i - 1
        substring = s[start-diff:end-diff]
        if substring in digitList:
            return digitList[substring]
    if s[ind].isdigit():
        return s[ind]
    else:
        return None

def main():
    f = open(sys.argv[1], "r")
    tot = 0
    for line in f:
        actLine = line.strip()
        i = 0
        j = len(actLine) - 1
        digits = ["o", "o"]
        while True:
            i_res = isValidDigit(actLine, i, True)
            j_res = isValidDigit(actLine, j, False)
            if i_res != None:
                digits[0] = i_res
            else:
                i += 1                
            if j_res != None:
                digits[1] = j_res
            else:
                j -= 1 
            if i_res != None and j_res != None:
                break
        tot += int("".join(digits))
    print(f"The total is {tot}")

if __name__ == "__main__":
    main()