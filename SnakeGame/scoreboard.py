from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 265)
        self.color('white')
        self.ht()
        self.score = 0
        self.update_score()
        self.goto(0,270)

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()