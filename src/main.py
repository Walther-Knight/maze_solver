from window import *

def main():

    win = Window(800, 600)

    p1 = Point(10, 10)
    p2 = Point(20, 20)
    p3 = Point(10, 20)
    p4 = Point(20, 30)
    test_cell = Cell(p1, p2, win.canvas, "black")
    test_cell2 = Cell(p3, p4, win.canvas, "black")
    test_cell.draw()
    test_cell2.draw()
    print(test_cell)
    test_cell.draw_move(test_cell2)
    
    win.wait_for_close()

if __name__ == "__main__":
        main()