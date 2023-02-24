from random import shuffle
from tkinter import Canvas, Tk

BOARD_SIZE = 4
SQUARE_SIZE = 80
EMPTY_SQUARE = BOARD_SIZE ** 2

root = Tk()
root.title("Fifteen")

c = Canvas(root, width=BOARD_SIZE * SQUARE_SIZE,
           height=BOARD_SIZE * SQUARE_SIZE, bg='#808080')
c.pack()

root.mainloop()
