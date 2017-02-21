import os.path
import re
import sys
import scriptfunctions

cnfin = sys.argv[1]
threecnf = "threecnf" + sys.argv[1]
output = "output" + sys.argv[1]

def testuniqueness(cnfin, threecnf, output):
	scriptfunctions.run_cnf_and_sat(cnfin, threecnf, output)
	if (scriptfunctions.is_satisfiable(output)):
		scriptfunctions.remove_extra_char(output)
		scriptfunctions.modify_cnf(output, cnfin)
		scriptfunctions.run_cnf_and_sat(cnfin, threecnf, output)
		if (scriptfunctions.is_satisfiable(output)):
			print("Puzzle is not unique")
			# pipe output to new file
			return False
		else:
			print("Puzzle is unique")
			# pipe output to a new file
			return True
	else:
		print("This was not a valid board.")

testuniqueness(cnfin, threecnf, output)