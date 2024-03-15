from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, cordx, cordy):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(cordx,cordy)

    def move_up(self):
       changing_y =  self.ycor() + 10
       self.setposition(self.xcor(), changing_y)
       

    def move_down(self):    
        changing_y =  self.ycor() - 10
        self.setposition(self.xcor(), changing_y)
