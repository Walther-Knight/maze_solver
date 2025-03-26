from window import *
from maze import *

def main():

    win = Window(800, 600)

    maze_test = Maze(10, 10, 14, 19, 40, 40, win, seed=0)
    
    win.wait_for_close()

if __name__ == "__main__":
        main()