from cell import *
from window import *
import time




class maze:
    def __init__(self, x, y, num_rows, num_cols, cell_size, win):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self.win = win
        self._cells = []
        
    def _create_cells(self):
        for i in range(self.num_rows):
            self._cells.append([])
            for col in range(self.num_cols):
                self._cells[i].append(Cell(Point(self.x+self.cell_size*col, self.y+self.cell_size*i), self.cell_size, self.win))
        
        self._draw_cells()
    def _draw_cells(self):
        for row in self._cells:
            for cell in row:
                cell.draw()
                self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    