import sys

def main():
    f = open(sys.argv[1], "r")
    tot_id = 0
    max_color = {"red": 12, "green": 13, "blue": 14}
    for line in f:
        line_arr = line.split(":")
        id = int(line_arr[0][5:])
        rest = line_arr[1].strip()
        rounds = rest.split(";")
        cur_max = {"red": -1, "green": -1, "blue": -1}
        for r in rounds:
            shown = r.split(",")
            for clrAmt in shown:
                actClrAmt = clrAmt.strip()
                amt, clr = actClrAmt.split(" ")
                if int(amt) > cur_max[clr]:
                    cur_max[clr] = int(amt)
        satisfies = True
        for key in max_color:
            if cur_max[key] > max_color[key]:
                satisfies = False
                break
        if satisfies:
            tot_id += id
    print(f"The total is {tot_id}")

if __name__ == "__main__":
    main()