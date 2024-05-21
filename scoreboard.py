from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.score_text = "Score:"
        self.lives = 4
        self.lives_remaining = "Lives:"
        self.lose = "Out of Lives! You Lose!"
        self.win = "You Win!"
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-380, 200)
        self.write(self.lives_remaining, align="left", font=("Courier", 15, "normal"))
        self.goto(-300, 200)
        self.write(self.lives, align="left", font=("Courier", 15, "normal"))
        self.goto(310, 200)
        self.write(self.score_text, align="center", font=("Courier", 15, "normal"))
        self.goto(360, 200)
        self.write(self.score, align="center", font=("Courier", 15, "normal"))

    def update_score(self, points):
        self.score += points
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def you_lose(self):
        self.goto(0, 0)
        self.write(self.lose, align="center", font=("Courier", 30, "normal"))

    def you_win(self):
        self.goto(0, 0)
        self.write(self.win, align="center", font=("Courier", 30, "normal"))
