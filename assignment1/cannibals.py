import sys

class State(object):
	def __init__(self, misRight, canRight, misLeft, canLeft, boat):
		self.misRight = misRight
		self.canRight = canRight
		self.misLeft = misLeft
		self.canLeft = canLeft
		self.boat = boat

	# Checks for a valid state.
	# If missionaries are present on a bank, then there cannot be more missionaries
	def isValid():
		valid = False
		# if there are missionaries on the right, and there are more cannibals
		if (self.misRight > 0) and (self.misRight < self.canRight):
			valid = False
		# if there are missionaries on the left, and there are more cannibals
		elif (self.misleft > 0) and (self.misLeft < self.canLeft):
			valid = False
		# if any of the values are negative
		elif self.misLeft < 0 or self.canLeft < 0 or slef.misRight < 0 or self.canRight < 0:
			valid = False
		else
			valid = True


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

	return left_bank, right_bank

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

	left, right = load_data(starting_state)

	validModes = set(["bfs", "dfs", "iddfs", "astar"])
	if mode not in validModes:
		print ("Please specify a valid mode from ", validModes)
		exit

	print(left)
	print(right)

if __name__ == "__main__":
	main(sys.argv)

def breadth_first(initial_left, initial_right, goal):
	fringe = []
	initial = State(initial_right[0], initial_right[1], initial_left[0], initial_left[1], 'right')

	while(fringe):
