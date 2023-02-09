import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

tim = Paddle()
tim.goto(350, 0)
jim = Paddle()
jim.goto(-350, 0)
ball = Ball()
score = Scoreboard()

game_on = True
screen.onkey(fun=tim.move_up, key="Up")
screen.onkey(fun=tim.move_down, key="Down")
screen.onkey(fun=jim.move_up, key="w")
screen.onkey(fun=jim.move_down, key="s")

while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(tim) < 50 and ball.xcor() > 330 or ball.distance(jim) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
