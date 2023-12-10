import sys

def main():
    f = open(sys.argv[1], "r")
    tot = 0
    copies = dict()
    for line in f:
        card, rest = line.strip().split(":")
        card_num = int(card[5:])
        if card_num not in copies:
            copies[card_num] = 1
        else:
            copies[card_num] += 1
        winning, nums = rest.strip().split("|")
        win_list = winning.strip().split(" ")
        num_list = nums.strip().split(" ")
        while '' in win_list:
            win_list.remove('')
        while '' in num_list:
            num_list.remove('')
        # now for the actual logic
        matches = 0
        for num in num_list:
            if num in win_list:
                matches += 1
        for i in range(1, matches+1):
            cur_card = card_num + i
            if cur_card not in copies:
                copies[cur_card] = copies[card_num]
            else:
                copies[cur_card] += copies[card_num]
    for key in copies:
        tot += copies[key]
    print(f"The total is {tot}")
    
if __name__ == "__main__":
    main()