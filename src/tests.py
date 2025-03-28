import unittest
from maze import Maze
from window import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_maze_different_dimensions(self):
        num_cols = 5
        num_rows = 8
        m2 = Maze(0, 0, num_rows, num_cols, 15, 15)
        self.assertEqual(len(m2._cells), num_cols)
        self.assertEqual(len(m2._cells[0]), num_rows)
    
    def test_maze_properties(self):
        x1 = 5
        y1 = 10
        num_rows = 7
        num_cols = 6
        cell_x = 20
        cell_y = 25
        m = Maze(x1, y1, num_rows, num_cols, cell_x, cell_y)
        
        # Test that maze properties are stored correctly
        self.assertEqual(m.x1, x1)
        self.assertEqual(m.y1, y1)
        self.assertEqual(m.num_rows, num_rows)
        self.assertEqual(m.num_cols, num_cols)
        self.assertEqual(m.cell_size_x, cell_x)
        self.assertEqual(m.cell_size_y, cell_y)
    
    def test_cell_walls_initialization(self):
        num_cols = 3
        num_rows = 3
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
    
        # Recreate cells without breaking walls
        m._cells = []
        m._create_cells()

        # Check that all cells (except entrance and exit) have all walls by default
        for row_idx, row in enumerate(m._cells):
            for col_idx, cell in enumerate(row):
                # Skip entrance and exit cells
                if (row_idx == 0 and col_idx == 0) or (row_idx == num_rows-1 and col_idx == num_cols-1):
                    continue
                
                self.assertTrue(cell.has_left_wall)
                self.assertTrue(cell.has_right_wall)
                self.assertTrue(cell.has_top_wall)
                self.assertTrue(cell.has_bottom_wall)

            
    def test_cell_positions(self):
        # Test that cells are positioned correctly using simpler values
        x1 = 0
        y1 = 0
        num_rows = 2
        num_cols = 2
        cell_size_x = 5
        cell_size_y = 5
        m = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y)
    
        # Check first cell (top-left)
        cell_0_0 = m._cells[0][0]
        self.assertEqual(cell_0_0.boundaries["top_left"].x, 0)
        self.assertEqual(cell_0_0.boundaries["top_left"].y, 0)
        self.assertEqual(cell_0_0.boundaries["bottom_right"].x, 5)
        self.assertEqual(cell_0_0.boundaries["bottom_right"].y, 5)
    
        # Check second cell (to the right of first)
        cell_1_0 = m._cells[1][0]
        self.assertEqual(cell_1_0.boundaries["top_left"].x, 5)
        self.assertEqual(cell_1_0.boundaries["top_left"].y, 0)
        self.assertEqual(cell_1_0.boundaries["bottom_right"].x, 10)
        self.assertEqual(cell_1_0.boundaries["bottom_right"].y, 5)
    
        # Check third cell (below first)
        cell_0_1 = m._cells[0][1]
        self.assertEqual(cell_0_1.boundaries["top_left"].x, 0)
        self.assertEqual(cell_0_1.boundaries["top_left"].y, 5)
        self.assertEqual(cell_0_1.boundaries["bottom_right"].x, 5)
        self.assertEqual(cell_0_1.boundaries["bottom_right"].y, 10)
    
        # Check fourth cell (bottom-right)
        cell_1_1 = m._cells[1][1]
        self.assertEqual(cell_1_1.boundaries["top_left"].x, 5)
        self.assertEqual(cell_1_1.boundaries["top_left"].y, 5)
        self.assertEqual(cell_1_1.boundaries["bottom_right"].x, 10)
        self.assertEqual(cell_1_1.boundaries["bottom_right"].y, 10)
    
        # Now test with non-zero starting position and different cell size
        x1 = 10
        y1 = 20
        cell_size_x = 15
        cell_size_y = 25
        m2 = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y)
    
        # Check first cell with new parameters
        cell2_0_0 = m2._cells[0][0]
        self.assertEqual(cell2_0_0.boundaries["top_left"].x, 10)
        self.assertEqual(cell2_0_0.boundaries["top_left"].y, 20)
        self.assertEqual(cell2_0_0.boundaries["bottom_right"].x, 25)  # 10 + 15
        self.assertEqual(cell2_0_0.boundaries["bottom_right"].y, 45)  # 20 + 25



    def test_edge_cases(self):
        # Test 1x1 maze (smallest possible)
        m_small = Maze(0, 0, 1, 1, 10, 10)
        self.assertEqual(len(m_small._cells), 1)
        self.assertEqual(len(m_small._cells[0]), 1)
    
        # Test large maze
        rows = 25
        cols = 30
        m_large = Maze(0, 0, rows, cols, 5, 5)
        self.assertEqual(len(m_large._cells), cols)
        self.assertEqual(len(m_large._cells[0]), rows)

    def test_reset_visited_flags(self):
        num_rows = 3
        num_cols = 3
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
    
        # Mark some cells as visited
        m._cells[0][0].visited = True
        m._cells[1][1].visited = True
    
        # Reset all visited flags
        m._reset_cells_visited()
    
        # Verify all cells are now marked as not visited
        for col in m._cells:
            for cell in col:
                self.assertFalse(cell.visited)

    def test_entrance_exit(self):
        num_rows = 5
        num_cols = 5
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
    
        # Entry point should have no top wall (already broken in __init__)
        self.assertFalse(m._cells[0][0].has_top_wall)
    
        # Exit point should have no bottom wall (already broken in __init__)
        self.assertFalse(m._cells[num_cols-1][num_rows-1].has_bottom_wall)

if __name__ == "__main__":
    unittest.main()
