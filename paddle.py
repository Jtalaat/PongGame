from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,goto):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(goto)

    def go_upR(self):
        newY = self.ycor()+20
        self.goto(self.xcor(),newY)

    def go_downR(self):
        newY = self.ycor()-20
        self.goto(self.xcor(),newY)
    def go_upL(self):
        newY = self.ycor()+20
        self.goto(self.xcor(),newY)

    def go_downL(self):
        newY = self.ycor()-20
        self.goto(self.xcor(),newY)