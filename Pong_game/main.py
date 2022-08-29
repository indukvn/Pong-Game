from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=550)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-370, 0))

ball = Ball()
scoreboard = ScoreBoard()
scoreboard.update_score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_on = True
while is_on:
    time.sleep(ball.increase_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 255 or ball.ycor() < -250:
        ball.bounce_y()

    if ball.distance(r_paddle) < 40 and ball.xcor() > 330 or ball.distance(l_paddle) < 40 and ball.xcor() < -340:
        ball.bounce_x()

    if scoreboard.miss < 5:
        if ball.xcor() > 420:
            scoreboard.miss += 1
            ball.start()
            scoreboard.l_point()

        elif ball.xcor() < -420:
            scoreboard.miss += 1
            ball.start()
            scoreboard.r_point()
    else:
        scoreboard.result()
        is_on = False


screen.exitonclick()
