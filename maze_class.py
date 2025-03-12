from cell import *
from window import *
import time
import random




class Maze:
    def __init__(self, x, y, num_rows, num_cols, cell_size, win=None, seed = None):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self.win = win
        self._cells = []
        self._entrance = None
        self._exit = None
        if seed:
            random.seed(seed)

        
    def _create_cells(self):
        for i in range(self.num_rows):
            self._cells.append([])
            for col in range(self.num_cols):
                self._cells[i].append(Cell(Point(self.x+self.cell_size*col, self.y+self.cell_size*i), self.cell_size, self.win))
        
        self._draw_cells()
        self._entrance = self._cells[0][0]
        self._exit = self._cells[self.num_rows-1][self.num_cols-1]
        self._break_entrance_and_exit()
        self._create_maze()
        self._reset_visited()
        self.solve()

    def _draw_cells(self):
        for row in self._cells:
            for cell in row:
                cell.draw()
                self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        self._entrance.walls["up"] = False
        self._exit.walls["down"] = False
        self._entrance.draw()
        self._exit.draw()

    def _break_wall(self, cell1, cell2):
        if cell1.left_top_corner.x == cell2.left_top_corner.x:
            if cell1.left_top_corner.y < cell2.left_top_corner.y:
                cell1.walls["down"] = False
                cell2.walls["up"] = False
            else:
                cell1.walls["up"] = False
                cell2.walls["down"] = False
        else:
            if cell1.left_top_corner.x < cell2.left_top_corner.x:
                cell1.walls["right"] = False
                cell2.walls["left"] = False
            else:
                cell1.walls["left"] = False
                cell2.walls["right"] = False
        cell1.draw()
        cell2.draw()
        self._animate()
        
    def _get_neighbours(self, cell):
        neighbours = []
        row = int((cell.left_top_corner.y - self.y) / self.cell_size)
        col = int((cell.left_top_corner.x - self.x) / self.cell_size)
        if row > 0:
            neighbours.append(self._cells[row-1][col])
        if row < self.num_rows-1:
            neighbours.append(self._cells[row+1][col])
        if col > 0:
            neighbours.append(self._cells[row][col-1])
        if col < self.num_cols-1:
            neighbours.append(self._cells[row][col+1])
        return neighbours
    
    
    def _create_maze(self):
        stack = []
        current = self._cells[0][0]
        current.visited = True
        stack.append(current)
        while stack:
            self._animate()
            current = stack[-1]
            neighbours = [cell for cell in self._get_neighbours(current) if not cell.visited]
            if neighbours:
                next_cell = random.choice(neighbours)
                self._break_wall(current, next_cell)
                next_cell.visited = True
                stack.append(next_cell)
            else:
                stack.pop()

    def _reset_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

   

    def solve(self):
        stack = []
        current = self._entrance
        current.visited = True
        stack.append(current)
        while stack:
            self._animate()
            current = stack[-1]
            print(f"Current cell: ({current.left_top_corner.x}, {current.left_top_corner.y})")  # Debug
            if current == self._exit:
                print("Exit found!")  # Debug
                break
            next_cell = self._get_next_cell_to_visit(current)
            print(next_cell)
            if next_cell:
                print(f"Moving to cell: ({next_cell.left_top_corner.x}, {next_cell.left_top_corner.y})")  # Debug
                next_cell.visited = True
                stack.append(next_cell)
                current.draw_move(next_cell)
            else:
                print("Backtracking...")  # Debug
                stack.pop()
                if stack:
                    current.draw_move(stack[-1], undo=True)
        self._reset_visited()


    def _get_next_cell_to_visit(self, cell):
        row = int((cell.left_top_corner.y - self.y) / self.cell_size)
        col = int((cell.left_top_corner.x - self.x) / self.cell_size)
        print(f"Checking cell at ({cell.left_top_corner.x}, {cell.left_top_corner.y})")  # Debug
        if row > 0 and not cell.walls["up"] and not self._cells[row-1][col].visited:
            print(f"Up cell available at ({self._cells[row-1][col].left_top_corner.x}, {self._cells[row-1][col].left_top_corner.y})")  # Debug
            return self._cells[row-1][col]
        if row < self.num_rows-1 and not cell.walls["down"] and not self._cells[row+1][col].visited:
            print(f"Down cell available at ({self._cells[row+1][col].left_top_corner.x}, {self._cells[row+1][col].left_top_corner.y})")  # Debug
            return self._cells[row+1][col]
        if col > 0 and not cell.walls["left"] and not self._cells[row][col-1].visited:
            print(f"Left cell available at ({self._cells[row][col-1].left_top_corner.x}, {self._cells[row][col-1].left_top_corner.y})")  # Debug
            return self._cells[row][col-1]
        if col < self.num_cols-1 and not cell.walls["right"] and not self._cells[row][col+1].visited:
            print(f"Right cell available at ({self._cells[row][col+1].left_top_corner.x}, {self._cells[row][col+1].left_top_corner.y})")  # Debug
            return self._cells[row][col+1]
        print("No available cells to visit")  # Debug
        return None

