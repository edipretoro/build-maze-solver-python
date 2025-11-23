from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(700, 500)
    line = Line(p1, p2)
    win.draw_line(line, fill_color="blue", width=4)
    win.wait_for_close()


if __name__ == "__main__":
    main()
