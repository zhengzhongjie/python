from tkinter import *
from launchmodes import PortableLauncher
demoModules = ['DemoDlg', 'demoCheck', 'demoRadio', 'demo-Scale']

for demo in demoModules:
	PortableLauncher(demo, demo+'.py')()

root = Tk()
root.title('Processes')
Label(root, text='Multiple program demo:command lines', bg='white').pack()
root.mainloop()