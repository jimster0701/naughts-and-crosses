import tkinter
import tkinter.messagebox
import os
import random

class naughtsAndCrosses:
    root = tkinter.Tk()

    def buttonPressed(place):
        self = naughtsAndCrosses
        print(self.grid)
        self.grid[place] = self.gridNumber(self.turn)
        print(self.grid)
        if self.images["images"]:
            self.buttons[place].config(image=self.images[self.turn])
        else:
            self.buttons[place].config(text=self.turnChar(self.turn))
        self.turn = self.nextTurn(self.turn)
        self.text.config(text="naughts score: "+str(self.score[0])+
            "\ncrosses score: "+str(self.score[1])+"\n"+self.turn+"s turn")

    path = lambda path: os.path.join(os.path.abspath("."), path)
    turnChar = lambda turn: {"naught":"O", "cross":"X"}[turn]
    nextTurn = lambda turn: {"naught":"cross", "cross":"naught"}[turn]
    randomTurn = lambda: random.choice(["cross", "naught"])
    gridNumber = lambda turn: {"naught":-1, "cross":1}[turn]

    try:
        images = {"naught":tkinter.PhotoImage(file=path("assets/naught.gif")),
            "cross":tkinter.PhotoImage(file=path("assets/cross.gif")),
            "none":tkinter.PhotoImage(), "images":True}
    except Exception as e:
        images = {"none":tkinter.PhotoImage(), "images":False}
        print(e, "\nAn error has occoured loading the image files.\nText will be used instead.")
    try:
        root.iconbitmap(path("assets/icon.ico"))
    except Exception as e:
        print(e)

    root.title("Naughts and Crosses")
    root.geometry("330x378")
    root.resizable(False, False)

    turn = randomTurn()
    score = [0]*2
    grid = [0]*9

    text = tkinter.Label(text="naughts score: "+str(score[0])+"\ncrosses score: "+str(score[1])+"\n"+turn+"s turn")
    mainGrid = tkinter.Frame()
    text.pack()
    mainGrid.pack()

    buttons = []
    for column in range(3):
        for row in range(3):
            if images["images"]:
                buttons.append(tkinter.Button(mainGrid, image=images["none"], height=100, width=100))
            else:
                buttons.append(tkinter.Button(mainGrid, text=" ", image=images["none"], height=100, width=100, compound="center"))
            buttons[(column*3)+row].config(command=lambda arg=(column*3)+row: naughtsAndCrosses.buttonPressed(arg))
            buttons[(column*3)+row].grid(column=column, row=row)

naughtsAndCrosses.root.mainloop()
