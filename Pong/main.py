from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong Pong")
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

scoreboard = Scoreboard()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.ricochet()

    if ball.xcor() > 380:
        ball.reset_position()
        ball.speed_up()
        #left player gets a point
        scoreboard.l_goal()

    if ball.xcor() < -380:
        ball.reset_position()
        ball.speed_up()
        #right player gets a point
        scoreboard.r_goal()


screen.exitonclick()