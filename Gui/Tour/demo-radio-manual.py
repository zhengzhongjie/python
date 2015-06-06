from tkinter import *
state = 0
buttons = []

def onPress(i):
	global state
	state = i 
	for btn in buttons:
		btn.deselect()
	buttons[i].select()

root = Tk()
for i in range(10):
	rad = Radiobutton(root, text=str(i),
							value=i,command=(lambda i=i: onPress(i)))
	rad.pack(side=LEFT)
	buttons.append(rad)

onPress(0)
root.mainloop()
print(state)