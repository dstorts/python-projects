from turtle import Turtle
import random

class Food(Turtle):


    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        x = random.randrange(-280, 280)
        y = random.randrange(-280, 260)
        self.goto(x,y)

    def refresh(self):
        x = random.randrange(-280, 280)
        y = random.randrange(-280, 260)
        self.goto(x, y)