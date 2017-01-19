#!/bin/bash
# will take care of the following steps
# 1. take a CNF and convert to 3CNF
# 2. test the satisfiability of 3CNF
# 3. append the solution to the CNF
# 4. re-3CNF the modified CNF
# 5. test the new 3CNF in the sat-solver
import os.path



#fileString = input("Enter the .cnf file you would like to test: ")
# Step 1: Convert to 3CNF
os.system("/Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/cnftools-master/cnf2kcnf < /Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/cnftools-master/sud43cnfplusclues1.cnf > /Users/hrre/Documents/School/Fall\\ \\\'16/MATH\ 499/treengeling-bbc-sc2016/build/lingeling/3cnf.cnf")

# Step 2: Test satisfiability
#os.system("cd /Users/hrre/Documents/Fall\\ \\\'16/MATH\\ 499/treengeling-bbc-sc2016/build/lingeling")
os.system("/Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/treengeling-bbc-sc2016/build/lingeling/treengeling < /Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/treengeling-bbc-sc2016/build/lingeling/3cnf.cnf | tail -42 | head -5  > /Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/solved.txt")

#file1 = open('solved.txt', 'r')

#this function removes the extra junk from the sat-solver output
def remove_extra_char(filename):
	file = open(filename)
	lines = file.readlines()
	file.close()
	f = open(filename, 'r+')
	for line in lines:
		f.write(line[2:])
	file.close()
	return;

#this function is what determines if our solution will be a critical set
#if there is no initial solution, we return that it is not unique
#else if we found a solution that works, we will append the solution returned
#(but not the givens) to our cnf file, re 3cnf it, and rerun it in the sat solver
#if that yields an unsatisfiable result, then we have determined that our initial solution
#was the one and only solution
def is_unique(filename):
	print 'Running is_uniq on ' + filename
	file = open(filename)
	firstLine = file.readline().strip()
	if (firstLine == 'UNSATISFIABLE'):
		print 'NOT UNIQUE'
	elif (firstLine == 'SATISFIABLE'):
		print 'ready for the next step'
		rerun_sat(filename, 'sud43cnfplusclues1.cnf')
	else:
		print 'ERROR, neither unsatisfiable or satisfiable returned'
	return;

#filename1 being solved.txt and filename2 being sud43cnfplusclues1.cnf
#now we will begin to create our next .cnf for testing, this functions calls
#the bulk of our helper methods and does most of the work
def rerun_sat(filename1, filename2):
	os.system("cat /Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/solved.txt") #debugging
	remove_sat(filename1)
	os.system("cat /Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/solved.txt") #debugging
	os.chdir("/Users/hrre/Documents/School/Fall '16/MATH 499/cnftools-master/")
	print 'Descending into cnftools-master'
	gen_alt_sol(filename1)
	os.system("cat /Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/solved.txt") #debugging
	print os.getcwd() #a check to make sure that we are still in the cnf tools directory
	os.system("cp /Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/solved.txt /Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/cnftools-master/solved.txt")
	edit_param(filename2)
	merge_files(filename1, filename2)
	return;

#this removes the part of the output that says "SATISFIABLE"
#we open the file, read it, then for all lines that do not say "SATISFIABLE",
#we overwrite our file with that line 
def remove_sat(filename):
	file = open(filename, 'r')
	lines = file.readlines()
	file.close()
	file = open(filename, 'w')
	for line in lines:
		if line!="SATISFIABLE"+"\n":
			file.write(line)
	file.close()
	print 'Opening output... removing the line that says satisfiable...'
	return;

