import sys

class State(object):
	def __init__(self, misRight, canRight, misLeft, canLeft, boat):
		self.misRight = misRight
		self.canRight = canRight
		self.misLeft = misLeft
		self.canLeft = canLeft
		self.boat = boat

	def __repr__(self):
		return "left bank: %s %s right bank: %s %s boat: %s" % (self.misLeft, self.canLeft, self.misRight, self.canRight, self.boat)

	# Checks for a valid state.
	# If missionaries are present on a bank, then there cannot be more missionaries
	def isValid(self):
		valid = False
		# if there are missionaries on the right, and there are more cannibals
		if (self.misRight > 0) and (self.misRight < self.canRight):
			valid = False
		# if there are missionaries on the left, and there are more cannibals
		elif (self.misLeft > 0) and (self.misLeft < self.canLeft):
			valid = False
		# if any of the values are negative
		elif self.misLeft < 0 or self.canLeft < 0 or self.misRight < 0 or self.canRight < 0:
			valid = False
		else:
			valid = True
			print(self)


		return valid




def load_data(file):
	left_bank = []
	right_bank = []
	first_line = 1

	file = open(file, 'r')

	# loop through each line in the file
	for line in file:
		# tokenize the line
		line = line.replace("\n", "").split(',')
		# convert the line to numbers and not strings
		# //line = map(int, line)
		if (first_line):
			left_bank = list(map(int,line[0:3]))
			first_line = 0
		else:
			right_bank = list(map(int,line[0:3]))

	# check boat position and create state
	if (right_bank[2] == 1):
		state = State(right_bank[0], right_bank[1], left_bank[0], left_bank[1], 'right')
	else:
		state = State(right_bank[0], right_bank[1], left_bank[0], left_bank[1], 'left')

	return state

def breadth_first(initial_state, goal_state):
	visited = set()
	fringe = []
	# push first node into queue
	fringe.append(initial_state)
	while(fringe):
		# gets the first element in the fringe
		current_node = fringe.pop(0)
		# check if current node is goal
		if (current_node == goal_state):
			print("We found the goal")
			return
		if (current_node not in visited):
			print("adding to visited")
			visited.add(current_node)
			#FIX THIS BOI
			valid_children = expand(current_node)
			for state in valid_children:
				fringe.append(state)

def expand(current):
	valid_children = []
	if (current.boat == 'right'):
		print("expanding w/ boat on right")
		# move one missionary
		child = State(current.misRight - 1, current.canRight, current.misLeft + 1, current.canLeft, 'left', current_node)
		if (child.isValid()):
			valid_children.append(child)
		# move two missionaries
		child = State(current.misRight - 2, current.canRight, current.misLeft + 2, current.canLeft, 'left', current_node)
		if (child.isValid()):
			valid_children.append(child)
		# move one cannibal
		child = State(current.misRight, current.canRight - 1, current.misLeft, current.canLeft + 1, 'left', current_node)
		if (child.isValid()):
			valid_children.append(child)
		# move one cannibal and one missionary
		child = State(current.misRight - 1, current.canRight - 1, current.misLeft + 1, current.canLeft + 1, 'left', current_node)
		if (child.isValid()):
			valid_children.append(child)
		# move two cannibals
		child = State(current.misRight, current.canRight - 2, current.misLeft, current.canLeft + 2, 'left', current_node)
		if (child.isValid()):
			valid_children.append(child)
	elif (current.boat == 'left'):
		print("expanding w/ boat on left")
		# move one missionary
		child = State(current.misRight + 1, current.canRight, current.misLeft - 1, current.canLeft, 'right', current_node)
		if (child.isValid()):
			valid_children.append(child)
		# move two missionaries
		child = State(current.misRight + 2, current.canRight, current.misLeft - 2, current.canLeft, 'right', current_node)
		if (child.isValid()):
			valid_children.append(child)
		# move one cannibal
		child = State(current.misRight, current.canRight + 1, current.misLeft, current.canLeft - 1, 'right', current_node)
		if (child.isValid()):
			valid_children.append(child)
		# move one cannibal and one missionary
		child = State(current.misRight + 1, current.canRight + 1, current.misLeft - 1, current.canLeft - 1, 'right', current_node)
		if (child.isValid()):
			valid_children.append(child)
		# move two cannibals
		child = State(current.misRight, current.canRight + 2, current.misLeft, current.canLeft - 2, 'right', current_node)
		if (child.isValid()):
			valid_children.append(child)

	# print(valid_children)
	return valid_children

def main(args):
	print (len(args))
	# Ensure enough arguments are present
	if len(args) != 5:
		print ("Incorrect number of command lind arguments provided.")
		print ("Usage: starting_state goal_state mode output_file")
		return

	# Save file name
	starting_state = args[1]
	goal_state = args[2]
	mode = args[3]
	output = args[4]

	initial = load_data(starting_state)
	goal = load_data(goal_state)

	validModes = set(["bfs", "dfs", "iddfs", "astar"])
	if mode not in validModes:
		print ("Please specify a valid mode from ", validModes)
		exit

	if mode == "bfs":
		breadth_first(initial, goal)
	# print(left)
	# print(right)

if __name__ == "__main__":
	main(sys.argv)
