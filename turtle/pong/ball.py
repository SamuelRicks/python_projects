from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setpos(0,0)
        self.x_move = 3
        self.y_move = 3


    def move(self):
        moving_x = self.xcor() + self.x_move
        moving_y = self.ycor() + self.y_move
        self.goto(moving_x, moving_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
    

    

    
        