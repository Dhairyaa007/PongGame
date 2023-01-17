from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

LEFT_POS = (-250, 0)
RIGHT_POS = (250, 0)

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("PONG GAME")
s.tracer(0)

r_paddle = Paddle(RIGHT_POS)
l_paddle = Paddle(LEFT_POS)
ball = Ball()
score = Score()

s.listen()
s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")

s.onkey(l_paddle.go_up, "w")
s.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 220 or ball.distance(l_paddle) < 50 and ball.xcor() < -220:
        ball.bounce_x()

    if ball.xcor() > 270:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -270:
        ball.reset_position()
        score.r_point()

s.exitonclick()
