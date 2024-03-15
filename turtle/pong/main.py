from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

#The screen settings 
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

#scoreboard
scoreboard = Scoreboard()

#The paddle
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

#ball
ball = Ball()

#Screen listening events
screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

#Game variables
game_on = True
while game_on:
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() > -325:
        ball.bounce_x()

    #detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

    #detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()

screen.exitonclick()