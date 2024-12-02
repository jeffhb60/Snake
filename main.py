import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen, Turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BG_COLOR = "black"
TITLE = "Project Scaling Invention: Snake Game"
COLLISION_TOLERANCE = 15


# Set up the screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title(TITLE)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

active_game = True
while active_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < COLLISION_TOLERANCE:
        food.refresh()
        scoreboard.increase_score()
        print("nom nom nom")

# Wait for user to click before exiting
screen.exitonclick()