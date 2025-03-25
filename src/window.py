from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        #create tkinter root object and set title
        print(f"Generating Window of size {width} X {height}!")
        self.root = Tk()
        self.root.title("Amazing Maze Solver")
        #set up canvas and pack
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()
        #set run state flag
        self.run_state = False
        #prevent program from running after closing window
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.run_state = True
        print("Running Maze!")
        while self.run_state:
            self.redraw()
    
    def close(self):
        print("Exiting...")
        self.run_state = False

class Point:
    #sets and stores relative location of draw operations
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

class Line:
    def __init__(self, point1, point2):
        # Store as Point instances
        self.start_point = point1
        self.end_point = point2

    def draw(self, canvas, color):
        # Use the points directly in the draw method
        canvas.create_line(
            self.start_point.x, self.start_point.y,
            self.end_point.x, self.end_point.y,
            fill=color, width=2
        )

    def length(self):
        # Calculate the line's length using Point's distance_to method
        return self.start_point.distance_to(self.end_point)

    def midpoint(self):
        # Calculate and return the midpoint as a new Point
        mid_x = (self.start_point.x + self.end_point.x) / 2
        mid_y = (self.start_point.y + self.end_point.y) / 2
        return Point(mid_x, mid_y)

    def __str__(self):
        # String representation for debugging
        return f"Line from {self.start_point} to {self.end_point}, length: {self.length():.2f}"