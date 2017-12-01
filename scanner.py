import re

f_handle = open("tiny_sample_code.txt","r")
file = f_handle.readlines()
text_file = open("scanner_output.txt", "w")


def saveToken (token):
	specialSymbols = ["+","-","*","/","=","<",">","(",")",";",":="]
	ReservedWords = ["if","then","else","end","repeat","until","read","write"]
	if (token in specialSymbols) :
		text_file.write("%s: special symbol\n" %token) 
		
	elif(token in ReservedWords) :
		text_file.write("%s : reserved word\n" %token)

	elif(re.match('[0-9]+',token)) :
		text_file.write("%s : number\n" %token)
		
	elif(re.match('[A-Za-z]',token)) :
		text_file.write("%s : identifier\n" %token)			

def create_token(token,data,old_state,state) :
	if(old_state == state) :
		token += data
	else :
		if (token != "empty") :
			saveToken(token)
		token = data
	return token	

old_state = "no state"
state = "start"
token = "empty"

for line in file :

	for data in line :
		if (state == "comment_start") :
			if re.match('}',data) :
				state = "start"

		elif (re.match(' |\n', data)) :
			state = "space & new line"

		elif (re.match('[0-9]',data)) :
			state = "digit"
			token = create_token(token,data,old_state,state)
								
		elif (re.match('[A-Za-z]',data)) :
			state = "word"
			token = create_token(token,data,old_state,state)

		elif (re.match('\*|\+|-|/|<|>|\(|\)|;',data)) :
			state = "special symbole"
			token = create_token(token,data,old_state,state)

		elif re.match(':',data) :
			state = "assignment"	
			token = create_token(token,data,old_state,state)

		elif re.match('=',data)	:
			if (old_state == "assignment") :
				state = "assignment"
			else :
				state = "equal"
			token = create_token(token,data,old_state,state)	

		elif (re.match('{',data)) :
			state = "comment_start"

		old_state = state

saveToken(token)			

					



		