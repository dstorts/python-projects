from tkinter import *
from tkinter import ttk


root = Tk()

gameTitleLabel = Label(root, text='Minesweeper')
gameTitleLabel.grid(row=0, column=0)
#gameTitleLabel.pack()

def Reveal(event):
    print("reveal")

def Flag(event):
    print("flag")

gameGrid = list() #define a new list to hold all the game tiles
for y in range(10):
    #root.columnconfigure(y, minsize=30)
    for x in range(10):
        #root.rowconfigure(x, minsize=30)
        currentcount = gameGrid.__len__()
        newTile = Label(root, text=currentcount, font=("Arial", 20), bg='gray')
        newTile.config(padx=10)
        newTile.bind('<Button-1>', Reveal)
        newTile.bind('<Button-3>', Flag)
        newTile.grid(row=y, column=x+1)
        gameGrid.append(newTile) #add the new tile to the game board list

root.geometry('650x400')
root.mainloop()