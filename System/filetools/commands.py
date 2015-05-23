#!/usr/local/bin/python
from sys import argv
from scanfile import *
class UnknowCommand(Exception): pass

def processLine(line):
	if line[0] == '*':
		print("Ms.", line[1:-1])
	elif line[0] == '+':
		print("Mr.", line[1:-1])
	else:
		raise UnknowCommand(line)
commands = {'*': 'Ms.', '+': 'Mr.'}
def processLine2(line):
	try:
		print(commands[line[0]], line[1:-1])
	except KeyError:
		raise UnknowCommand(line)

filename = 'data.txt'
if len(argv) == 2: filename = argv[1]
scanner5(filename, processLine2)