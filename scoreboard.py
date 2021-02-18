from turtle import Turtle

FONT = ("Arial", 10, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        text_position = (0, 280)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(text_position)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, move=False, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        global FONT
        self.write("GAME OVER", align=ALIGNMENT, move=False, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



