import os, sys
print('Runing in: ', os.getcwd())

from Tools.find import findlist
mydir = os.path.dirname(findlist('PyFtpGui.pyw', startdir=os.curdir)[0])

if sys.platform[:3] == 'win':
	os.system('start %s\getfilegui.py' % mydir)
	os.system('start %s\putfilegui.py' % mydir)
else:
	os.system('python %s/getfilegui.py' % mydir)
	os.system('python %s/putfilegui.py' % mydir)