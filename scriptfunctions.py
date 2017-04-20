#!/usr/bin/python

import os.path
import re
import sys
import makecnfclues

path = os.getcwd()
# print "PATH: " + path

def run_cnf_and_sat(cnfin, threecnf, output):
	# print ("Running 3cnf script. Input: %s, Output: %s" % (cnfin, threecnf))
	os.system("%s/cnftools-master/cnf2kcnf < %s/%s > %s/%s" % (path, path, cnfin, path, threecnf))
	# print ("Running sat-solver script. Input: %s, Output: %s" % (threecnf, output))
	os.system("%s/lingeling-bbc-9230380-160707-druplig-009/lingeling/lingeling < %s/%s -v --drupligtrace > %s/%s" % (path, path, threecnf, path, output))

def is_satisfiable(solveroutput):
	# print("Checking to see if the output in %s is satisfiable" % (solveroutput))
	if "UNSATISFIABLE" in open(solveroutput).read():
		return False
	elif "SATISFIABLE" in open(solveroutput).read():
		return True
	else: 
		# print("Error, neither unsatisifable or satisfiable returned. Script terminated.")
		sys.exit()

def remove_extra_char(solveroutput):
	file = open(solveroutput)
	lines = file.readlines()
	file.close()
	f = open(solveroutput, 'w')
	for line in lines:
		f.write(line[2:])
	f.close()

def identify_clues(cnffile):
	file = open(cnffile, 'r')
	firstLine = file.readline()
	lines = file.readlines()
	clues = []
	for line in lines:
		matchObj = re.match( r'([0-9]*) 0', line, re.M)
		if matchObj:
			if (int(matchObj.group(1)) < 64):
				clues.append(int(matchObj.group(1)))
		# else:
		# 	print("No match!")
	# print("identify_clues located these as clues: ")
	# print(clues)
	return clues

def gen_alt_sol(solveroutput, fullsolutionlist):
	file = open(solveroutput, 'r+')
	firstLine = file.readline()
	lines = file.readlines()
	nums = []
	# print("Our clues: ")
	# print(fullsolutionlist)
	solutionblock = ""
	found = False
	for line in lines:
		if found:
			if "agil:" in line: break
			solutionblock += line
		else:
			if line.strip() == "SATISFIABLE":
				found = True
	file.close()
	literals = solutionblock.split()
	for literal in literals:
		if (int(literal) > 0 and int(literal) < 64):
			nums.append(int(literal))
	# print("Solution to puzzle: ")
	# print(makecnfclues.cnf_vals_to_board(nums))
	nums.append(0)
	# print("Solution to puzzle: ")
	# print(nums)
	for clue in fullsolutionlist:
		if clue in nums:
			# print str(clue) + " is a clue. Remove from list"
			nums.remove(clue)
	# print("Solution without clues: ")
	# print(nums)
	return nums

def mult_list_negative(solutionlistwithoutclues):
	# print(solutionlistwithoutclues)
	neglist = []
	for clue in solutionlistwithoutclues:
		neglist.append(clue * -1)
	# print("negated list of solution: ")
	# print(neglist)
	return neglist

def edit_param(cnffile):
	file1 = open(cnffile, 'r+')
	firstLine = file1.readline()
	mylist = firstLine.split()
	tochange = mylist[3]
	number = int(tochange) + 1
	mylist[3] = str(number)
	mystring = " ".join(mylist)
	file1.seek(0)
	file1.write(mystring)
	file1.close()

def append_sol_cnf(cnffile, negclues):
	# print("Doing Append")
	cnf = open(cnffile, 'a')
	cnf.seek(1)
	cnf.write(" ".join(str(clue) for clue in negclues))
	cnf.close()
	cnf = open(cnffile, 'r')
	lines = cnf.readlines()
	cnf.close()
	cnf = open(cnffile, 'w')
	for line1 in lines:
		cnf.write(line1)
	cnf.close()

def modify_cnf(solveroutput, cnffile):
	# remove_extra_char(solveroutput)
	theclues = identify_clues(cnffile)
	thelist = gen_alt_sol(solveroutput, theclues)
	neglist = mult_list_negative(thelist)
	edit_param(cnffile)
	append_sol_cnf(cnffile, neglist)



