import sys

def load_data(file):
    left_bank = []
    right_bank = []
    first_line = 1

    file = open(file, 'r')

    # loop through each line in the file
    for line in file:
        # tokenize the line
        line = line.split(',')
        # convert the line to numbers and not strings
        line = map(int, line)
        if (first_line):
            left_bank = line[0:3]
            first_line = 0
        else:
            right_bank = line[0:3]

    return left_bank, right_bank

def main(args):
    # Ensure enough arguments are present
    if len(args) != 3:
        print "Incorrect number of command lind arguments provided."
        print "Usage: starting_state goal_state"
        return

    # Save file name
    starting_state = args[1]
    goal_state = args[2]

    left, right = load_data(starting_state)

if __name__ == "__main__":
    main(sys.argv)
