from turtle import Turtle
FONT_COLOR = "white"
FONT_TYPE= "Courier New"
FONT_SIZE = 24
FONT_WEIGHT = "bold"
ALIGNMENT="center"
POS_X = 0
POS_Y = 260
GAME_OVER_X=0
GAME_OVER_Y=0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(POS_X, POS_Y)
        self.color(FONT_COLOR)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT_TYPE,FONT_SIZE,FONT_WEIGHT))

    def game_over(self):
        self.goto(GAME_OVER_X,GAME_OVER_Y)
        self.write("GAME OVER!", align=ALIGNMENT, font=(FONT_TYPE,FONT_SIZE,FONT_WEIGHT))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT_TYPE, FONT_SIZE, FONT_WEIGHT))

