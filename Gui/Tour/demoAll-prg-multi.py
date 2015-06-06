from tkinter import *
from multiprocessing import Process
demoModules = ['DemoDlg', 'demoCheck', 'demoRadio', 'demo-Scale']

def runDemo(modname):
	module = __import__(modname)
	module.Demo().mainloop()

if __name__ == '__main__':
	for modname in demoModules:
		Process(target=runDemo, args=(modname,)).start()

	root = Tk()
	root.title('Processes')
	Label(root, text='Multiple program demo: multiprocessing', bg='white').pack()
	root.mainloop()