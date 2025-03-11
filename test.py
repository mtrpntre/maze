import unittest
from maze_class import *

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.win = Window(100,100)
        self.maze = Maze(0, 0, 2, 2, 10, self.win)

    def test_initialization(self):
        self.assertEqual(self.maze.x, 0)
        self.assertEqual(self.maze.y, 0)
        self.assertEqual(self.maze.num_rows, 2)
        self.assertEqual(self.maze.num_cols, 2)
        self.assertEqual(self.maze.cell_size, 10)
        self.assertEqual(self.maze.win, self.win)
        self.assertEqual(self.maze._cells, [])

    def test_create_cells(self):
        self.maze._create_cells()
        self.assertEqual(len(self.maze._cells), 2)
        self.assertEqual(len(self.maze._cells[0]), 2)
        self.assertIsInstance(self.maze._cells[0][0], Cell)
        self.assertIsInstance(self.maze._cells[0][1], Cell)
        self.assertIsInstance(self.maze._cells[1][0], Cell)
        self.assertIsInstance(self.maze._cells[1][1], Cell)

    def test_break_entrance_and_exit(self):
        self.maze._create_cells()
        self.maze._break_entrance_and_exit()
        self.assertFalse(self.maze._cells[0][0].walls["up"])
        self.assertFalse(self.maze._cells[1][1].walls["down"])
        


if __name__ == '__main__':
    unittest.main()