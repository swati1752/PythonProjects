from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pencolor("green")
        self.penup()
        self.goto(0,-350)
        self.pensize(5)
        self.setheading(90)
        self.A = 0
        self.B = 0
        # for _ in range(14):
        #     self.down()
        #     self.forward(25)
        #     self.penup()
        #     self.forward(25)

    def update_board(self):
        self.clear()
        self.goto(-80,240)
        self.write(self.A,align="center",font= ("arial",40,"normal"))
        self.goto(80, 240)
        self.write(self.B, align="center", font=("arial", 40, "normal"))

    def scoreA(self):
        self.A +=1
        self.update_board()
    def scoreB(self):
        self.B +=1
        self.update_board()