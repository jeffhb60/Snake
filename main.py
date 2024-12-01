from turtle import Screen, Turtle

from numba.cuda import const

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BODY_SHAPE = "square"
BODY_COLOR = "white"
BG_COLOR = "black"
TITLE = "Project Scaling Invention: Snake Game"

# Set up the screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title(TITLE)

# Create and position the snake segments

start_pos = [(0,0), (-20,0), (-40,0)]

for pos in start_pos:
    new_seg = Turtle(shape=BODY_SHAPE)
    new_seg.color(BODY_COLOR)
    new_seg.goto(pos)

# Wait for user to click before exiting
screen.exitonclick()