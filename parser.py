import sys

class Parser :
	def __init__(self,token_list) :
		self.tokens = self.adjust_list(token_list)
		self.i = 0
		self.token = self.tokens[0]
		self.text_file = open("parser_output.txt", "w")

	def adjust_list(self,lest) :
		adjusted_list = []
		for item in lest :
			if (item [1] == "reservedword" or item[1] == "specialsymbol") :
				adjusted_list.append(item[0])
			else :
				adjusted_list.append(item[1])
		return adjusted_list	

	def Error(self):
		print ("Error found at",self.token)
		sys.exit()

	def match(self,t):
		if (t==self.token):
			if (self.i < len(self.tokens)-1) :
				self.i+=1
				self.token=self.tokens[self.i]	
			else : 
				print ("Program was parsed successfully with no errors")			
		else:
			self.Error()


	def parse(self) :
		self.program()		

	def program(self) :
		self.stmt_sequence()
		self.text_file.write("Program Found \n")

	def stmt_sequence(self):
		self.statment()
		while (self.token == ";"):
			self.match(";")
			self.statment()
		self.text_file.write("Statment_sequence Found \n")	

	def statment(self):
		if (self.token == "if") :
			self.if_stmt()
		elif (self.token == "repeat") :
			self.repeat_stmt()
		elif (self.token == "read") :
			self.read_stmt()
		elif (self.token == "write") :
			self.write_stmt()
		elif (self.token == "identifier") :
			self.assign_stmt()
		else :
			self.Error()	
		self.text_file.write("Statment Found \n")	

	def if_stmt(self) :
		if (self.token == "if") :
			self.match("if")
			self.exp()
			if (self.token == "then") :
				self.match("then")
				self.stmt_sequence()
				if (self.token == "end") :
					self.match("end")
				elif (self.token == "else") :
					self.match("else")
					self.stmt_sequence()
					if(self.token == "end") :
						self.match("end")
					else :
						self.Error()	
				else :
					self.Error()	
			else :
				self.Error()
		else :
			self.Error()	
		self.text_file.write("If_Statment Found \n")	

	def repeat_stmt(self):
	    self.match('repeat')
	    self.stmt_sequence()
	    self.match('until')
	    self.exp()
	    self.text_file.write("Repeat_Statment Found \n")

	def assign_stmt(self):
	    self.match('identifier')
	    self.match(':=')
	    self.exp()
	    self.text_file.write("Assignment_Statment Found \n")
	    #heree

	def read_stmt(self):
		self.match('read')
		self.match('identifier')
		self.text_file.write("Read_Statment Found \n")

	def write_stmt(self):
		self.match('write')
		self.exp()
		self.text_file.write("Write_Statment Found \n")

	def exp(self):
		self.simple_exp()
		if (self.token == '<' or self.token == '='):
			self.comparison_op()
			self.simple_exp() 	   
		self.text_file.write("Expression Found \n")   
	            
	def comparison_op(self):
	    if (self.token=='<' or self.token == '='):
	        self.match(self.token)
	    else:
	        self.Error()
	    self.text_file.write("Comparison_Operator Found \n")

	def simple_exp(self):
	    self.term()
	    while (self.token == '+' or self.token == '-'):
	        self.add_op()
	        self.term()  
	    self.text_file.write("Simple_Expression Found \n")     
	       
	def add_op(self):
	    if (self.token=='+' or self.token == '-'):
	        self.match(self.token)
	    else:
	        self.Error() 
	    self.text_file.write("Add_Operator Found \n")   

	def term(self):
		self.factor()
		while(self.token=="*" or self.token=="/"):
			self.mulop()	
			self.factor()
		self.text_file.write("Term Found \n")	

	def mulop(self):
		if(self.token=="*" or self.token=="/"):
			self.match(self.token)
		else :
			self.Error()
		self.text_file.write("Mul_Operator Found \n")	

	def factor(self):
		if(self.token=="number" or self.token=="identifier"):
			self.match(self.token)
		elif(self.token=="("):
			self.match("(")
			self.exp()
			self.match(")")
		else:
			self.Error() 
		self.text_file.write("Factor Found \n")	



	



