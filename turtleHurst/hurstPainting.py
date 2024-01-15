import random
import colorgram
import turtle as t

t.colormode(255)
tina = t.Turtle()

# colors = colorgram.extract('image.jpg', 20)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
# print(rgb_colors)

color_list = [(195, 167, 125), (154, 144, 48), (144, 110, 32), (236, 241, 236), (201, 200, 110), (95, 38, 21), (84, 124, 122), (81, 111, 143), (12, 38, 68), (88, 69, 77), (201, 144, 147), (179, 90, 89), (225, 226, 229), (34, 87, 84), (33, 85, 87), (228, 224, 226), (178, 91, 94), (90, 48, 41), (144, 166, 161)]
#dots, 20 wide, 50 apart, 10 by 10 grid
tina.shape("turtle")
tina.speed('fastest')
row_height = -200
tina.up()
tina.goto(-300,row_height)
tina.down()

for _ in range(10):
    for _ in range(10):
        tina.dot(20, random.choice(color_list))
        tina.up()
        tina.forward(50)
        tina.down()
    tina.up()
    row_height += 50
    tina.goto(-300, row_height)
    tina.down()

screen = t.Screen()
screen.exitonclick()