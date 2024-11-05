from turtle import Turtle

UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270


class Snake:

    def __init__(self):
        self.initial_coordinates = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.forward_dist = 20

    def create_snake(self):
        for position in self.initial_coordinates:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)

        self.segments[0].forward(self.forward_dist)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.shapesize(stretch_len=0.5, stretch_wid=0.5)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
