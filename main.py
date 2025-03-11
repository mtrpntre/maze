from window import *
from cell import *

def main():
    win = Window(800,600)
    cell1 = Cell(Point(100,100), 50, win)
    cell2 = Cell(Point(200,100), 50, win)
    cell1.draw()
    cell2.draw()
    cell1.draw_move(cell2)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()