import os, sys
from tkinter import *
from PIL import Image, ImageTk

imgdir = 'images'
if len(sys.argv) > 1: imgdir = sys.argv[1]
imgfiles = os.listdir(imgdir)

main = Tk()
main.title('Viever')
quit = Button(main, text='Quit all', command=main.quit, font=('courier', 25))
quit.pack()
savephotos = []

for imgfile in imgfiles:
	imgpath = os.path.join(imgdir, imgfile)
	win = Toplevel()
	win.title(imgfile)
	try:
		image = Image.open(imgpath)
		imgobj = ImageTk.PhotoImage(image)
		Label(win, image=imgobj).pack()
		print(imgpath, imgobj.width(), imgobj.height())
		savephotos.append(imgobj)
	except:
		errmsg = 'skipping %s\n %s' % (imgfile, sys.exc_info()[1])
		Label(win, text=errmsg).pack()

main.mainloop()