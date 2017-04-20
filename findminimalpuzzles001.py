# findminimalpuzzles001.py
#!/usr/bin/python

import unique
import copy

# input: a valid Sudoku board and "removal marks" indicating where a puzzle does not have entries, or has unremovable entries
# 	removal_marks is 1 if cell has been removed, -1 if it's unremovable, 0 otherwise
# output: prints a list of puzzles for that board
board = [[1, 2, 3, 4], [3, 4, 1, 2], [2, 3, 4, 1], [4, 1, 2, 3]]

counterlist = [0 for j in range(17)]

listofallrm = []

def gen_puzzles(board,removal_marks = [[-1,-1,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]):
  found_removable = False
  duplicate_puzzle = False
  
  for i in range(0,16):
    xcoor = i/4
    ycoor = i % 4
    temp_removal_marks = copy.deepcopy(removal_marks)
    # print "Temp_removal_marks: ", temp_removal_marks, xcoor, ycoor
    if temp_removal_marks not in listofallrm:
      if (removal_marks[xcoor][ycoor] == 0):
        temp_removal_marks[xcoor][ycoor] = 1 # cell i is to be removed
        # return True if puzzle obtained from board by deleting cells where removal_marks is nonzero is uniquely solvable, false if not
        puzzle = create_puzzle_from_board(board, temp_removal_marks)
        boolunique = unique.testuniqueness(puzzle)
        if boolunique:
          found_removable = True
          # recursively dig into sub-puzzle
          print gen_puzzles(board,temp_removal_marks)
        else:
          # i is unremovable
          removal_marks[xcoor][ycoor] = -1
    else:
      duplicate_puzzle = True
  
  if not found_removable and not duplicate_puzzle:
    listofallrm.append(removal_marks)
    # toprint = print_listofallrm(listofallrm)
    # return "Removal marks: ", removal_marks
    index = count_neg_ones(removal_marks)
    counterlist[index] += 1
    return counterlist # this puzzle is now minimal




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

def print_listofallrm(listofallrm):
    outstring = "List of all RM: \n"
    for rm in listofallrm:
      outstring += "\t"
      outstring += str(rm)
      outstring += "\n"
    return outstring



print gen_puzzles(board,removal_marks = [[0 for j in range(4)] for i in range(4)])