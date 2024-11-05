from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.goto(x=random.randrange(-280, 280, 20), y=random.randrange(-280, 280, 20))
        self.score = 1

    def food_relocator(self):
        self.hideturtle()
        self.goto(x=random.randrange(-280, 280, 20), y=random.randrange(-280, 280, 20))
        self.showturtle()
