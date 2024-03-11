from turtle import Turtle

FONT = ("Ariel", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.current_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.current_scoreboard()
    
    def current_scoreboard(self):
        self.write(f"Your score is: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font=FONT)
