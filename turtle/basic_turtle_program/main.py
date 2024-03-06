from turtle import Turtle, Screen

tim = Turtle()

array1 = [3,4,5,6,7,8,9,10]
colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta", "purple"]


for i in range(len(array1)):
    color = colors[i]
    angle = 360/array1[i]
    moves = array1[i]
    for move in range(moves):
        tim.color(color)
        tim.rt(angle)
        tim.forward(100)

screen = Screen()
screen.exitonclick()