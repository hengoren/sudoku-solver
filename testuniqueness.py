#import packages
#os.path will be used to make calls to the command line
#re will make use of pythons regular expression package
import os.path
import re
import sys

#should be operating in the directory that has cnftools-master as a folder
#this will save the path as a string so that the code may be ran by different users
path = os.getcwd()
print "PATH: " + path





#methods (in alphabetical order)


#This method will add the alternative solution to the original .cnf using the list generated
#in gen_alt_sol and mult_list_negative. It opens the file, navigates to the correct index, 
#and then writes in the clues from the list to alter the .cnf file. 
#This is the final step before re-running the sat-solver.
def append_sol_cnf(filename1, alist):
	file1 = open(filename1, 'a')
	file1.seek(1)
	file1.write(" ".join(str(n) for n in alist)) 
	file1.close()
	file1 = open(filename1, 'r')
	lines = file1.readlines()
	file1.close()
	file1 = open(filename1, 'w')
	for line1 in lines:
		file1.write(line1)
		file1.write("\n")
	file1.close()
	print 'Finalizing .cnf file...'
	print 'The modified .cnf file, ' + filename1 + ', is ready to be tested using the sat-solver. It can be found in '
	print os.getcwd()

#Part of the operation of the executable that changes .cnf files to 3cnf 
#depends on the amount of clauses in the file. When we test for uniqueness, 
#we append another clause to the .cnf file. This method will update the 
#parameter of the .cnf file to increase it by 1 as necessary.
def edit_param(filename):
	file1 = open(filename, 'r+')
	print file1
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


#When we append the solution from the sat-solver to test uniqueness, we must
#pull the solution from the sat-solver's output. In this method, we read the first line
#(which will say satisfiable) and then read in the rest of the file, which is the solution.
#For each positive number under 64 (which indicates a certain number being assigned to 
#a certain square in the puzzle), we append it to a list 'nums'. We also append the number 0,
#this is useful for appending to the .cnf because all lines in the .cnf must end with 0.
#Next, we loop through the list of clues and check to see if it is in the list of nums. 
#If it is, we remove it, then we return our list of solutions (that are not the clues)
def gen_alt_sol(filename, alist):
	file = open(filename, 'r+')
	firstLine = file.readline() #makes it so we do not look at the line that says SATISFIABLE
	lines = file.readlines()
 	nums = []
 	print "Our clues:"
 	print alist
 	for line in lines:
		for word in line.split():
			if (int(word) > 0 and int(word) < 64):
				nums.append(int(word))
	nums.append(0)
	print "Solution to puzzle:"
	print nums
	for elem in alist:
		if elem in nums:
			print str(elem) + " is a clue. Remove from list"
			nums.remove(elem)
	print "Updated list:"
	print nums
	print file
	file.close()
	print file
	return nums


#When we go to test for uniqueness, we need to append the (negation of the) solution 
#to the original .cnf to ensure that is the only solution. However, we must not negate
#the initial givens from the original puzzle. In order to do this, we must know what
#the initial givens from the original puzzle are. This method identifies the clues and 
#returns them in a list clues.
def identify_clues(filename):
	file = open(filename, 'r')
	print file
	firstLine = file.readline()
	lines = file.readlines()
	clues = []
	for line in lines:
		matchObj = re.match( r'([0-9]*) 0', line, re.M)
		if matchObj:
			if (int(matchObj.group(1)) < 64):
				clues.append(int(matchObj.group(1)))
		else:
				print "No match!!"
	print "Identify Clues located these as clues: "
	print clues
	return clues

