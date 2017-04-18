import sys

class State(object):
	def __init__(self, misRight, canRight, misLeft, canLeft, boat):
		self.misRight = misRight
		self.canRight = canRight
		self.misLeft = misLeft
		self.canLeft = canLeft
		self.boat = boat

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

	initial_state = load_data(starting_state)
	goal_state = load_data(goal_state)

	validModes = set(["bfs", "dfs", "iddfs", "astar"])
	if mode not in validModes:
		print ("Please specify a valid mode from ", validModes)
		exit

	print(left)
	print(right)

if __name__ == "__main__":
	main(sys.argv)

def breadth_first(initial_state, goal_state):
	visited = set()
	fringe = []
	# push first node into queue
	fringe.append(initial_state)
	while(fringe):
		# gets the first element in the fringe
		current_node = fringe.remove()
		# check if current node is goal
		if (current_node == goal):
			return
		if (current_node not in visited):
			visited.add(current_node)
			#FIX THIS BOI
			valid_children = expand(current_node)

def expand(current):
	valid_children = []
	if (current.boat == 'right'):
		# move one missionary
		child = State(current.misRight - 1, current.canRight, current.misLeft + 1, current.canLeft, 'left')
		if (child.isValid()):
			valid_children.append(child)
		# move two missionaries
		child = State(current.misRight, current.canRight - 2, current.misLeft, current.canLeft + 2, 'left')
		if (child.isValid()):
			valid_children.append(child)
		# move one cannibal
		child = State(current.misRight, current.canRight - 1, current.misLeft, current.canLeft + 1, 'left')
		if (child.isValid()):
			valid_children.append(child)
		# move one cannibal and one missionary
		child = State(current.misRight - 1, current.canRight - 1, current.misLeft + 1, current.canLeft + 1, 'left')
		if (child.isValid()):
			valid_children.append(child)
		# move two cannibals
		child = State(current.misRight, current.canRight - 2, current.misLeft, current.canLeft + 2, 'left')
		if (child.isValid()):
			valid_children.append(child)
	elif (current.boat == 'left'):
		# move one missionary
		child = State(current.misRight + 1, current.canRight, current.misLeft - 1, current.canLeft, 'right')
		if (child.isValid()):
			valid_children.append(child)
		# move two missionaries
		child = State(current.misRight, current.canRight + 2, current.misLeft, current.canLeft - 2, 'right')
		if (child.isValid()):
			valid_children.append(child)
		# move one cannibal
		child = State(current.misRight, current.canRight + 1, current.misLeft, current.canLeft - 1, 'right')
		if (child.isValid()):
			valid_children.append(child)
		# move one cannibal and one missionary
		child = State(current.misRight + 1, current.canRight + 1, current.misLeft - 1, current.canLeft - 1, 'right')
		if (child.isValid()):
			valid_children.append(child)
		# move two cannibals
		child = State(current.misRight, current.canRight + 2, current.misLeft, current.canLeft - 2, 'right')
		if (child.isValid()):
			valid_children.append(child)

	return valid_children
