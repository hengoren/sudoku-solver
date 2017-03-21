README

The cnftools-master directory contains the script (2kcnf) to 3cnf .cnf files.

The lingeling-bbc-9230380-160707-druplig-009 directory contains the druplig package of lingeling to provide unsat certificates.

The treengeling-bbc-sc2016 directory contains the sat-solver that won first place at the 2016 SAT Solver Competition.

findminimalpuzzles.py is the script that was drafted with Dr. Cooper to find the minimal puzzles of a given board.

generateboard.py is the script that contains the functions to return a board (a list of lists) from a given textfile representation of the board.

rulesofsudoku.py is the script that generates the cnf propositions that denote the rules of Sudoku for a given order of a board. For example, it will generate the propositions that are similar to English statements of the rules of Sudoku such as: "If there is a 1 in the cell in the first row and first column, then there cannot be a 1 in any other cell in the first row and there cannot be a 1 in any other cell in the first column".

makecnfclues.py is the script that will take a puzzle and add the propositions it contains to the cnf file. For example, if there is a 1 in the cell in the first column and the first row, it will generate the corresponding value for the literal and specify a proposition that requires a 1 be in the cell in the first column and the first row.

unique.py is the scrip that tests the uniqueness of a given puzzle. A puzzle is unique if it can satisfied in one and only one way. This script also contains the function that generates a cnf file for a given puzzle.

scriptfunctions.py is the script that contains the functions that the unique script calls upon. These functions include functions that call the cnf and sat solver (run_cnf_and_sat), determine if a puzzle is satisfiable (is_satisfiable), remove extra characters from the output (remove_extra_char), identifies the given clues in the cnf (identify_clues), generates the actual solution, which is the satisifiabilty assignment for the puzzle without the clues (gen_alt_sol), negate the actual solution (mult_list_neg), edits the parameters of the cnf file (edit_param),  appends the negated solution to the cnf to see if there is another solution (append_sol_cnf), and the function that wraps all of these functions together (modify_cnf).

sampleboard.txt outlines the format for boards/puzzles to be written out as text files. It is one of the two boards for the 4x4 puzzles.