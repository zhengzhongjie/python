"""
find and delete all "*.pyc" bytecode files at and below the directory
name on the command-line; assumes a nooportable Unix-like find command-line
"""

import os, sys
rundir = sys.argv[1]
if sys.platform[:3] == 'win':
	findcmd = r'c:\cygwin64\bin\find %s -name "*.pyc" -print' % rundir
else:
	findcmd = 'find %s -name "*.pyc" -print' % rundir
print(findcmd)

count = 0
for fileline in os.popen(findcmd):
	count += 1
	print(fileline, end='')
	os.remove(fileline.rstrip())

print('Removed %d .pyc files' % count)