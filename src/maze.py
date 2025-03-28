from time import sleep
from window import *
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
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
        if seed is not None:
            random.seed(seed)
        self._cells = []
        self._create_cells()
        self._break_walls_r(0,0)
        self._break_entrance_and_exit()
        self._reset_cells_visited()
        
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

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def _break_entrance_and_exit(self):
        start_cell = self._cells[0][0]
        end_cell = self._cells[-1][-1]
        start_cell.has_top_wall = False
        end_cell.has_bottom_wall = False
        self._draw_cell(start_cell)
        self._draw_cell(end_cell)

    #i is columns, j is rows
    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            to_visit = []
        
            # Check all four directions (with boundary checks)
            # Up (decrease row)
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1, "up"))
            # Right (increase column)
            if i < self.num_cols-1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j, "right"))
            # Down (increase row)
            if j < self.num_rows-1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1, "down"))
            # Left (decrease column)
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j, "left"))
        
            # If no unvisited neighbors, we're done with this cell
            if len(to_visit) == 0:
                return
            # Choose random direction from valid options
            next_i, next_j, direction = random.choice(to_visit)
        
            # Break walls based on chosen direction
            if direction == "up":
                current.has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif direction == "right":
                current.has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            elif direction == "down":
                current.has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            elif direction == "left":
                current.has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            
            # Draw the cells to show the wall being broken
            self._draw_cell(current)
            self._draw_cell(self._cells[next_i][next_j])
        
            # Recursively visit the next cell
            self._break_walls_r(next_i, next_j)


    def solve(self):
        start_time = time.time()
        success = self._solve_r(0, 0)
        elapsed_time = time.time() - start_time
        print(f"Maze solved in {elapsed_time:.4f} seconds with success code: {success}")

    #i is columns, j is rows
    def _solve_r(self, i=0, j=0):
        self._animate()
        current = self._cells[i][j]
        end_cell = self._cells[-1][-1]
        current.visited = True
        if current == end_cell:
            return True
        #set for right-hand bias
        # Right (increase column)
        if i < self.num_cols-1 and not self._cells[i+1][j].visited and current.has_right_wall == False:
            current.draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j) == True:
                return True
            else:
                current.draw_move(self._cells[i+1][j], True)

        # Down (increase row)
        if j < self.num_rows-1 and not self._cells[i][j+1].visited and current.has_bottom_wall == False:
            current.draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1) == True:
                return True
            else:
                current.draw_move(self._cells[i][j+1], True)

        # Left (decrease column)
        if i > 0 and not self._cells[i-1][j].visited and current.has_left_wall == False:
            current.draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j) == True:
                return True
            else:
                current.draw_move(self._cells[i-1][j], True)

        # #Up (decrease row)
        if j > 0 and not self._cells[i][j-1].visited and current.has_top_wall == False:
            current.draw_move(self._cells[i][j-1], True)
            if self._solve_r(i, j-1) == True:
                return True
            else:
                current.draw_move(self._cells[i][j-1], True)

        return False
