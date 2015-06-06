from tkinter import *
from quitter import Quitter 
fields = 'Name', 'Job', 'pay'

def fetch(entries):
	for entry in entries:
		print('Input => "%s"' % entry.get())

def makeForm(root, fields):
	entries = []
	for field in fields:
		row = Frame(root)
		lab = Label(row, width=5, text=field)
		ent = Entry(row)
		row.pack(side=TOP, fill=X)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT, expand=YES, fill=X)
		entries.append(ent)
	return entries

if __name__ == '__main__':
	root = Tk()
	ents = makeForm(root, fields)
	root.bind('<Return>', (lambda event: fetch(ents)))
	Button(root, text='fetch', command=(lambda: fetch(ents))).pack(side=LEFT)
	Quitter(root).pack(side=RIGHT)
	root.mainloop()