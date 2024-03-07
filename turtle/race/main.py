from turtle import Turtle, Screen, colormode
import random

colors = ["red", "green", "blue", "pink", "yellow", "purple"]
colormode(255)
screen = Screen()
turtle_player = []

user_input = screen.textinput(title="Turtle race", prompt="Please select the color you think will win: ")

for position in range(len(colors)):
    x_coordinate = -250
    y_coordinate = -150 +(50 * position)
    player = Turtle()
    player.color(f"{colors[position]}")
    player.shape("turtle")
    player.penup()
    player.goto(x_coordinate, y_coordinate)
    turtle_player.append(player)


if user_input:
    start_race = True

while start_race:
    for turtle in turtle_player:
        if turtle.xcor() > 300:
            if user_input == turtle.pencolor():
                print("You have guessed correctly! You win!")
            else:
                print("You lose")
            print(f"{turtle.pencolor()} has won the race")
            start_race = False
        turtle.forward(random.randint(0,10))



screen.exitonclick()