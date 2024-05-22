from turtle import Turtle

MOVE = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.goto(position)


    def up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(),new_y)    

    def down(self):
        new_y = self.ycor() - MOVE
        self.goto(self.xcor(),new_y) 
