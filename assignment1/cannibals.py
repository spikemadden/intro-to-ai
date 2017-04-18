import sys

class State(object):
	def __init__(self, misRight, canRight, misLeft, canLeft, boat, parent, level):
		self.misRight = misRight
		self.canRight = canRight
		self.misLeft = misLeft
		self.canLeft = canLeft
		self.parent = parent
		self.boat = boat
		self.level = level


	def __repr__(self):
		return "left bank: %s %s right bank: %s %s boat: %s" % (self.misLeft, self.canLeft, self.misRight, self.canRight, self.boat)

	def __eq__(self, other):
		if self.misRight == other.misRight \
		and self.misLeft == other.misLeft \
		and self.canRight == other.canRight \
		and self.canLeft == other.canLeft \
		and self.boat == other.boat:
			return True
		else:
			return False

	def __hash__(self):
		return hash((self.misLeft, self.misRight, self.canLeft, self.canRight, self.boat))

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
			# print(self)

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
		state = State(right_bank[0], right_bank[1], left_bank[0], left_bank[1], 'right', None, 0)
	else:
		state = State(right_bank[0], right_bank[1], left_bank[0], left_bank[1], 'left', None, 0)

	return state

def breadth_first(initial_state, goal_state):
	visited = set()
	fringe = []
	# push first node into queue
	fringe.append(initial_state)
	while(fringe):
		# gets the FIRST element in the fringe
		current_node = fringe.pop(0)
		# check if current node is goal
		if (current_node == goal_state):
			print("We found the goal")
			path = solution(current_node, initial_state)
			return path
		if current_node not in visited:
			visited.add(current_node)

			valid_children = expand(current_node)
			for state in valid_children:
				fringe.append(state)

	return None

def depth_first(initial_state, goal_state):
	visited = set()
	fringe = []
	# push first node into queue
	fringe.append(initial_state)
	while(fringe):
		# gets the LAST element in the fringe
		current_node = fringe.pop()
		# check if current node is goal
		if (current_node == goal_state):
			print("We found the goal")
			path = solution(current_node, initial_state)
			return path

		if current_node not in visited:
			visited.add(current_node)

			valid_children = expand(current_node)
			valid_children = list(reversed(valid_children))
			for state in valid_children:
				fringe.append(state)

	return None

def iterative_deepening(initial_state, goal_state):
	visited = set()
	fringe = []
	limit = 0
	goal_found = 0

	while (1):
		# push first node into queue
		fringe.append(initial_state)
		while(fringe):
			# gets the LAST element in the fringe
			current_node = fringe.pop()
			# check if current node is goal
			if (current_node == goal_state):
				print("We found the goal")
				path = solution(current_node, initial_state)
				return path

			if current_node not in visited:
				visited.add(current_node)

				# if the current level is less than the iterator
				# we want to expand
				if (current_node.level < limit):
					valid_children = expand(current_node)
					valid_children = list(reversed(valid_children))
					for state in valid_children:
						fringe.append(state)

		visited.clear()
		limit = limit + 1
		
def expand(current):
	valid_children = []
	if (current.boat == 'right'):
		# print("expanding w/ boat on right")
		# move one missionary
		child = State(current.misRight - 1, current.canRight, current.misLeft + 1, current.canLeft, 'left', current, current.level + 1)
		if (child.isValid()):
			valid_children.append(child)
		# move two missionaries
		child = State(current.misRight - 2, current.canRight, current.misLeft + 2, current.canLeft, 'left', current, current.level + 1)
		if (child.isValid()):
			valid_children.append(child)
		# move one cannibal
		child = State(current.misRight, current.canRight - 1, current.misLeft, current.canLeft + 1, 'left', current, current.level + 1)
		if (child.isValid()):
			valid_children.append(child)
		# move one cannibal and one missionary
		child = State(current.misRight - 1, current.canRight - 1, current.misLeft + 1, current.canLeft + 1, 'left', current, current.level + 1)
		if (child.isValid()):
			valid_children.append(child)
		# move two cannibals
		child = State(current.misRight, current.canRight - 2, current.misLeft, current.canLeft + 2, 'left', current, current.level + 1)
		if (child.isValid()):
			valid_children.append(child)
	elif (current.boat == 'left'):
		# print("expanding w/ boat on left")
		# move one missionary
		child = State(current.misRight + 1, current.canRight, current.misLeft - 1, current.canLeft, 'right', current, current.level + 1)
		if (child.isValid()):
			valid_children.append(child)
		# move two missionaries
		child = State(current.misRight + 2, current.canRight, current.misLeft - 2, current.canLeft, 'right', current, current.level + 1)
		if (child.isValid()):
			valid_children.append(child)
		# move one cannibal
		child = State(current.misRight, current.canRight + 1, current.misLeft, current.canLeft - 1, 'right', current, current.level + 1)
		if (child.isValid()):
			valid_children.append(child)
		# move one cannibal and one missionary
		child = State(current.misRight + 1, current.canRight + 1, current.misLeft - 1, current.canLeft - 1, 'right', current, current.level + 1)
		if (child.isValid()):
			valid_children.append(child)
		# move two cannibals
		child = State(current.misRight, current.canRight + 2, current.misLeft, current.canLeft - 2, 'right', current, current.level + 1)
		if (child.isValid()):
			valid_children.append(child)

	return valid_children

def solution(finalState, initial):
	currentState = finalState
	path = []
	path.append(finalState)
	while currentState.parent != initial:
		currentState = currentState.parent
		path.insert(0, currentState)

	print("**** Printing Solution ****")
	for step in path:
		print(step)
	return path

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
	output = open(args[4], 'w')

	initial = load_data(starting_state)
	goal = load_data(goal_state)

	validModes = set(["bfs", "dfs", "iddfs", "astar"])
	if mode not in validModes:
		print ("Please specify a valid mode from ", validModes)
		exit

	if mode == "bfs":
		solutionPath = breadth_first(initial, goal)
	elif mode == "dfs":
		solutionPath = depth_first(initial, goal)
	elif mode == 'iddfs':
		solutionPath = iterative_deepening(initial, goal)

	if solutionPath != None:
		for step in solutionPath:
			print(step, file=output)
	else:
		print("No solution was found")

if __name__ == "__main__":
	main(sys.argv)
