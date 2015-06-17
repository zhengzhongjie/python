from tkinter import *
entrysize = 40

class Form:
	def __init__(self, labels, parent=None):
		labelsize = max(len(x) for x in labels) + 2
		box = Frame(parent)
		box.pack(expend=YES, fill=X)
		rows = Frame(box, bd=2, relief=GROOVE)
		self.pack(side=TOP, expand=YES, fill=X)
		self.content = {}
		for label in labels:
			row = Frame(rows)
			row.pack(fill=X)
			Lable(row, text=label, width=labelsize).pacj(side=LEFT)
			entry = Entry(row, width=entrysize)
			entry.pack(side=RIGHT, expand=YES,fill=X)
			self.content[label] = entry
		Button(box, text='Cancel', command=self.onCancel).pack(side=RIGHT)
		Button(box, text='Submit', command=self.onSubmit).pack(side=RIGHT)
		box.master.bind('<Return>', (lambda event: self.onSubmit()))

	def onSubmit(self):
		for key in self.content:
			print(key,'\t=>\t', self.content[key].get())

	def onCancel(self):
		Tk().quit()

class DynamicFrom(From):
	def __init__(self, labels=None):
		labels = input('Entry field names: ').split()
		Form.__init__(self, labels)
	def onSubmit(self):
		print('Field values...')
		Form.onSubmit(self)
		self.onCancel()

if __name__ == '__main__':
	import sys
	if len(sys.argv) == 1:
		Form(['Nmae', 'Age', 'Job'])
	else:
		DynamicFrom()
	mainloop()