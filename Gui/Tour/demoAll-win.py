from tkinter import *
demoModules = ['DemoDlg', 'demoCheck', 'demoRadio', 'demo-Scale']

def makePopups(modnames):
	demoObjects = []
	for modname in demoModules:
		module = __import__(modname)
		window = Toplevel()
		demo = module.Demo(window)
		window.title(module.__name__)
		demoObjects.append(demo)
	return demoObjects

def allstates(demoObjects):
	for obj in demoObjects:
		if hasattr(obj, 'report'):
			print(obj.__module__, end= ' ')
			obj.report()

root = Tk()
root.title('Popups')
demos = makePopups(demoModules)
Label(root, text='Multiple Toplevel window demo', bg='white').pack()
Button(root, text='States', command=lambda: allstates(demos)).pack(fill=X)
root.mainloop()