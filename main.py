import time
from turtle import Screen, Turtle

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
segs = []

for pos in start_pos:
    new_seg = Turtle(shape=BODY_SHAPE)
    new_seg.color(BODY_COLOR)
    new_seg.goto(pos)
    segs.append(new_seg)

active_game = True

while active_game:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(segs) - 1, 0, -1):
        new_x = segs[seg - 1].xcor()
        new_y = segs[seg - 1].ycor()
        segs[seg].goto(new_x, new_y)




# Wait for user to click before exiting
screen.exitonclick()