from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.up()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def ricochet(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.ricochet()

    def speed_up(self):
        if self.x_move > 0:
            self.x_move += 3
        else:
            self.x_move -= 3

        if self.y_move > 0:
            self.y_move += 3
        else:
            self.y_move -= 3
