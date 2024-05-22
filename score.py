from turtle import Turtle

POSITION = ("Impact","45","normal")

class Scoreboard(Turtle):

    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.color("white")
        self.goto(position)
        self.write(f"{self.score}",align="center",font=POSITION)
        

    def score_update(self):
        self.score +=1
        self.clear()
        self.write(f"{self.score}",align="center",font=POSITION)

