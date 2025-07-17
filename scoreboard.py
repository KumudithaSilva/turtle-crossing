from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
GAME_OVER_ALIGNMENT = "center"
GAME_OVER_FONT = ("Courier", 35, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_scoreboard()

    def increase_level(self):
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=GAME_OVER_ALIGNMENT, font=GAME_OVER_FONT)
