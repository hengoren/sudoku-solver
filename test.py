import unique
import findminimalpuzzles

# print unique.testuniqueness([[0, 0, 0, 0], [0, 0, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]])
# print findminimalpuzzles.create_puzzle_from_board([[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]], 
													# [[1, 1, 1, 1], [1, 1, -1, -1], [1, 0, 0, 0], [0, 0, 0, 0]])

print findminimalpuzzles.count_neg_ones([[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]])