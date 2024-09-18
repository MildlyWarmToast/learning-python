from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.going_up = False
        self.going_down = False
        self.x_pos = 0
        self.y_pos = 0
        self.y_movement = 10
        self.x_movement = 10

    def bounce_y(self):
        self.y_movement *= -1

    def bounce_x(self):
        self.x_movement *= -1

    def movement(self):
        self.x_pos = self.xcor() + self.x_movement
        self.y_pos = self.ycor() + self.y_movement
        self.goto(self.x_pos, self.y_pos)

    def starting_pos(self):
        self.goto(0, 0)
        self.x_movement *= -1