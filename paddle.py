from turtle import Turtle

positions = ((350, 0), (-350, 0))
paddles = []


class Paddle:
    def __init__(self):
        for pos in positions:
            paddle = Turtle("square")
            paddle.penup()
            paddle.color("white")
            paddle.turtlesize(stretch_wid=1, stretch_len=5)
            paddle.setheading(90)
            paddle.goto(pos)
            paddles.append(paddle)

    def return_list(self):
        return paddles

    def up_1(self):
        paddles[0].forward(20)

    def down_1(self):
        paddles[0].backward(20)

    def up_2(self):
        paddles[1].forward(20)

    def down_2(self):
        paddles[1].backward(20)
