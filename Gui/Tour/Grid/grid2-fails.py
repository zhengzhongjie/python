__author__ = 'zhongjie'
from tkinter import *
from grid2 import gridbox, packbox

root = Tk()
frm = Frame(root)
frm.pack()

gridbox(frm)
packbox(root)
Button(root, text='Quit', command=root.quit).pack()
mainloop()