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


def draw_board():
    c.delete('all')  # clean all
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            index = str(board[BOARD_SIZE * i + j])
            if index != str(EMPTY_SQUARE):
                c.create_rectangle(j * SQUARE_SIZE, i * SQUARE_SIZE,
                                   j * SQUARE_SIZE + SQUARE_SIZE,
                                   i * SQUARE_SIZE + SQUARE_SIZE,
                                   fill='#43ABC9',
                                   outline='#FFFFFF')
                c.create_text(j * SQUARE_SIZE + SQUARE_SIZE / 2,
                              i * SQUARE_SIZE + SQUARE_SIZE / 2,
                              text=index,
                              font="Arial {} italic".format(int(SQUARE_SIZE / 4)),
                              fill='#FFFFFF')


board = list(range(1, EMPTY_SQUARE + 1))
correct_board = board[:]
shuffle(board)


def click(event):
    x, y = event.x, event.y
    x = x // SQUARE_SIZE
    y = y // SQUARE_SIZE
    board_index = x + (y * BOARD_SIZE)
    empty_index = get_empty_neighbor(board_index)
    board[board_index], board[empty_index] = board[empty_index], board[board_index]
    draw_board()
    if board == correct_board:
        show_victory_plate()


def get_empty_neighbor(index):
    empty_index = board.index(EMPTY_SQUARE)
    abs_value = abs(empty_index - index)
    if abs_value == BOARD_SIZE:
        return empty_index
    elif abs_value == 1:
        max_index = max(index, empty_index)
        if max_index % BOARD_SIZE != 0:
            return empty_index
    return index


def show_victory_plate():
    c.create_rectangle(SQUARE_SIZE / 5,
                       SQUARE_SIZE * BOARD_SIZE / 2 - 10 * BOARD_SIZE,
                       BOARD_SIZE * SQUARE_SIZE - SQUARE_SIZE / 5,
                       SQUARE_SIZE * BOARD_SIZE / 2 + 10 * BOARD_SIZE,
                       fill='#000000',
                       outline='#FFFFFF')
    c.create_text(SQUARE_SIZE * BOARD_SIZE / 2, SQUARE_SIZE * BOARD_SIZE / 1.9,
                  text="Win!", font="Helvetica {} bold".format(int(10 * BOARD_SIZE)), fill='#DC143C')


root.mainloop()
