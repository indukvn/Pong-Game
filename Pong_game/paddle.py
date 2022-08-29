from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        y_pos = self.ycor() + 30
        self.goto(x=self.xcor(), y=y_pos)

    def go_down(self):
        y_pos = self.ycor() - 30
        self.goto(x=self.xcor(), y=y_pos)
