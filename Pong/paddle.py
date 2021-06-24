from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos):
        self.pos = pos
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setheading(90)
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_len=5)
        self.goto(pos,0)
        self.showturtle()

    def up(self):
        # self.forward(60)
        new_y = self.ycor() + 40
        self.goto(self.pos,new_y)

    def down(self):
        # self.backward(60)
        new_y = self.ycor() - 40
        self.goto(self.pos,new_y)

