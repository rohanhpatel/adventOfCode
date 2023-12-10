import sys

def main():
    f = open(sys.argv[1], "r")
    cur_seeds = []
    lines = f.readlines()
    tmp_dict = dict()
    for l in range(len(lines)):
        cur_line = lines[l].strip()
        if l == 0:
            tmp_seeds = cur_line[7:].split(" ")
            cur_seeds = []
            for s in tmp_seeds:
                cur_seeds.append(int(s))
            print(f'starting seeds: {cur_seeds}')
        elif cur_line == '':
            if tmp_dict != dict():
                print(f"dict: {tmp_dict}")
                for i in range(len(cur_seeds)):
                    seed = cur_seeds[i]
                    for key in tmp_dict:
                        if seed >= key[0] and seed < key[1]:
                            cur_seeds[i] = seed + tmp_dict[key]
                            break
                print(f'seeds: {cur_seeds}')
        elif cur_line[-1] == ':':
            tmp_dict = dict()
        else:
            values = cur_line.split(" ")
            start_val = int(values[1])
            diff = int(values[0]) - int(values[1])
            rnge = int(values[2])
            seed_list = (start_val, start_val + rnge)
            tmp_dict[seed_list] = diff
    # do last conversion since we run out of lines
    for i in range(len(cur_seeds)):
        seed = cur_seeds[i]
        for key in tmp_dict:
            if seed >= key[0] and seed < key[1]:
                cur_seeds[i] = seed + tmp_dict[key]
                break
    print(f'final seeds: {cur_seeds}')
    print(f"The smallest location is {min(cur_seeds)}")

if __name__ == "__main__":

    main()