import sys

def main():
    f = open(sys.argv[1], "r")
    tot = 0
    for line in f:
        _, rest = line.strip().split(":")
        winning, nums = rest.strip().split("|")
        win_list = winning.strip().split(" ")
        num_list = nums.strip().split(" ")
        while '' in win_list:
            win_list.remove('')
        while '' in num_list:
            num_list.remove('')
        # now for the actual logic
        matches = -1
        for num in num_list:
            if num in win_list:
                matches += 1
        tot += int(2 ** matches)
    print(f"The total is {tot}")
    
if __name__ == "__main__":
    main()