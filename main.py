from scanner import Scanner
from parser import Parser


program_scanner = Scanner()
token_list = program_scanner.scan()
program_parser= Parser(token_list)
program_parser.parse()