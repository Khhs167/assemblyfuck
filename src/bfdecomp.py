def Decomp(program):
	out = ""
	for cmd in program:
		if (cmd == ">"):
			out += "ptr add\n"
		elif(cmd == "<"):
			out += "ptr minus\n"
		elif(cmd == "+"):
			out += "add\n"
		elif(cmd == "-"):
			out += "sub\n"
		elif(cmd == "."):
			out += "out\n"
		elif(cmd == ","):
			out += "inp\n"
		elif(cmd == "["):
			out += "{\n"
		elif(cmd == "]"):
			out += "}\n"
	print(out)
Decomp(open(input("File to decompile: "), "r"))
