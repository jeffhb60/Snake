from turtle import Turtle
from constants import *  # Import scoreboard constants

class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the scoreboard with default score and properties."""
        super().__init__()
        self.score = 0  # Initialize the score
        self.goto(POS_X, POS_Y)  # Position the scoreboard
        self.color(FONT_COLOR)  # Set the font color
        self.update_scoreboard()  # Display the initial score
        self.hideturtle()  # Hide the turtle cursor

    def update_scoreboard(self):
        """Update the scoreboard display with the current score."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT_TYPE, FONT_SIZE, FONT_WEIGHT))

    def game_over(self):
        """Display the 'GAME OVER' message."""
        self.goto(GAME_OVER_X, GAME_OVER_Y)
        self.write("GAME OVER!", align=ALIGNMENT, font=(FONT_TYPE, FONT_SIZE, FONT_WEIGHT))

    def increase_score(self):
        """Increment the score and refresh the display."""
        self.clear()  # Clear the previous score
        self.score += 1  # Increment the score
        self.update_scoreboard()  # Update the scoreboard
