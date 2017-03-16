def gen_neg_clauses(t):
    thestring = ""
    for x in range(t**2):
        for y in range(t**2):
            for a in range(t**2-1):
                for b in range(a+1,t**2):
                    var1 = (t**4)*x+(t**2)*y+a+1
                    var2 = (t**4)*x+(t**2)*y+b+1
                    thestring += '-'+str(var1)+' '+'-'+str(var2)+' 0\n'
    return thestring

def gen_pos_clauses(t):
    # rows
    thestring = ""
    for a in range(t**2):
        for x in range(t**2):
            outstr = ''
            for y in range(t**2):
                outstr += str((t**4)*x+(t**2)*y+a+1)+' '
            thestring += outstr+'0\n'
    # cols
    for a in range(t**2):
        for y in range(t**2):
            outstr = ''
            for x in range(t**2):
                outstr += str((t**4)*x+(t**2)*y+a+1)+' '
            thestring += outstr+'0\n'
    # blocks
    for a in range(t**2):
        for band in range(t):
            for stack in range(t):
                outstr = ''
                for x in range(band*t,(band+1)*t):
                    for y in range(stack*t,(stack+1)*t):
                        outstr += str((t**4)*x+(t**2)*y+a+1)+' '
                thestring += outstr+'0\n'
    return thestring



# if elem == (len(input_list) - 1):
# 				thestring = thestring + strtoappend
# 			else:
# 				thestring = thestring + strtoappend + "\n"


def gen_all_rules(t):
	returnstring = ""
	postring = gen_pos_clauses(t)
	returnstring += postring
	negstring = gen_neg_clauses(t)
	returnstring += negstring
	return returnstring


def create_cnf_file(filename, rulesstring):
	file = open(filename, 'w+')
	file.write('p cnf 64 144\n')
	file.write(rulesstring)
	file.close()

# create_cnf_file('generalrules.cnf')


# add 'p cnf 64 (96 + 48)'




