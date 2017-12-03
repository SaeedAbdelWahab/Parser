import re


class Scanner :

	def __init__(self) :
		self.f_handle = open("tiny_sample_code.txt","r")
		self.file = self.f_handle.readlines()
		self.text_file = open("scanner_output.txt", "w")

	def saveToken(self,token) :
		specialSymbols = ["+","-","*","/","=","<",">","(",")",";",":="]
		ReservedWords = ["if","then","else","end","repeat","until","read","write"]
		if (token in specialSymbols) :
			self.text_file.write("%s: special symbol\n" %token) 	
		elif(token in ReservedWords) :
			self.text_file.write("%s : reserved word\n" %token)
		elif(re.match('[0-9]+',token)) :
			self.text_file.write("%s : number\n" %token)			
		elif(re.match('[A-Za-z]',token)) :
			self.text_file.write("%s : identifier\n" %token)

	def create_token(self,token,data,old_state,state) :
		if(old_state == state) :
			token += data
		else :
			if (token != "empty") :
				self.saveToken(token)
			token = data
		return token

	def scan(self) :	
		old_state = "no state"
		state = "start"
		token = "empty"
		for line in self.file :
			for data in line :
				if (state == "comment_start") :
					if re.match('}',data) :
						state = "start"

				elif (re.match(' |\n', data)) :
					state = "space & new line"

				elif (re.match('[0-9]',data)) :
					state = "digit"
					token = self.create_token(token,data,old_state,state)
										
				elif (re.match('[A-Za-z]',data)) :
					state = "word"
					token = self.create_token(token,data,old_state,state)

				elif (re.match('\*|\+|-|/|<|>|\(|\)|;',data)) :
					state = "special symbole"
					token = self.create_token(token,data,old_state,state)

				elif re.match(':',data) :
					state = "assignment"	
					token = self.create_token(token,data,old_state,state)

				elif re.match('=',data)	:
					if (old_state == "assignment") :
						state = "assignment"
					else :
						state = "equal"
					token = self.create_token(token,data,old_state,state)	

				elif (re.match('{',data)) :
					state = "comment_start"

				old_state = state

		self.saveToken(token)
		self.text_file.close()	


			

			

					



		