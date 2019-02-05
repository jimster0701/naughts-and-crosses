import tkinter
import tkinter.messagebox
import os
import sys
import random

class naughtsAndCrosses:
    root = tkinter.Tk()

    def buttonPressed(place):
        self = naughtsAndCrosses
        if self.grid[place]:
            return
        self.grid[place] = self.gridNumber(self.turn)

        if self.images["images"]:
            self.buttons[place].config(image=self.images[self.turn])
        else:
            self.buttons[place].config(text=self.turnChar(self.turn))

        hasWon = int(self.hasWon(self.grid))
        if hasWon:
            self.text.config(text="naughts score: "+str(self.score[0])+
            "\ncrosses score: "+str(self.score[1])+"\n")
            self.message(self.pluralTurn(self.turn)+" has won", self.pluralTurn(self.turn)+" has won")
            self.grid = [0]*9
            self.score[self.scoreIndex(self.turn)] += 1
            self.turn = self.randomTurn()
            for i in range(9):
                if self.images["images"]:
                    self.buttons[i].config(image=self.images["none"])
                else:
                    self.buttons[i].config(text=" ")
        else:
            self.turn = self.nextTurn(self.turn)
        self.text.config(text="naughts score: "+str(self.score[0])+
            "\ncrosses score: "+str(self.score[1])+"\n"+self.pluralTurn(self.turn)+" turn")

    def hasWon(grid):
        for i in range(3):
            tmp = grid[(i*3)] + grid[(i*3)+1] + grid[(i*3)+2]
            if tmp in [-3, 3]:
                return tmp/3
            tmp = grid[i] + grid[3+i] + grid[6+i]
            if tmp in [-3, 3]:
                return tmp/3
        for i in range(0,3,2):
            tmp = grid[0+i] + grid[4] + grid[8-i]
            if tmp in [-3, 3]:
                return tmp/3
        return 0

    def path(relativePath):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relativePath)
        return os.path.join(os.path.abspath("."), relativePath)
    
    turnChar = lambda turn: {"naught":"O", "cross":"X"}[turn]
    pluralTurn = lambda turn: {"naught":"naughts", "cross":"crosses"}[turn]
    scoreIndex = lambda turn: {"naught":0, "cross":1}[turn]
    nextTurn = lambda turn: {"naught":"cross", "cross":"naught"}[turn]
    randomTurn = lambda: random.choice(["cross", "naught"])
    gridNumber = lambda turn: {"naught":-1, "cross":1}[turn]
    message = lambda title, message: tkinter.messagebox.showinfo(title=title, message=message)

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
    root.resizable(False, False)
    root.geometry("330x375")

    turn = randomTurn()
    score = [0]*2
    grid = [0]*9

    text = tkinter.Label(text="naughts score: "+str(score[0])+"\ncrosses score: "+str(score[1])+"\n"+pluralTurn(turn)+" turn")
    mainGrid = tkinter.Frame()
    text.pack()
    mainGrid.pack()

    buttons = []
    for column in range(3):
        for row in range(3):
            buttons.append(tkinter.Button(mainGrid, image=images["none"],
                command=lambda arg=(column*3)+row: naughtsAndCrosses.buttonPressed(arg)))
            if images["images"]:
                buttons[(column*3)+row].config(height=100, width=100)
            else:
                buttons[(column*3)+row].config(text=" ", height=98, width=98, compound="center")
            buttons[(column*3)+row].grid(column=column, row=row)

naughtsAndCrosses.root.mainloop()
