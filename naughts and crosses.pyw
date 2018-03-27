import tkinter
import tkinter.messagebox
import os
import random

grid = [0,0,0,0,0,0,0,0,0]
score = [0,0]
turn = 1
root = tkinter.Tk()

def hasWon(a):
    b = [a[0]+a[1]+a[2], a[3]+a[4]+a[5], a[6]+a[7]+a[8], a[0]+a[3]+a[6], a[1]+a[4]+a[7], a[2]+a[5]+a[8], a[0]+a[4]+a[8], a[2]+a[4]+a[6]]
    if 3 in b:
        print("1 has won")
        return 1
    elif -3 in b:
        print("-1 has won")
        return -1
    else:
        print("no one has won")
        return 0

def reset():
    global grid
    for i in range(1,10):
        changeButton(i,"")
    grid = [0,0,0,0,0,0,0,0,0]
    
def resetText():
    global turn
    global score
    global label
    turn = random.choice([-1,1])
    if turn == 1:
        t = "X"
    else:
        t = "O"
    label.config(text=("X's score: " + str(score[0])+"\nO's score: " + str(score[1])+"\n"+t+"'s turn"))

def gameInfo():
    global label
    global turn
    global grid
    print(turn,"s turn")
    w = hasWon(grid)
    if turn == 1:
        t = "X"
    else:
        t = "O"
    if w == 1:
        score[0] = score[0] + 1
        resetText()
        print("X got a point")
        tkinter.messagebox.showinfo(title="X has won", message="X has won")
        reset()
    elif w == -1:
        score[1] = score[1] + 1
        resetText()
        print("O got a point")
        tkinter.messagebox.showinfo(title="O has won", message="O has won")
        reset()
    else:
        if not 0 in grid:
            resetText()
            print("no one won")
            tkinter.messagebox.showinfo(title="No one won", message="No one won")
            reset()
        else:
            turn = 0 - turn
            if turn == 1:
                t = "X"
            else:
                t = "O"
            label.config(text=("X's score: " + str(score[0])+"\nO's score: " + str(score[1])+"\n"+t+"'s turn"))

def changeButton(a,x):
    global turn
    if turn == 1:
        b = "X"
    else:
        b = "O"
    if not x == 0:
        b = x
    if a == 1:
        global button1
        button1.config(text=b)
    if a == 2:
        global button2
        button2.config(text=b)
    if a == 3:
        global button3
        button3.config(text=b)
    if a == 4:
        global button4
        button4.config(text=b)
    if a == 5:
        global button5
        button5.config(text=b)
    if a == 6:
        global button6
        button6.config(text=b)
    if a == 7:
        global button7
        button7.config(text=b)
    if a == 8:
        global button8
        button8.config(text=b)
    if a == 9:
        global button9
        button9.config(text=b)

def b1():
    global turn
    global grid
    global button1
    if grid[0] == 0:
        grid[0] = turn
        changeButton(1,0)
        gameInfo()

def b2():
    global turn
    global grid
    global label
    global button2
    if grid[1] == 0:
        grid[1] = turn
        changeButton(2,0)
        gameInfo()

def b3():
    global turn
    global grid
    global label
    global button3
    if grid[2] == 0:
        grid[2] = turn
        changeButton(3,0)
        gameInfo()

def b4():
    global turn
    global grid
    global label
    global button4
    if grid[3] == 0:
        grid[3] = turn
        changeButton(4,0)
        gameInfo()

def b5():
    global turn
    global grid
    global label
    global button5
    if grid[4] == 0:
        grid[4] = turn
        changeButton(5,0)
        gameInfo()

def b6():
    global turn
    global grid
    global label
    global button6
    if grid[5] == 0:
        grid[5] = turn
        changeButton(6,0)
        gameInfo()
    
def b7():
    global turn
    global grid
    global label
    global button7
    if grid[6] == 0:
        grid[6] = turn
        changeButton(7,0)
        gameInfo()

def b8():
    global turn
    global grid
    global label
    global button8
    if grid[7] == 0:
        grid[7] = turn
        changeButton(8,0)
        gameInfo()

def b9():
    global turn
    global grid
    global label
    global button9
    if grid[8] == 0:
        grid[8] = turn
        changeButton(9,0)
        gameInfo()

label = tkinter.Label(text=("X's score: " + str(score[0])+"\nO's score: " + str(score[1])+"\nX's turn"))
frame1 = tkinter.Frame(width=30, height=15)
frame2 = tkinter.Frame(frame1, width=30, height=5)
frame3 = tkinter.Frame(frame1, width=30, height=5)
frame4 = tkinter.Frame(frame1, width=30, height=5)
button1 = tkinter.Button(frame2, text="", command=b1, height = 5, width = 10)
button2 = tkinter.Button(frame2, text="", command=b2, height = 5, width = 10)
button3 = tkinter.Button(frame2, text="", command=b3, height = 5, width = 10)
button4 = tkinter.Button(frame3, text="", command=b4, height = 5, width = 10)
button5 = tkinter.Button(frame3, text="", command=b5, height = 5, width = 10)
button6 = tkinter.Button(frame3, text="", command=b6, height = 5, width = 10)
button7 = tkinter.Button(frame4, text="", command=b7, height = 5, width = 10)
button8 = tkinter.Button(frame4, text="", command=b8, height = 5, width = 10)
button9 = tkinter.Button(frame4, text="", command=b9, height = 5, width = 10)
label.pack()
frame1.pack(expand=False, side=tkinter.BOTTOM)
frame2.pack(expand=False)
frame3.pack(expand=False)
frame4.pack(expand=False)
button1.pack(side=tkinter.LEFT)
button2.pack(side=tkinter.LEFT)
button3.pack(side=tkinter.LEFT)
button4.pack(side=tkinter.LEFT)
button5.pack(side=tkinter.LEFT)
button6.pack(side=tkinter.LEFT)
button7.pack(side=tkinter.LEFT)
button8.pack(side=tkinter.LEFT)
button9.pack(side=tkinter.LEFT)

try:
    root.iconbitmap("assets/icon.ico")
except Exception as e:
    print(e)
root.title("Naughts and Crosses")
root.geometry("250x310")
root.resizable(False, False)
root.mainloop()
