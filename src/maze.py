from time import sleep
from window import *

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if self._win == None:
            self.canvas = None
        else:
            self.canvas = self._win.canvas
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        
    def _create_cells(self):
        for i in range(self.num_cols):
            rows = []
            self._cells.append(rows)
            for j in range(self.num_rows):
                p1 = Point(self.x1 + i * self.cell_size_x, self.y1 + j * self.cell_size_y)
                p2 = Point(self.x1 + (i+1) * self.cell_size_x, self.y1 + (j+1) * self.cell_size_y)
                cell = Cell(p1, p2, self.canvas, "black")
                self._draw_cell(cell)
                rows.append(cell)
    
    def _draw_cell(self, cell):
        if self._win is not None:
            cell.draw()
            self._animate()

    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            sleep(0.05)

    def _break_entrance_and_exit(self):
        start_cell = self._cells[0][0]
        end_cell = self._cells[-1][-1]
        start_cell.has_top_wall = False
        end_cell.has_bottom_wall = False
        self._draw_cell(start_cell)
        self._draw_cell(end_cell)