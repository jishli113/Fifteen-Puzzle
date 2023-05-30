

from tkinter import *
import fifteen
import sys

import tkinter.font as font

global labels
global buttons

def swap(event):
    global zeropos
    print(board.tiles.getDict()[event].getId())
    if board.update(board.tiles.getDict()[event].getId()):
        for i in labels:
            print(i.get())
        print(event)
        print(zeropos)
        print(board.tiles.getDict()[zeropos + 1].getId())
        labels[zeropos].set(str(board.tiles.getDict()[zeropos + 1].getId()))
        print(labels[zeropos].get())
        labels[event-1].set(" ")
        # print(labels[zeropos].get())
        # print(labels[event].get())
        buttons[zeropos].config(text=labels[zeropos].get())
        buttons[event-1].config(text="")
        zeropos = event-1
        if board.is_solved():
            win = Tk()
            canvas = Canvas(win, width = 500, height = 500)
            canvas.create_text(250, 250, text="The puzzle is completed!", font ='Helvetica 15 bold')
            canvas.pack()
            win.mainloop()
        updateboard()


def shuffle():
    global zeropos
    global labels
    global buttons
    board.shuffle()
    labels = []
    buttons = []
    for i in range(1, 5):
        for j in range(1, 5):
            text = StringVar(value=str(board.tiles.getDict()[(i - 1) * 4 + j].getId()))
            com = 4 * (i - 1) + j
            if board.tiles.getDict()[(i - 1) * 4 + j].getId() == 0:
                zeropos = (i - 1) * 4 + j - 1
                text.set("")
            labels.append(text)
            btn = Button(frame, text=text.get(), command=lambda x=com: swap(x))
            btn.bind(f"Button {4 * (i - 1) + j}")
            btn.grid(column=j - 1, row=i - 1, sticky="news")
            buttons.append(btn)
    # for i in labels:
    #     print(i.get())
    updateboard()


def updateboard():
    for i in range(1, 5):
        for j in range(1, 5):
            buttons[(i - 1) * 4 + j - 1].bind(f"Button {4 * (i - 1) + j}")
            buttons[(i-1)*4 + j - 1].grid(column=j - 1, row=i - 1, sticky="news")
    print(board)


if __name__ == "__main__":
    root = Tk()
    board = fifteen.Fifteen()
    frame = Frame(root)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    frame.grid(row=0, column=0, sticky="news")
    grid = Frame(frame)
    grid.grid(sticky="news", column=0, row=7, columnspan=2)
    frame.rowconfigure(7, weight=1)
    frame.columnconfigure(0, weight=1)
    labels = []
    buttons = []
    zeropos = 0
    for i in range(1, 5):
        for j in range(1, 5):
            text = StringVar(value=str(board.tiles.getDict()[(i-1)*4 + j].getId()))
            com = 4 * (i - 1) + j
            if board.tiles.getDict()[(i - 1) * 4 + j].getId() == 0:
                zeropos = (i - 1) * 4 + j - 1
                text.set("")
            labels.append(text)
            btn = Button(frame, text=text.get(), command=lambda x=com: swap(x))
            buttons.append(btn)
            btn.bind(f"Button {4 * (i - 1) + j}")
            btn.grid(column=j - 1, row=i - 1, sticky="news")
    shuffBtn = Button(frame, text="Shuffle", command=shuffle)
    shuffBtn.grid(column=0, row=6, sticky="news")
    print(board.is_solved())

    frame.columnconfigure(tuple(range(10)), weight=1)
    frame.rowconfigure(tuple(range(5)), weight=1)
    mainloop()