#If we are to find a unique solution, we must be sure that there is at least one solution.
#This method tests if the sat-solver returned a satisfiable solution. If so, we will proceed
#to run the methods necessary to re-run the sat-solver to test uniqueness.
def is_satisfiable(filename, cnffile): #is satisfiable and sends to next step
	print 'Running is_satisfiable on ' + filename
	if 'UNSATISFIABLE' in open(filename).read():
		print 'NOT UNIQUE'
		os.chdir("%s/lingeling-bbc-9230380-160707-druplig-009/lingeling" % (path))
		print 'Navigating to lingeling directory with druplig...'		
		os.system('%s/lingeling-bbc-9230380-160707-druplig-009/lingeling/lingeling %s/cnftools-master/%s -v --druplig --drupligtrace > %s/unsatcertificate.txt' % (path, path, cnffile, path))
		print 'Unsat certificate piped to file unsatcertificate.txt in %s' % (path)
	elif 'SATISFIABLE' in open(filename).read():
		print 'Satisfiable.\n If this is your second time through, your puzzle is NOT UNIQUE.\n'
		print 'If this is your first time through, press 1 to proceed to the next step'
		# userinput = raw_input("Press 1 if this your first time through\n")
		# if userinput is "1":
			#cut off output
		run_sat_and_cnf(cnffile, '3cnf.cnf', 'solved1.txt')
		is_satisfiable('solved1.txt', cnffile)
		# else: 
			# print "NOT UNIQUE"
	else:
		print 'ERROR, neither unsatisfiable or satisfiable returned. Script terminated.'
		sys.exit()


	# file = open(filename)
	# firstLine = file.readline().strip()
	# print "The first line is: " + firstLine
	# file.close()
	# if (firstLine == 'UNSATISFIABLE'):
	# 	print 'NOT UNIQUE'
	# elif (firstLine == 'SATISFIABLE'):
	# 	print 'Proceeding to the next step...'
	# 	rerun_sat(filename, 'sud43cnfplusclues1.cnf')
	# else:
	# 	print 'ERROR, neither unsatisfiable or satisfiable returned. Script terminated.'
	# 	sys.exit()


#This method will loop through the list of clues generated by gen_alt_sol and
#multiply each of them by -1. This is necessary because when we append to the 
#.cnf file we want to make sure that we do not find the same exact solution.
#This will return the list from gen_alt_sol, but with negative numbers (and still the 0).
def mult_list_negative(alist):
	newlist = []
	for elem in alist:
		newlist.append(elem * -1)
	print "entered mult_clues_negative"
	print newlist
	return newlist

#This function removes the extra characters from the sat-solver's output.
def remove_extra_char(filename):
	file = open(filename)
	lines = file.readlines()
	file.close()
	f = open(filename, 'w')
	for line in lines:
		f.write(line[2:])
	f.close()

#This function calls upon all the helper functions to re-run the sat-solver.
#It takes in the output from the sat-solver and the .cnf file as params respectively.
#It makes sure we are in the correct directory to call upon the output from the sat-solver.
#Then it obtains the list of clues from .cnf file and uses it as a parameter to find
#the alternate solution. Then we use that solution and negate it as necessary for the .cnf.
#Then we alter the parameters of the .cnf file so that the 3cnf script can be reran.
#Finally, we append the alterative solution to the .cnf.
def rerun_sat(filename1, filename2):
	os.chdir(path + "/cnftools-master/")
	print 'Descending into cnftools-master'
	theclues = identify_clues(filename2)
	thelist = gen_alt_sol(filename1, theclues)
	negclues = mult_list_negative(thelist)
	edit_param(filename2)
	append_sol_cnf(filename2, negclues)

def run_sat_and_cnf(cnfin, the3cnf, output):
	#call the system to convert to 3cnf
	print "Running 3cnf on " + cnfin
	os.system("%s/cnftools-master/cnf2kcnf < %s/cnftools-master/%s > %s/lingeling-bbc-9230380-160707-druplig-009/lingeling/%s" % (path, path, cnfin, path, the3cnf))
	#os.system(path + "/cnftools-master/cnf2kcnf < " + path + "/cnftools-master/" + tobe3cnf + " > " + path + "/lingeling-bbc-9230380-160707-druplig-009/lingeling/" + the3cnf)
	#call the system to test satisfiability
	print "Running sat-solver"
	os.system("%s/lingeling-bbc-9230380-160707-druplig-009/lingeling/lingeling < %s/lingeling-bbc-9230380-160707-druplig-009/lingeling/%s -v --druplig --drupligtrace > %s/%s" % (path, path, the3cnf, path, output))
	#os.system(path + "/lingeling-bbc-9230380-160707-druplig-009/lingeling/lingeling < " + path + "/lingeling-bbc-9230380-160707-druplig-009/lingeling/" + the3cnf + " | tail -35 | head -18 > " + path + output)

#remove the extra characters from sat-solver's output
print os.getcwd()
run_sat_and_cnf('sud4.cnf', '3cnf.cnf', 'solved.txt')
# run_sat_and_cnf('sud43cnfplusclues1.cnf', '3cnf.cnf', 'solved.txt')
remove_extra_char('solved.txt')
#test to see if the 3cnf was satisfiable
is_satisfiable('solved.txt', 'sud4.cnf')
os.chdir(path)
# remove_extra_char('solved1.txt')



