import math
import turtle as t
import random as rand

tina = t.Turtle()
t.colormode(255)

def random_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

tina.shape("turtle")
tina.speed('fastest')

def draw_spriograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tina.color(random_color())
        tina.circle(100)
        tina.setheading(tina.heading() + gap_size)
        tina.circle(100)

draw_spriograph(5)
screen = t.Screen()
screen.exitonclick()
