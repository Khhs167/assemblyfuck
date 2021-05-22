def toBrain(opcode):
	commands = opcode.split(" ")
	if (len(commands) == 0):
		return ""
	if(commands[0] == "ptr"):
		if(len(commands) == 1):
			print("Invalid command " + opcode)
			return  ""
		if(commands[1] == "p" or commands[1] == "plus" or commands[1] == "+" or commands[1] == "add"):
			return ">"
		elif(commands[1] == "m" or commands[1] == "minus" or commands[1] == "-" or commands[1] == "sub"):
			return "<"
		else:
			print("Invalid ptr command " + commands[1])
	elif(commands[0] == "add"):
		return "+"
	elif(commands[0] == "sub"):
		return "-"
	elif (commands[0] == "{"):
		return "["
	elif (commands[0] == "}"):
		return "]"
	elif (commands[0] == "inp"):
		return ","
	elif (commands[0] == "out"):
		return "."
	return ""
program = open(input(".af(assemblyfuck) file: "), "r").read().split("\n")
mode = input("Do you want to compile or run? c/r ").lower()
while not mode in ["c", "r"]: 
	mode = input("Not valid! Do you want to compile or run? c/r ").lower()
bf = ""
for i in range(len(program)):
		bf += toBrain(program[i])
if mode == "c":
	print("Output: " + bf)
import bfinterp
if mode == "r":
	bfinterp.RunProgram(bf)
