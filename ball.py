from turtle import Turtle

class Ball(Turtle):

    def __init__(self, shape: str = "circle"):
        super().__init__(shape)
        self.penup()
        self.color("white")
        self.goto(0,0)
        self.speed_counter = 0.1
        self.x_pos = 15
        self.y_pos = 15



    def move(self):
        new_x = self.xcor() + self.x_pos
        new_y = self.ycor() + self.y_pos #Adjusted to move the ball to top-right corner 20, 14.74
        self.goto(new_x,new_y)


    def bounce_y(self):
        self.y_pos *= -1


    def bounce_x(self):
        self.x_pos *= -1
        self.speed_counter *= 0.9

    
    def reset_pos(self):
        self.goto(0,0)
        self.speed_counter = 0.1
        self.bounce_x()

