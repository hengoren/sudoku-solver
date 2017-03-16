# input: a valid Sudoku board and "removal marks" indicating where a puzzle does not have entries, or has unremovable entries
# 	removal_marks is 1 if cell has been removed, -1 if it's unremovable, 0 otherwise
# output: prints a list of puzzles for that board
def gen_puzzles(board,removal_marks = [0 for i in range(16)]):
  modified_cells = [i if removal_marks[i] != 0 for i in range(16)]
  recent_modification = max(modified_cells,-1)
  found_removable = False
  for i in range(recent_modification+1,16):
    temp_removal_marks = copy(removal_marks)
    temp_removal_marks[i] = 1 # cell i is to be removed
    # return True if puzzle obtained from board by deleting cells where removal_marks is nonzero is uniquely solvable, false if not
    unique = test_for_uniqueness(board,temp_removal_marks)
    if unique:
      found_removable = True
      # recursively dig into sub-puzzle
      print gen_puzzles(board,temp_removal_marks)
    else:
      # i is unremovable
      removal_marks[i] = -1
  if not found_removable:
    return removal_marks # this puzzle is now minimal


