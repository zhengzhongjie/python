import sys

def getreply():
	"""
	read a reply key from an interactive user
	even if stdin redirected to a file or pipe
	"""
	if sys.stdin.isatty():
		return input('?')
	else:
		if sys.platform[:3] == 'win':
			import msvcrt
			msvcrt.putch(b'?')
			key = msvcrt.getche()
			msvcrt.putch(b'\n')
			return key
		else:
			assert False, 'platform not supported'
			#linux?: open('/dev/tty').readline()[:-1]

def more(text, numlines=10):
	"""
	page numlines string to stdout
	"""
	lines = text.splitlines()
	while lines:
		chunk = lines[:numlines]
		lines = lines[numlines:]
		for line in chunk: print(line)
		if lines and getreply() not in ['y', 'Y']: break

if __name__ == '__main__':
	if len(sys.argv) == 1:
		more(sys.stdin.read())
	else:
		more(open(sys.argv[1]).read())