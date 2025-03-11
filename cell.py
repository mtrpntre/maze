from point import *
from window import *
from tkinter import Tk, BOTH, Canvas

class Cell:
    def __init__(self, left_top_corner, width, window=None):
        self.left_top_corner = left_top_corner
        self.center = Point(left_top_corner.x + width / 2, left_top_corner.y + width / 2)
        self.width = width
        self.right_bottom_corner = Point(left_top_corner.x + width, left_top_corner.y + width)
        self.walls = [True, True, True, True]
        self.window = window
        

    def draw(self):
        x = self.left_top_corner.x
        y = self.left_top_corner.y
        w = self.width
        if self.walls[0]:
            self.window.draw_line(Line(Point(x, y), Point(x + w, y)), "black")
        if self.walls[1]:
            self.window.draw_line(Line(Point(x + w, y), Point(x + w, y + w)), "black")
        if self.walls[2]:
            self.window.draw_line(Line(Point(x + w, y + w), Point(x, y + w)), "black")
        if self.walls[3]:
            self.window.draw_line(Line(Point(x, y + w), Point(x, y)), "black")

    def draw_move(self, to_cell, undo=False):
        self.window.draw_line(Line(self.center, to_cell.center), "grey")
        if undo:
            self.window.draw_line(Line(self.center, to_cell.center), "red")