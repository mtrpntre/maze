from window import *
from cell import *
from maze_class import *


def main():
    win = Window(800,600)
    maze1 = Maze(10,10,4, 4, 20, win,100)
    maze1._create_cells()
    
    win.wait_for_close()

if __name__ == "__main__":
    main()