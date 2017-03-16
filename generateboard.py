import makecnfclues
import rulesofsudoku
import sys

givensinput = sys.argv[1]
cnfinput = sys.argv[2]


def make_cnf_file(givensfilename, cnffilename):
	rulesstring = rulesofsudoku.gen_all_rules(2)
	rulesofsudoku.create_cnf_file(cnffilename, rulesstring)
	theboard = makecnfclues.get_board_from_file(givensfilename)
	givens = makecnfclues.generate_corresponding_vals(theboard)
	numberofgivens = makecnfclues.get_given_count(theboard)
	makecnfclues.append_givens_to_cnf(givens, cnffilename)
	makecnfclues.edit_param(numberofgivens, cnffilename)

make_cnf_file(givensinput, cnfinput)


# p cnf 64 144
# p cnf 