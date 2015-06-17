import sys

def reader(F):
	tmp, sys.stdin = sys.stdin, F
	line = input()
	print(line)
	sys.stdin = tmp

reader( open('test-stream-modes.py') )
reader( open('test-stream-modes.py', 'rb') )

def writer(F):
	tmp, sys.stdout = sys.stdout, F
	print(99, 'spam')
	sys.stdout = tmp

writer( open('temp', 'w') )
print( open('temp', 'w') )

#writer( open('temp', 'wb') )
#writer( open('temp', 'w', 0) )