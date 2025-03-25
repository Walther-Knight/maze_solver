from window import *
from maze import *

def main():

    win = Window(800, 600)

    maze_test = Maze(0, 0, 15, 20, 40, 40, win)
    
    win.wait_for_close()

if __name__ == "__main__":
        main()