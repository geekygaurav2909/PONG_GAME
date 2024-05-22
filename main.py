from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time


screen = Screen()

screen.title("The Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-380,0))
r_paddle = Paddle((380,0))
ball = Ball()

l_score = Scoreboard((-200,220))
r_score = Scoreboard((200,220))

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

is_game_on = True

while is_game_on:
    time.sleep(ball.speed_counter)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor()> 280 or ball.ycor() < -280:
        ball.bounce_y()


    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()


    #Detect if ball crosses the wall or misses the paddle
    if ball.xcor() > 380:
        l_score.score_update()
        ball.reset_pos()
    elif ball.xcor() < -380:
        r_score.score_update()
        ball.reset_pos()

    


    
        


screen.exitonclick()