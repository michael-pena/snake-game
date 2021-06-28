from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.get_high_score()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

        if self.score > self.high_score:
            file = open("high_score.txt", "w")
            file.write(str(self.score))
            file.close()

    def get_high_score(self):
        file = open("high_score.txt", "r")
        self.high_score = int(file.read())
        file.close()
