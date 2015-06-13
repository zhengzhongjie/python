__author__ = 'zhongjiezheng'
import _thread as thread, queue, os
from tkinter import Tk 
from Gui.Tools.guiStreams import GuiOutput
stdoutQueue = queue.Queue()

def produce(input):
	while True:
		line = input.readline()
		stdoutQueue.put(line)
		if not line: break

def consumer(output, root, term='<end>'):
	try:
		line = stdoutQueue.get(block=False)
	except queue.Empty:
		pass
	else:
		if not line:
			output.write(term)
			return
		output.write(line)
	root.after(250, lambda: consumer(output, root, term))

def redirectedGuiShellCmd(command, root):
	input  = os.popen(command, 'r')
	output = GuiOutput(root)
	thread.start_new_thread(produce, (input,))
	consumer(output, root)

if __name__ == '__main__':
	win = Tk()
	redirectedGuiShellCmd('python -u pip-nongui.py', win)
	win.mainloop()