import hashlib 

def count_removal_marks(removal_marks):
  count = 0
  for i in range(len(removal_marks)):
      for j in range(len(removal_marks[i])):
        if removal_marks[i][j] == -1:
          count += 1
  return count

print count_removal_marks([[1, 1, 1, 1], [1, 1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]])