__author__ = 'zhongjiezheng'
from tkinter import *
from Gui.Tools.guiStreams import redirectedGuiShellCmd

def launch():
	redirectedGuiShellCmd('python -u pip-nongui.py')

window = Tk()
Button(window, text='GO!', command=launch).pack()
window.mainloop()