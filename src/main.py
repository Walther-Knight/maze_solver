from window import *
from maze import *

def main():

    win = Window(800, 600)

    maze_test = Maze(10, 10, 15, 20, 38, 38, win, seed=0)
    maze_test.solve()
    
    win.wait_for_close()

if __name__ == "__main__":
        main()