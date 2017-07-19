#!/usr/bin/python

import unique
import copy

### Input: A valid Suokdu board and a mask, "removal_marks", indicating where a puzzle does not have entries,
###        or has unremovable entries. 
###        An entry in removal_marks is either a
### 									1: indicating a cell that has been removed
###                                    -1: indicating an unremovable cell
###                                     0: otherwise
### Output: A list containing the mumber of minimal puzzles for each possible number of unremovable entries


board = [[1, 2, 3, 4],
		  [3, 4, 1, 2],
		  [2, 1, 4, 3],
		  [4, 3, 2, 1]]

counterlist = [0 for x in range(17)]

removal_marks_dict = {}

def gen_puzzles(board, removal_marks = [[0 for j in range(4)] for i in range(4)]):
	found_removable = False
	duplicate_puzzle = False

	for i in range(0, 16):
		
		xcoor = i / 4
		ycoor = i % 4
		# print "index: (" + str(xcoor) + ", " + str(ycoor) +")"
		temp_removal_marks = copy.deepcopy(removal_marks)
		# print_all_rm()

		if (removal_marks[xcoor][ycoor] == 0):
			temp_removal_marks[xcoor][ycoor] = 1
			if not removal_marks_dict.has_key(stringify_matrix(temp_removal_marks)):
			
				puzzle = create_puzzle_from_board(board, temp_removal_marks)

				boolunique = unique.testuniqueness(puzzle)

				if boolunique:
					found_removable = True
					if not removal_marks_dict.has_key(stringify_matrix(temp_removal_marks)):
						print "Recursing..."
						print temp_removal_marks
						finished_bool = not ('0' in stringify_matrix(temp_removal_marks))
						removal_marks_dict[stringify_matrix(temp_removal_marks)] = finished_bool
						print gen_puzzles(board, temp_removal_marks)
				else:
					removal_marks[xcoor][ycoor] = -1
			else:
				duplicate_puzzle = True


	if not found_removable and not duplicate_puzzle:
		finished_bool = '0' in stringify_matrix(temp_removal_marks)
		removal_marks_dict[stringify_matrix] = finished_bool
		return "Removal marks: ", removal_marks
		index = count_neg_ones(removal_marks)
		counterlist[index] += 1
		# return counterlist






### Helper functions

def count_neg_ones(removal_marks):
	count = 0
	for i in range(len(removal_marks)):
		for j in range(len(removal_marks[i])):
			if removal_marks[i][j] == -1:
				count += 1
	return count

def create_puzzle_from_board(board, removal_marks):
	boardcopy = copy.deepcopy(board)
	for i in range(len(removal_marks)):
		for j in range(len(removal_marks[i])):
			if removal_marks[i][j] == 1:
				boardcopy[i][j] = 0
	return boardcopy

def print_all_rm():
	print removal_marks_dict.items()


def stringify_matrix(removal_marks):
	outstring = ""
	for x in range(len(removal_marks)):
		for y in range(len(removal_marks[x])):
			outstring += str(removal_marks[x][y])
	return outstring

print gen_puzzles(board, removal_marks = [[0 for j in range(4)] for i in range(4)])