#this gets the new clues from the first solution to append to the .cnf
#this is the step that needs to be modified (and for some reason stopped working)
#we need to create a list of the initial givens for the puzzle
#in another function, i would add each given from the puzzle
#(i would do that by going into the cnf file and for all lines of the format x 0,
# where x is some number between 0 and 64, add x to the list)
#and be able to check the list as another part of the conditional statement
#Note: the method to check if a member is contained in a list ".index", 
#will return an 'error', so we will have to use an if-else statement to handle this
def gen_alt_sol(filename):
	file = open(filename, 'r')
	lines = file.readlines()
	file.close()
	file = open(filename, 'r+')	
	file.truncate()
 	for line in lines:
		for word in line.split():
			if (int(word) > 0 and int(word) < 64):
				file.write('-'+ word + ' ')
				print "entered this block and the word is " + word #debugging
	file.write('0')
	file.write('anything') #debugging
	file.close()
	print filename #debugging
	print 'Modifying solved.txt to include only the numbers between 0 and 64...'
	#os.system("cat /Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/solved.txt") #debugging
	return;

#this changes the parameters for the .cnf file
#what this will do is add the correct number of clues in the 
#modified list of the solutions (wihtout the givens)
#We read the first line of the .cnf file 
#(which indicates the # of clauses and predicates in the file)
#We split that line into a list, which will be four numbers (if i recall correctly)
#The final number is the number of clauses, which is what we want to alter,
#we want to add one to it, because we are adding 1 extra clause to the .cnf file
#the rest of this function just handles conversions from string to integer 
#and making sure the number gets put in the correct part of the file
def edit_param(filename):
	file1 = open(filename, 'r+')
	firstLine = file1.readline()
	mylist = firstLine.split()
	tochange = mylist[3]
	number = int(tochange) + 1
	mylist[3] = str(number)
	mystring = " ".join(mylist)
	file1.seek(0)
	file1.write(mystring)
	file1.close()
	print 'Opening the .cnf file and changing the parameters...'
	return;

#this adds the clues from the solved.txt
#to the first line under the params in the .cnf
#we open the .cnf file and move ourselves to under the first line 
#(the one that deals with the clauses and such)
#then we get the string of numbers to add to the function from gen_alt_sol
#and insert it into the .cnf file. at this point that .cnf file should be ready to go
def merge_files(filename1, filename2):
	file1 = open(filename2, 'a')
	file1.seek(1)
	file = open(filename1, 'rb')
	file1.write(file.read())
	file1.close()
	file1 = open('sud43cnfplusclues1.cnf', 'r')
	lines = file1.readlines()
	file1.close()
	file1 = open('sud43cnfplusclues1.cnf', 'w')
	for line1 in lines:
		file1.write(line1),
	file1.close()
	print 'Finalizing .cnf file...'
	print 'The modified .cnf file, ' + filename2 + ', is ready to be tested using the sat-solver. It can be found in '
	print os.getcwd()
	return;




# THE ACTUAL CODE THAT IS RAN
remove_extra_char('solved.txt')
is_unique('solved.txt')
#print 'Converting .cnf to 3cnf..'
#os.system("/Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/cnftools-master/cnf2kcnf < /Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/cnftools-master/sud43cnfplusclues1.cnf > /Users/hrre/Documents/School/Fall\\ \\\'16/MATH\ 499/treengeling-bbc-sc2016/build/lingeling/3cnfNEW.cnf")
#print 'Sending a copy of the new .cnf file, 3cnfNEW.cnf, to the sat-solver directory...'
print 'Resetting the files to test again...'
os.chdir("/Users/hrre/Documents/School/Fall '16/MATH 499/treengeling-bbc-sc2016/build/lingeling/")
#os.system('rm 3cnfNEW.cnf')
os.chdir("/Users/hrre/Documents/School/Fall '16/MATH 499/cnftools-master/")
os.system('rm sud43cnfplusclues1.cnf')
os.system('cp savedfile.cnf sud43cnfplusclues1.cnf')
os.chdir("/Users/hrre/Documents/School/Fall '16/MATH 499/")




#os.chdir("/Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/cnftools-master/")
#filepath = os.path.join('/Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/cnftools-master/', 'newfile.txt')
#if not os.path.exists('/Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/cnftools-master/'):
#	os.makedirs('/Users/hrre/Documents/School/Fall\\ \\\'16/MATH\\ 499/cnftools-master/')



