from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
paddle = Paddle()
paddles = paddle.return_list()
ball = Ball()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.listen()
screen.onkeypress(key="w", fun=paddle.up_1)
screen.onkeypress(key="s", fun=paddle.down_1)
screen.onkeypress(key="Down", fun=paddle.down_2)
screen.onkeypress(key="Up", fun=paddle.up_2)

game_is_on = True
while game_is_on:
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    if ball.distance(paddles[0]) < 50 and ball.xcor() > 320 or ball.distance(paddles[1]) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.x_movement += 1
        ball.y_movement += 1
    if ball.xcor() >= 380:
        ball.starting_pos()
        scoreboard.l_point()
        scoreboard.update_board()
    if ball.xcor() <= -380:
        ball.starting_pos()
        scoreboard.r_point()
        scoreboard.update_board()

    ball.movement()
    time.sleep(0.1)
    screen.update()



screen.exitonclick()