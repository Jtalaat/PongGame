from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

from score import ScoreBord

R_paddle = Paddle((380,0))
L_paddle = Paddle((-380,0))
ball = Ball()
score = ScoreBord()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Game")
screen.tracer(0)



screen.listen()
screen.onkeypress(R_paddle.go_upR,'Up')
screen.onkeypress(R_paddle.go_downR,'Down')

screen.onkeypress(L_paddle.go_upL,'w')
screen.onkeypress(L_paddle.go_downL,'s')

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounceY()
    
    if ball.distance(R_paddle)< 50 and ball.xcor() > 320 or ball.distance(L_paddle)< 50 and ball.xcor() < -320:
        ball.bounceX()
    
    if ball.xcor()>380:
        ball.resetposition()
        score.l_point()

    if ball.xcor()<-380 :
        ball.resetposition()
        score.r_point()


screen.exitonclick()