from scanner import Scanner
from parser import Parser


program_scanner = Scanner()
token_list = program_scanner.scan() #this token list is a list of lists each small list 
									#contains the token name and the token value
program_parser= Parser(token_list)
program_parser.parse()