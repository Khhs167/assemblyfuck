def RunProgram(program):
	reg = [0]
	ptr = 0
	i = 0
	while i < len(program):
		command = program[i]
		
		if (command == ">"):
			ptr += 1
			if(ptr >= len(reg)):
				reg.append(0)
		elif (command == "<"):
			ptr -= 1
			if(ptr < 0):
				reg.insert(0, 0)
				ptr = 0
		elif (command == "+"):
			reg[ptr] += 1
		elif (command == "-"):
			reg[ptr] -= 1
		elif (command == "["):
			if (reg[0] == 0):
				i = program[i:].index("]")
		elif (command == "."):
			print(chr(reg[ptr]), end="")
		i += 1
		if (command == "]"):
			if (reg[0] != 0):
				i = program[:i].index("[")
