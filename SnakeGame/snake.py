from turtle import Turtle
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    segments = []

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.color('white')
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def grow(self):
        #add segment to snake
        self.add_segment(self.segments[-1].position()) #in python, using -1 as an index in a list points to the last element in the list


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
