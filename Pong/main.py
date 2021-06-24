from turtle import Turtle,Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=850, height=600)
screen.bgcolor("#e1faff")
screen.title("•◘Pong◘•")


paddle1 = Paddle(-400)
screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")

paddle2 = Paddle(400)
screen.listen()
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

ball = Ball()
score = ScoreBoard()
score.update_board()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    # elif ball.xcor()>390 or ball.xcor()<-390:
    #     ball.bounce_x()

    if ball.distance(paddle1) < 50 and ball.xcor()<-350 or ball.distance(paddle2) < 50 and ball.xcor()>350:
        ball.bounce_x()

    elif ball.xcor()<-380:
        ball.reset_pos()
        score.scoreA()

    elif ball.xcor()>380:
        ball.reset_pos()
        score.scoreB()
    # if ball.distance(paddle2) < 50 and ball.xcor()>350:
    #     ball.bounce_x()
    # elif ball.xcor()>390:
    #     score.scoreB()








#     paddle1.goto(-400,300)
#     paddle1.goto(-400,-300)

screen.exitonclick()