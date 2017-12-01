import scanner

def adjust_list(lest) :
	adjusted_list = []
	for item in lest :
		if (item [1] == "reservedword" or item[1] == "specialsymbol") :
			adjusted_list.append(item[0])
		else :
			adjusted_list.append(item[1])
	return adjusted_list

f_handle = open("x.txt","r")
file = f_handle.readlines()

filee = []

for line in file :
	line = line.replace('\n','')
	line = line.replace(' ','')
	filee.append(line.rsplit(':',1))	

tokens = adjust_list(filee)
print (*tokens,sep='  ')


			


def program() :
	stmt_sequence()

def stmt_seq():
	statment()
	while (token == ";"):
		match(token)
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
		match(token)
		exp()
		if (token == "then") :
			match(token)
			stmt_sequence()
			if (token == "end") :
				match(token)
			elif (token == "else") :
				match(token)
				stmt_sequence()
				if(token == "end") :
					match(token)
				else :
					Error()	
			else :
				Error()	
		else :
			Error()
	else :
		Error()						

