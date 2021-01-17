from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,paddle_alignment):
        super().__init__()
        self.goto(paddle_alignment)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)

        self.penup()



    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


