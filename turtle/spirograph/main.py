from turtle import Turtle, Screen, colormode
import random

colormode(255)
timmy = Turtle()
timmy.speed("fastest")
timmy.circle(100)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_composition = (r,g,b)
    return color_composition


def draw_spirograph(gap_space):
    for i in range(int(360/gap_space)):
        timmy.color(random_color())
        timmy.setheading(timmy.heading() + gap_space)
        timmy.circle(100)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()