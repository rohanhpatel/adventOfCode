import sys

direc = [0, 0]
labMap = Map()

class MapTile:
	def __init__(self, val):
		self.val = val
		self.visited = False
		self.guard = False

	def visit(self):
		if self.val == "#":
			return False
		else:
			self.visited = True
			self.guard = True
			return True

	def leave(self):
		if self.guard:
			self.guard = False
			return True
		else:
			return False

class Map:
	def __init__(self, lines):
		self.map = []
		self.direc = [0, 0]
		for line in lines:
			curLine = []
			for c in line:
				if c != "." and c != "#":
					if c == "^":
						self.direc = [-1, 0]
					elif c == ">":
						self.direc == [0, 1]
					elif c == "v":
						self.direc == [1, 0]
					elif c == "<":
						self.direc == [0, -1]
					startTile = MapTile(c)
					startTile.visit()
					curLine.append(startTile)
				else:
					curLine.append(MapTile(c))
	
	def nextDir(self):
		if self.direc[0] == 0:
			self.direc = [self.direc[1], 0]
		elif self.direc[1] == 0:
			self.direc = [0, -self.direc[0]]


def parse():
	file = open(sys.argv[1], "r")
	lines = []
	global labMap
	for line in file:
		lines.append(line.strip())
	labMap = Map(lines)


def part1():
	pass

def part2():
	pass

if __name__ == "__main__":
	if sys.argv[2] == "1":
		part1()
	elif sys.argv[2] == "2":
		part2()
