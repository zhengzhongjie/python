def scanner(name, function):
	file = open(name, 'r')
	while True:
		line = file.readline()
		if not line: break
		function(line)
	file.close()

def scanner2(name, function):
	for line in open(name, 'r'):
		function(line)

def scanner3(name, function):
	list(map(function, open(name, 'r')))

def scanner4(name, function):
	[function(line) for line in open(name, 'r')]

def scanner5(name, function):
	list(function(line) for line in open(name, 'r'))