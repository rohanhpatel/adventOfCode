import sys
from functools import cmp_to_key

updates = []
rules = dict()

def parse():
	file = open(sys.argv[1], "r")
	global rules
	global updates
	for line in file:
		if "|" in line:	
			key, val = [int(x) for x in line.strip().split("|")]
			if key not in rules:
				rules[key] = [val]
			else:
				rules[key].append(val)
		elif "," in line:
			updates.append([int(x) for x in line.strip().split(",")])			

def part1():
	parse()
	middleTotal = 0
	for up in updates:
		goodUpdate = True
		for i in range(len(up)):
			if i == 0:
				continue
			elif up[i] in rules:
				checkArr = up[:i]
				if len(set(rules[up[i]]).intersection(set(checkArr))) > 0:
					goodUpdate = False
					break
		if goodUpdate:
			middleTotal += up[int(len(up)/2)]

	print(f"TOTAL OF MIDDLES: {middleTotal}")
	

def update_comp(x, y):
	if x in rules and y in rules[x]:
		return -1
	elif y in rules and x in rules[y]:
		return 1
	return 0

def part2():
	parse()
	middleTotal = 0	
	for up in updates:
		sorted_up = sorted(up, key=cmp_to_key(update_comp))
		if sorted_up != up:
			middleTotal += sorted_up[int(len(sorted_up)/2)]

	print(f"TOTAL OF INCORRECT MIDDLES: {middleTotal}")

if __name__ == "__main__":
	if sys.argv[2] == "1":
		part1()
	elif sys.argv[2] == "2":
		part2()
