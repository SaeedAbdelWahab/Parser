
import sys
from scanner import Scanner


def adjust_list(lest) :
	adjusted_list = []
	for item in lest :
		if (item [1] == "reservedword" or item[1] == "specialsymbol") :
			adjusted_list.append(item[0])
		else :
			adjusted_list.append(item[1])
	return adjusted_list

def Error():
	print ("Error found at",token)
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
			print ("Program was parsed successfully with no errors")			
	else:
		Error()

def program() :
	stmt_sequence()
	text_file.write("Program Found \n")

def stmt_sequence():
	statment()
	while (token == ";"):
		match(";")
		statment()
	text_file.write("Statment_sequence Found \n")	

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
	text_file.write("Statment Found \n")	

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
	text_file.write("If_Statment Found \n")	

def repeat_stmt():
    match('repeat')
    stmt_sequence()
    match('until')
    exp()
    text_file.write("Repeat_Statment Found \n")

def assign_stmt():
    match('identifier')
    match(':=')
    exp()
    text_file.write("Assignment_Statment Found \n")
    #heree

def read_stmt():
	match('read')
	match('identifier')
	text_file.write("Read_Statment Found \n")

def write_stmt():
	match('write')
	exp()
	text_file.write("Write_Statment Found \n")

def exp():
	simple_exp()
	if (token == '<' or token == '='):
		comparison_op()
		simple_exp() 	   
	text_file.write("Expression Found \n")   
            
def comparison_op():
    if (token=='<' or token == '='):
        match(token)
    else:
        Error()
    text_file.write("Comparison_Operator Found \n")

def simple_exp():
    term()
    while (token == '+' or token == '-'):
        add_op()
        term()  
    text_file.write("Simple_Expression Found \n")     
       
def add_op():
    if (token=='+' or token == '-'):
        match(token)
    else:
        Error() 
    text_file.write("Add_Operator Found \n")   

def term():
	factor()
	while(token=="*" or token=="/"):
		mulop()	
		factor()
	text_file.write("Term Found \n")	

def mulop():
	if(token=="*" or token=="/"):
		match(token)
	else :
		Error()
	text_file.write("Mul_Operator Found \n")	

def factor():
	if(token=="number" or token=="identifier"):
		match(token)
	elif(token=="("):
		match("(")
		exp()
		match(")")
	else:
		Error() 
	text_file.write("Factor Found \n")	



program_scanner = Scanner()
program_scanner.scan()

f_handle = open("scanner_output.txt","r")
file = f_handle.readlines()
token_list = []

for line in file :
	line = line.replace('\n','')
	line = line.replace(' ','')
	token_list.append(line.rsplit(':',1))	

tokens = adjust_list(token_list)

text_file = open("parser_output.txt", "w")

i = 0
token = tokens[0]
  							
program()
