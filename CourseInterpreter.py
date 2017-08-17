tokens = []
symbol_Table = {}
def open_file(file):
	data = open(file, 'r').read()
	data += "<EOF>"
	return data

def lex(filecontents):
	tok = ""
	state = 0
	expr = ""
	isexpr = 0
	sign = 0
	start = 0
	var = ""
	varstarted = 0
	string = ""
	filecontents = list(filecontents)
	for char in filecontents:
		tok += char
		if tok == " ":
			if state == 0:
				tok = ""
			else:
				tok = " "
		elif tok == "program":
			print("program found")
			start = 1
			tok = ""
		elif tok == "begin":
			if start !=1:
				raise Exepetion("Program keyword is missing")
			else:
				print("program begin")
			tok = ""
		elif tok == ":":
			tok = ""
		elif tok == "end":
			print("program End")
			tok = ""

		elif tok == "\n" or tok == "<EOF>":
			if expr != "" and isexpr == 1:
				tokens.append("Expr:" +expr)
				expr = ""
			elif expr != "" and isexpr == 0:
				tokens.append("Num:" +expr)
				expr = ""
			elif var !="":
				tokens.append("Var:" +var)
				varstarted = 0
				var = ""
			tok = ""	
		elif tok == "=" and state == 0:
			if expr != "" and isexpr == 0:
				tokens.append("Num:" +expr)
				expr = ""

			if var != "":
				tokens.append("Var:" +var)
				var = ""
				varstarted = 0
			if tokens[-1] == "Equals":
				tokens[-1] = "EE"
			else:
				tokens.append("Equals")
			tok = ""
		
		elif tok == "$" and state == 0:
			varstarted = 1	
			var +=tok	
			tok = ""	
		elif varstarted == 1:
			if tok == "<" or tok == ">" :
				if var != "":
					tokens.append("Var:" +var)
					var = ""
					varstarted = 0
			var += tok
			tok = ""	
		elif tok == "\t":
			tok = ""
		elif tok == "print":
			tokens.append("print")
			tok =""
		elif tok == "input":
			tokens.append("input")
			tok = ""
		elif tok == "if":
			tokens.append("if")
			tok = ""
		elif tok == "else":
			tokens.append("else")
			tok = ""
		elif tok == "endif":
			tokens.append("endif")
			tok = ""
		elif tok == "then":
			if expr != "" and isexpr == 0:
				tokens.append("Num:" +expr)
				expr = ""
			tokens.append("then")
			tok = ""
		elif tok == "0" or tok == "1" or tok == "2" or tok == "3" or tok == "4" or tok == "5" or tok == "6" or tok == "7" or tok == "8" or tok == "9":
			expr +=tok
			sign = 1
			tok =""
		elif tok == "+" or tok == "-" or tok == "*" or tok == "/":
			isexpr = 1
			expr += tok
			tok =""
		elif tok == "\"" or tok == " \"":
			if state == 0:
				state = 1
			elif state == 1:
				tokens.append("String:" + string + "\"")
				string = ""
				state = 0
				tok = ""
		elif sign == 1 and expr !="":
			tokens.append("Num:"+expr)
			expr = ""
			if tok == "<":
				tokens.append("Smaller")
				tok = ""
			elif tok == ">":
				tokens.append("Greater")
				tok = ""
			sign = 0
		
		elif state == 1:
			string += tok
			tok = ""
	#print(tokens)
	return tokens
	#return ''

def doPrint(toPrint):
	if toPrint[0:6] == "String":
		toPrint = toPrint[8:]
		toPrint = toPrint[:-1]
	elif toPrint[0:3] == "Num":
		toPrint = toPrint[4:]
	elif toPrint[0:4] == "Expr":
		toPrint = evaluate(toPrint[5:])
	print(toPrint)

def evaluate(expr):
	return eval(expr)

def Assigmnet(name,value):
	symbol_Table[name[4:]] = value

def getVariable(name):
	name = name[4:]
	if name in symbol_Table:
		return symbol_Table[name]
	else:
		return "Error"
		exit()

def getInput(varname,string):
	i = input(string[1:-1])
	symbol_Table[varname] = "String:\"" + i + "\""


def parse(toks):
	i = 0
	secondOption = 0
	while (i < len(toks)):
		if toks[i] == "endif":
			i+=1
	
		elif secondOption == 0 and  toks[i] + " " + toks[i+1][0:6] == "print String" or toks[i] + " " + toks[i+1][0:3] == "print Num" or toks[i] + " " + toks[i+1][0:4] == "print Expr" or toks[i] + " " + toks[i+1][0:3] == "print Var": 
			if toks[i+1][0:6] == "String":
				doPrint(toks[i+1])
			elif toks[i+1][0:3] == "Num":
				doPrint(toks[i+1])
			elif toks[i+1][0:4] == "Expr":
				doPrint(toks[i+1])
			elif toks[i+1][0:3] == "Var":
				doPrint(getVariable(toks[i+1]))
			i+=2
		elif secondOption == 0 and toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:6] == "Var Equals String" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "Var Equals Num" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:4] == "Var Equals Expr" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "Var Equals Var":
			if toks[i+2][0:6] == "String":
				Assigmnet(toks[i],toks[i+2])
			elif toks[i+2][0:3] == "Num":
				Assigmnet(toks[i],toks[i+2])
			elif toks[i+2][0:4] == "Expr":
				Assigmnet(toks[i],"Num:" + str(evaluate(toks[i+2][5:])))
			elif toks[i+2][0:3] == "Var":
				Assigmnet(toks[i],getVariable(toks[i+2]))
			i+=3
		elif secondOption == 0 and toks[i][0:3] + " " +toks[i+1] + " " + toks[i+2] + " " + toks[i+3][0:6] == "Var Equals input String":
			getInput(toks[i][4:],toks[i+3][7:])
			i+=4

		##===========If Statement============##	
		elif secondOption == 0 and toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "if Num EE Num then":
			if toks[i+1][4:] == toks[i+3][4:]:
				print("T")
			else:
				secondOption = 1
			i+=5
			
		elif secondOption == 0 and toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3] + " " + toks[i+4][0:3] + " "+ toks[i+5] == "if Num Greater Equals Num then":
			if toks[i+1][4:] >= toks[i+4][4:]:
				print("Greater")
			else:
				secondOption = 1
			i+=6	
			
		elif secondOption == 0 and toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3] + " " + toks[i+4][0:3] + " " + toks[i+5] == "if Num Smaller Equals Num then":
			if toks[i+1][4:] <= toks[i+4][4:]:
				print("Smaller")
			else:
				secondOption  = 1
			i+=6
		elif secondOption == 1:
			if toks[i] == "else":
				i+=1
				secondOption = 0
			else:
				i+=1	
		else:
			i+=1		
		
		
		
				

def run():
	file = input("Enter the file name>>")
	data = open_file(file)
	toks = lex(data)
	parse(toks)

run()