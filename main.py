from window import *
from cell import *
from maze_class import *


def main():
    win = Window(800,600)
    maze1 = maze(10,10,5, 5, 50, win)
    maze1._create_cells()
    
    win.wait_for_close()

if __name__ == "__main__":
    main()