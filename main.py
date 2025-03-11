from window import *

def main():
    win = Window(800,600)
    win.draw_line(Line(Point(0,0), Point(800,600)), "red")
    win.draw_line(Line(Point(0,600), Point(800,0)), "blue")
    win.draw_line(Line(Point(0,300), Point(800,300)), "green")
    win.wait_for_close()

if __name__ == "__main__":
    main()