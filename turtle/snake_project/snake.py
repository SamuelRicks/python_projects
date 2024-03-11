from turtle import Turtle
TURTLE_SIZE = 20
MOVE_DISTANCE = 20
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.intro_snake()
        self.head = self.segments[0]

    def intro_snake(self):
        for snake in STARTING_POSITION:
            self.create_segment(snake)
            
    def create_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)
        

    def add_segment(self):
        self.create_segment(self.segments[-1].position())
            

    def movement(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
    
    def up(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0 and self.head.heading() != 180:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 0 and self.head.heading() != 180:
            self.head.setheading(0)
        
