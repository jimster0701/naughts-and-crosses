import tkinter
import tkinter.messagebox
import os
import random

class naughtsAndCrosses:
    root = tkinter.Tk()
    try:
        root.iconbitmap(os.path.join(os.path.abspath("."), "assets\icon.ico"))
    except Exception as e:
        print(e)
    root.title("Naughts and Crosses")
    root.geometry("330x375")
    root.resizable(False, False)

    text = tkinter.Label(text="-\n-\n-")#("Xs score: " + str(score[0])+"\nOs score: " + str(score[1])+"\n## turn"))
    grid = tkinter.Frame()
    text.pack()
    grid.pack()

    noImg = tkinter.PhotoImage()
    buttons = []
    for i in range(9):
        buttons.append(tkinter.Button(grid, image=noImg, height=100, width=100))
    

    # frame1.pack(expand=True)
    # frame2.pack(expand=False)
    # frame3.pack(expand=False)
    # frame4.pack(expand=False)
    buttons[0].grid(column=0, row=0)
    buttons[1].grid(column=0, row=1)
    buttons[2].grid(column=0, row=2)
    buttons[3].grid(column=1, row=0)
    buttons[4].grid(column=1, row=1)
    buttons[5].grid(column=1, row=2)
    buttons[6].grid(column=2, row=0)
    buttons[7].grid(column=2, row=1)
    buttons[8].grid(column=2, row=2)

naughtsAndCrosses.root.mainloop()
