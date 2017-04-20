#!/usr/bin/python


import unique
# import findminimalpuzzles

# print unique.testuniqueness([[0, 0, 0, 0], [0, 0, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]])
# print findminimalpuzzles.create_puzzle_from_board([[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]], 
													# [[1, 1, 1, 1], [1, 1, -1, -1], [1, 0, 0, 0], [0, 0, 0, 0]])

# print findminimalpuzzles.count_neg_ones([[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]])
# print findminimalpuzzles.print_listofallrm([[[0, 0, 0, 0], [0, 0, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]],[[0, 0, 0, 0], [0, 0, 1, 2], [0, 1, 0, 3], [0, 3, 2, 0]]])

unique.make_cnf_file([[0,0,0,0],[0,0,1,2],[0,3,4,0],[0,1,2,0]], 'samplecnf.cnf')