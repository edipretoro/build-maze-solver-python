from graphics import Window, Cell


def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.draw(0, 0)
    cell2 = Cell(win)
    cell2.draw(0, 20)
    cell3 = Cell(win)
    cell3.draw(20, 0)
    cell4 = Cell(win)
    cell4.draw(20, 20)
    win.wait_for_close()


if __name__ == "__main__":
    main()
