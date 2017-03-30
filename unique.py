import os.path
import re
import sys
import scriptfunctions
import rulesofsudoku
import makecnfclues
import generateboard
import hashlib

def make_cnf_file(puzzle, cnffilename):
	rulesstring = rulesofsudoku.gen_all_rules(2)
	rulesofsudoku.create_cnf_file(cnffilename, rulesstring)
	# thepuzzle = generateboard.get_board_from_file(puzzle)
	givens = makecnfclues.generate_corresponding_vals(puzzle)
	numberofgivens = makecnfclues.get_given_count(puzzle)
	makecnfclues.append_givens_to_cnf(givens, cnffilename)
	makecnfclues.edit_param(numberofgivens, cnffilename)

# make function to make a unique string for a puzzle
# def make_puzzle_string(puzzle):
# 	puzzlestring = ""
#   for i in range(0,len(thelist)):
#     for j in range(0,len(thelist[i])):
#         aval += thelist[i][j]
#         puzzlestring += (str)val
#   return puzzlestring

def puzzle_encoding(puzzle):
	puzzlestring = ''.join(str(elem) for row in puzzle for elem in row)
	return hashlib.md5(puzzlestring).hexdigest()


def testuniqueness(puzzle):
	puzzlename = puzzle_encoding(puzzle)
	cnfin = puzzlename + ".cnf"
	make_cnf_file(puzzle, cnfin)
	threecnf = "threecnf" + cnfin
	output = "output" + cnfin
	scriptfunctions.run_cnf_and_sat(cnfin, threecnf, output)
	if (scriptfunctions.is_satisfiable(output)):
		scriptfunctions.remove_extra_char(output)
		scriptfunctions.modify_cnf(output, cnfin)
		scriptfunctions.run_cnf_and_sat(cnfin, threecnf, output)
		if (scriptfunctions.is_satisfiable(output)):
			print("Puzzle is not unique")
			# pipe output to new file
			return False
		else:
			print("Puzzle is unique")
			# pipe output to a new file
			return True
	else:
		print("This was not a valid board.")

# testuniqueness(cnfin, threecnf, output)

# cnfin = sys.argv[1]
# threecnf = "threecnf" + sys.argv[1]
# output = "output" + sys.argv[1]

# def testuniqueness(cnfin, threecnf, output):
# 	scriptfunctions.run_cnf_and_sat(cnfin, threecnf, output)
# 	if (scriptfunctions.is_satisfiable(output)):
# 		scriptfunctions.remove_extra_char(output)
# 		scriptfunctions.modify_cnf(output, cnfin)
# 		scriptfunctions.run_cnf_and_sat(cnfin, threecnf, output)
# 		if (scriptfunctions.is_satisfiable(output)):
# 			print("Puzzle is not unique")
# 			# pipe output to new file
# 			return False
# 		else:
# 			print("Puzzle is unique")
# 			# pipe output to a new file
# 			return True
# 	else:
# 		print("This was not a valid board.")

# testuniqueness(cnfin, threecnf, output)