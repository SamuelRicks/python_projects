"""import colorgram

color_pallet = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_pallet = (r,g,b)
    color_pallet.append(new_pallet)
"""
"""
The above code was used to get the most common colors used in the image
once we received the values we used the information in a new list
"""

new_color_pallet = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), 
                    (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), 
                    (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (
                    81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]


from turtle import Turtle as t, colormode, Screen, screensize
import random
colormode(255)
timmy = t()
timmy.hideturtle()
timmy.penup()

def print_dots(num_dots):
    starting_x = -250
    starting_y = -250
    timmy.setpos(starting_x,starting_y)
    for dot in range(num_dots):
        if dot%10 == 0:
            starting_y += 50
            timmy.setpos(starting_x, starting_y)
        timmy.setheading(0)
        timmy.dot(30, random.choice(new_color_pallet))
        timmy.forward(50)

print_dots(100)


Screen().exitonclick()
