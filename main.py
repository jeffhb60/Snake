import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
from constants import *  # Import all constants

# Set up the game screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)  # Set screen dimensions
screen.bgcolor(BG_COLOR)  # Set screen background color
screen.title(TITLE)  # Set screen title
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Initialize game components
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for keyboard inputs
screen.listen()
screen.onkey(snake.move_up, "Up")  # Bind "Up" key to move_up method
screen.onkey(snake.move_down, "Down")  # Bind "Down" key to move_down method
screen.onkey(snake.move_right, "Right")  # Bind "Right" key to move_right method
screen.onkey(snake.move_left, "Left")  # Bind "Left" key to move_left method

# Game loop
active_game = True
while active_game:
    screen.update()  # Refresh the screen
    time.sleep(0.1)  # Add delay for smooth movement
    snake.move()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < COLLISION_TOLERANCE:
        food.refresh()
        snake.grow()  # Grow the snake
        scoreboard.increase_score()  # Update the score

    # Detect collision with walls
    if (snake.head.xcor() > 280 or
        snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or
        snake.head.ycor() < -280):
        active_game = False

    # Detect collision with tail
    for segment in snake.body_segments:
        if (snake.head.distance(segment) < TAIL_COLLISION_TOLERANCE and
                segment != snake.head):
            active_game = False
            scoreboard.game_over()

# Display game over message
scoreboard.game_over()

# Wait for user to click before exiting
screen.exitonclick()
