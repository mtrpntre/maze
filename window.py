from tkinter import Tk, BOTH, Canvas
from point import *

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.configure(background="white")
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
        
