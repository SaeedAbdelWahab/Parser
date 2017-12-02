
import sys

def adjust_list(lest) :
	adjusted_list = []
	for item in lest :
		if (item [1] == "reservedword" or item[1] == "specialsymbol") :
			adjusted_list.append(item[0])
		else :
			adjusted_list.append(item[1])
	return adjusted_list

f_handle = open("scanner_output.txt","r")
file = f_handle.readlines()
filee = []

for line in file :
	line = line.replace('\n','')
	line = line.replace(' ','')
	filee.append(line.rsplit(':',1))	

tokens = adjust_list(filee)

i=0
token=tokens[0]

def Error():
	print ("Error at",token)
	sys.exit()


def match(t):
	global i
	global token
	global tokens

	if (t==token):
		if (i < len(tokens)-1) :
			i+=1
			token=tokens[i]
		else :
			print ("program parsed successfully ending with the token \"",token,"\"")	
	else:
		Error()



def program() :
	stmt_sequence()

def stmt_sequence():
	statment()
	while (token == ";"):
		match(";")
		statment()
def statment():
	if (token == "if") :
		if_stmt()
	elif (token == "repeat") :
		repeat_stmt()
	elif (token == "read") :
		read_stmt()
	elif (token == "write") :
		write_stmt()
	elif (token == "identifier") :
		assign_stmt()
	else :
		Error()	

def if_stmt() :
	if (token == "if") :
		match("if")
		exp()
		if (token == "then") :
			match("then")
			stmt_sequence()
			if (token == "end") :
				match("end")
			elif (token == "else") :
				match("else")
				stmt_sequence()
				if(token == "end") :
					match("end")
				else :
					Error()	
			else :
				Error()	
		else :
			Error()
	else :
		Error()	


def repeat_stmt():
    match('repeat')
    stmt_sequence()
    match('until')
    exp()

def assign_stmt():
    match('identifier')
    match(':=')
    exp()
    #heree

def read_stmt():
	match('read')
	match('identifier')

def write_stmt():
    match('write')
    exp()

def exp():
	simple_exp()
	if (token == '<' or token == '='):
		comparison_op()
		simple_exp()    
            
            


def comparison_op():
    if (token=='<' or token == '='):
        match(token)
    else:
        Error()

def simple_exp():
    term()
    while (token == '+' or token == '-'):
        add_op()
        term()   
        


def add_op():
    if (token=='+' or token == '-'):
        match(token)
    else:
        Error()

##Sherif


def term():
	factor()
	while(token=="*" or token=="/"):
		mulop()	
		factor()


def mulop():
	if(token=="*" or token=="/"):
		match(token)
	else :
		Error()

def factor():
	if(token=="number" or token=="identifier"):
		match(token)
	elif(token=="("):
		match("(")
		exp()
		match(")")
	else:
		Error()    							

program()
