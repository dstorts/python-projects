from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

WIDTH=600
HEIGHT=600
GAME_BOUNDS = 280
SNAKE_BODY_WIDTH = 20

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title('Pythen Snek')
screen.tracer(0) #turn tracer off, prevents screen graphics update till screen.update() is called

my_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

def is_snake_ob():
    curr_x = my_snake.head.xcor()
    curr_y = my_snake.head.ycor()
    if curr_x > GAME_BOUNDS or curr_x < -GAME_BOUNDS or curr_y > GAME_BOUNDS-SNAKE_BODY_WIDTH or curr_y < -GAME_BOUNDS:
        #here if ob
        scoreboard.game_over()
        return True
    return False

game_is_on = True
while game_is_on and not is_snake_ob():
    screen.update()
    time.sleep(0.1)  # sleep for 1 second
    my_snake.move()
    #collision with food
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.grow()
        scoreboard.increase_score()
        print("nom, nom, nom")

    #detect if eating slef
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()