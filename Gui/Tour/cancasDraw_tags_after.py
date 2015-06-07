__author__ = 'zhongjie'
from tkinter import *
import canvasDraw_tags

class CanvasEventsDemo(canvasDraw_tags.CanvasEventDemo):
    def moveEm(self, tag, moremove):
        (diffx, diffy), moremove = moremove[0], moremove[1:]
        self.canvas.move(tag, diffx, diffy)
        if moremove:
            self.canvas.after(250, self.moveEm, tag, moremove)

    def moveInSquares(self, tag):
        allmoves = [(+20, 0), (0, +20), (-20, 0), (0, -20)] * 5
        self.moveEm(tag, allmoves)

if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()