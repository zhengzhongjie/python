import os, sys
from tkinter import *
from PIL import Image, ImageTk

imgdir = 'images'
imgfile = 'florida-2009-1.jpg'
if len(sys.argv) > 1:
	imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
print(imgpath)
image = Image.open(imgpath)
imgobj = ImageTk.PhotoImage(image)
Label(win, image=imgobj).pack()
win.mainloop()
print(imgobj.width(), imgobj.height())