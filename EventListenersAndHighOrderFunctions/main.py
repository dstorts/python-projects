from turtle import Turtle, Screen

tina = Turtle()
screen = Screen()

#define a function to be passed into the onkey event listener
def move_forward():
    tina.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
#notice above, when you are passing a function as an argument, don't include the parenthesis
#parenthesis will make the function excute then and there in your code

screen.exitonclick()