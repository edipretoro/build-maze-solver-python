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
