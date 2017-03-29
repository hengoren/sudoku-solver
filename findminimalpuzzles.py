import unique
import copy

# input: a valid Sudoku board and "removal marks" indicating where a puzzle does not have entries, or has unremovable entries
# 	removal_marks is 1 if cell has been removed, -1 if it's unremovable, 0 otherwise
# output: prints a list of puzzles for that board
board = [[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]]

def gen_puzzles(board,removal_marks = [[0 for j in range(4)] for i in range(4)]):
  # print("Calling gen_puzzles")
  print "Board: ", board
  print "Removal Marks: ", removal_marks
  modified_cells = []
  # modified_cells = [i if removal_marks[i] != 0 for i in range(16)]
  # recent_modification = max(modified_cells,-1)
  # found_removable = False
  for i in range(16):
    xcoor = i/4
    ycoor = i % 4
    if removal_marks[xcoor][ycoor] != 0:
      modified_cells.append(i)
  print("Modified Cells: ", modified_cells)
  if not modified_cells:
    recent_modification = -1
  else:
    recent_modification = max(modified_cells)
  found_removable = False
  for i in range(recent_modification+1,16):
    xcoor = i/4
    ycoor = i % 4
    temp_removal_marks = copy.deepcopy(removal_marks)
    temp_removal_marks[xcoor][ycoor] = 1 # cell i is to be removed
    # return True if puzzle obtained from board by deleting cells where removal_marks is nonzero is uniquely solvable, false if not
    puzzle = create_puzzle_from_board(board, temp_removal_marks)
    boolunique = unique.testuniqueness(puzzle)
    if boolunique:
      # print("Puzzle was found to be unique")
      found_removable = True
      # recursively dig into sub-puzzle
      print gen_puzzles(board,temp_removal_marks)
      # This line ^ was causing problems because it was formerly print

    else:
      # i is unremovable
      removal_marks[xcoor][ycoor] = -1
  if not found_removable:
    return removal_marks # this puzzle is now minimal


def create_puzzle_from_board(board, removal_marks):
  for i in range(len(removal_marks)):
    for j in range(len(removal_marks[i])):
      if removal_marks[i][j] == 1:
        board[i][j] = 0
  return board


print gen_puzzles(board,removal_marks = [[0 for j in range(4)] for i in range(4)])


