import sys
import csv
import math

class lanternFish:
    def __init__(self, t):
        self.timer = t
    def tick(self):
        if self.timer != 0:
            self.timer -= 1
            return False
        else:
            self.timer = 6
            return True

datafile = open(sys.argv[1])
fish = []
onlyLine = ""
for line in datafile:
    onlyLine = line
string = onlyLine.split(",")
for s in string:
    fish.append(lanternFish(int(s)))

num_days = int(sys.argv[2])
for _ in range(num_days):
    cur_len = len(fish)
    for i in range(cur_len):
        create = fish[i].tick()
        if create:
            fish.append(lanternFish(8))

print(len(fish))
