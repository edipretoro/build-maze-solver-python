from tkinter import Tk, BOTH, Canvas


class Point():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y


class Line():
    def __init__(self, start: Point, end: Point):
        self.__start = start
        self.__end = end

    def draw(self, canvas: Canvas, color="black", width=2):
        canvas.create_line(self.__start._Point__x, self.__start._Point__y,
                           self.__end._Point__x, self.__end._Point__y,
                           fill=color, width=width)


class Window():
    def __init__(self, width=800, height=600):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color: str = "black", width: int = 2):
        line.draw(self.__canvas, color=fill_color, width=width)


class Cell():
    def __init__(self, window: Window):
        self.__win = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

    def draw(self, x: int, y: int):
        self.__x1 = x
        self.__y1 = y
        self.__x2 = x + 20
        self.__y2 = y + 20

        if self.has_top_wall:
            top_line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(top_line)

        if self.has_bottom_wall:
            bottom_line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(bottom_line)

        if self.has_left_wall:
            left_line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(left_line)

        if self.has_right_wall:
            right_line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(right_line)
