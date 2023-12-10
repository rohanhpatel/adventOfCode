import sys

def main():
    f = open(sys.argv[1], "r")
    tot_power = 0
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
        cur_power = 1
        for key in cur_max:
            cur_power *= cur_max[key]
        tot_power += cur_power
    print(f"The total is {tot_power}")

if __name__ == "__main__":
    main()