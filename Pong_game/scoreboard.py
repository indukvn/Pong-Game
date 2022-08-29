from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.miss = 0

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def result(self):
        if self.l_score > self.r_score:
            self.goto(0, -40)
            self.write(f"Left Player scored {self.l_score} and Won the game", align="center",
                       font=("Courier", 20, "normal"))
        else:
            self.goto(0, -40)
            self.write(f"Right Player scored {self.r_score} and Won the game", align="center",
                       font=("Courier", 20, "normal"))
