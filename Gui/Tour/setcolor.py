from tkinter import *
from tkinter.colorchooser import askcolor
def setBgColor():
	(triple, hexstr) = askcolor()
	if hexstr:
		print(hexstr)
		push.config(bg=hexstr)

root = Tk()
push = Button(root, text='SetBackground Color', command=setBgColor)
push.config(heigh=3, font=('times', 20, 'bold'))
push.pack(expand=YES, fill=BOTH)
root.mainloop()