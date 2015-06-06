import sys, math
from tkinter import *
from PIL.ImageTk import PhotoImage
from viewer_thumbs import makeThumbs, ViewOne

def viewer(imgdir, kind=Toplevel, cols=None):
	win = kind()
	win.title('Viewer: ' + imgdir)
	quit = Button(win, text='Quit', command=win.quit, bg='beige')
	quit.pack(fill=X, side=BOTTOM)
	thumbs = makeThumbs(imgdir)
	if not cols:
		cols = int(math.ceil(math.sqrt(len(thumbs))))

	savephotos = []
	while thumbs:
		thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
		row = Frame(win)
		row.pack(fill=BOTH)
		for (imgfile, imgobj) in thumbsrow:
			size = max(imgobj.size)
			photo = PhotoImage(imgobj)
			link = Button(row, image=photo)
			handler = lambda savefile=imgfile: ViewOne(imgdir,savefile)
			link.config(command=handler, width=size, height=size)
			link.pack(side=LEFT, expand=YES)
			savephotos.append(photo)
	return win, savephotos
if __name__ == '__main__':
	imgdir = (len(sys.argv) > 1 and sys.argv[1]) or 'images'
	main, save = viewer(imgdir, kind=Tk)
	main.mainloop()