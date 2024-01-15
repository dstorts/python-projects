from turtle import Turtle, Screen

tina = Turtle()
screen = Screen()

#define a function to be passed into the onkey event listener
def move_forward():
    tina.forward(5)

def move_backward():
    tina.backward(5)

def rotate_ccw():
    #0 heading is East, 90 is North
    tina.left(15)

def rotate_cw():
    tina.right(15)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_ccw)
screen.onkey(key="d", fun=rotate_cw)
#notice above, when you are passing a function as an argument, don't include the parenthesis
#parenthesis will make the function excute then and there in your code

screen.exitonclick()