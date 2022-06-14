from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.x_cor = 10
        self.y_cor = 10

    def move(self):
        newX = self.xcor()+ self.x_cor
        newY = self.ycor()+ self.y_cor
        self.goto(newX,newY)

    def bounceY(self):
        self.y_cor *=-1

    def bounceX(self):
        self.x_cor *=-1

    def resetposition(self):
        self.goto(0,0)