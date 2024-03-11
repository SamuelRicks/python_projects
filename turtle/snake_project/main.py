from turtle import Turtle, Screen

from food import Food
from snake import Snake
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score =Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update()
    sleep(.1)
    snake.movement()
    
    # detection code for food intake
    if snake.head.distance(food) < 20:
        food.refresh()
        score.increase_score()
        snake.add_segment()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()
        


    

screen.exitonclick()