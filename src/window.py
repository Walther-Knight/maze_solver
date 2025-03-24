from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #create tkinter root object and set title
        self.root = Tk()
        self.root.title("Amazing Maze Solver")
        #set up canvas and pack
        self.canvas = Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()
        #set run state flag
        self.run_state = False
        #prevent program from running after closing window
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.run_state = True
        while self.run_state:
            self.redraw()
    
    def close(self):
        self.run_state = False
