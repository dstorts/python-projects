from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,start_position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.up()
        self.goto(start_position)
        self.column = start_position[0]

    def go_up(self):
        self.goto(self.column, self.ycor()+30)

    def go_down(self):
        self.goto(self.column, self.ycor()-30)