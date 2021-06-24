from turtle import Turtle
import random as r
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape("square")
        self.shapesize()
        self.color("green")
        self.x_move= 10
        self.y_move= 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.move_speed *= 0.9
        self.x_move *= -1

    def reset_pos(self):
        self.move_speed = 0.1
        self.goto(0,0)