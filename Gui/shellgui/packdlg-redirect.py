__author__ = 'zhongjiezheng'
from tkinter import *
from packdlg import runPackDialog
from Gui.Tools.guiStreams import redirectedGuiFunc

def runPackDialog_Wrapped():
	redirectedGuiFunc(runPackDialog)

if __name__ == '__main__':
	root = Tk()
	Button(root, text='pop', command=runPackDialog_Wrapped).pack(fill=X)
	root.mainloop()