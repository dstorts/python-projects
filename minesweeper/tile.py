from tkinter import Button
import random

class Tile(Button):

    def __init__(self, txt):
        super().__init__()
        self.config(text=txt, font=("Arial",14))
        self.xcor = 0
        self.ycor = 0
        self.id = None
        self.bomb = False
        self.flagged = False
        self.revealed = False
        self.neighbor_bomb_count = 0
        self.bomb_text = "💣"
        self.flag_text = "🏴"