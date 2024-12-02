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
TAIL_COLLISION_TOLERANCE = 10


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
        snake.grow()
        scoreboard.increase_score()

    if (snake.head.xcor() > 280 or
            snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or
             snake.head.ycor() < -280):
        active_game = False

    for segment in snake.body_segments:

        if (snake.head.distance(segment) < TAIL_COLLISION_TOLERANCE and
                segment != snake.head):
            active_game = False
            scoreboard.game_over()

scoreboard.game_over()
# Wait for user to click before exiting
screen.exitonclick()