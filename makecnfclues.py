#!/usr/bin/python


# def get_board_from_file(thefile):
# 	boardlist = [[]]
# 	file = open(thefile, 'r')
# 	lines = file.readlines()
# 	file.close()
# 	i = 0
# 	for line in lines:	
# 		for num in line:
# 			if num != "\n":
# 				boardlist[i].append(num)
# 			else:
# 				boardlist.append([])
# 				i = i + 1
# 	return boardlist



def generate_corresponding_vals(thelist):
  printstring = ""
  for i in range(0,len(thelist)):
    for j in range(0,len(thelist[i])):
      if int(thelist[i][j]) != 0:
        toclue = ((i * 16) + (j * 4) + int(thelist[i][j]))
        printstring += str(toclue) + " 0\n"
  return printstring

def cnf_vals_to_board(thelist):
	longlist = []
	for i in range(0, len(thelist)):
		# if ((i+4) % 4 == 0):
		# 	newlist.append([])
		# else: 
		# 	newlist.append(thelist[i] % 4)
		val = thelist[i] % 4
		if val == 0:
			val += 4
		longlist.append(val)
	# print longlist
	boardlist = [[], [], [], []]
	for i in range(0, len(longlist)):
		boardlist[i/4].append(longlist[i])
		# print boardlist
	return boardlist

# toprintout = cnf_vals_to_board([1, 6, 11, 16, 19, 24, 25, 30, 34, 37, 44, 47, 52, 55, 58, 61])
# print toprintout


def get_given_count(thelist):
	val = 0
	for i in range(len(thelist)):
		for j in range(0,len(thelist[i])):
			if int(thelist[i][j]) != 0:
				val = val + 1
	return val

# mylist = [[1,0,3,4],[3,0,1,2],[4,0,2,1],[2,0,4,3]]
# givens = generate_corresponding_vals(ourboard) 

def append_givens_to_cnf(givens, thecnf):
	file = open(thecnf, 'r+')
	firstLine = file.readline()
	file.write(givens)
	file.close()


def edit_param(givencount, cnffile):
	file1 = open(cnffile, 'r+')
	firstLine = file1.readline()
	mylist = firstLine.split()
	tochange = mylist[3]
	number = int(tochange) + givencount
	mylist[3] = str(number)
	mystring = " ".join(mylist)
	file1.seek(0)
	file1.write(mystring)
	file1.close()
# append_clues_to_cnf(givens, 'generalrules.cnf')
