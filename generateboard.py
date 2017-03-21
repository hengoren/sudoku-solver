import makecnfclues
import rulesofsudoku
import sys

# textfilename = sys.argv[1]

def get_board_from_file(thefile):
	boardstring = ""
	file = open(thefile, 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		boardstring += line
	newboardstring = ""
	for char in boardstring:
		if char != "\n":
			newboardstring += char
	boardlist = eval(newboardstring)
	return boardlist

# ourboard = get_board_from_file('sampleboard.txt')
# print ourboard

def text_file_to_board(textfilename):
	puzzle = get_board_from_file(textfilename)
	return puzzle



# p cnf 64 144
# p cnf 


# take a text file and get the board from it
# find puzzles from that board
# 	testing the uniqueness of that puzzle
# 		makes a puzzle into a cnf
# 		then actually call the code that runs the cnf and test it for uniqueness  
# 	
