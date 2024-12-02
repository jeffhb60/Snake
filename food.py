from turtle import Turtle
import random
from constants import *  # Import constants for food properties

class Food(Turtle):
    def __init__(self):
        """Initialize the food object with predefined properties."""
        super().__init__()
        self.shape(FOOD_SHAPE)  # Set the shape of the food
        self.penup()  # Disable drawing when moving
        self.shapesize(stretch_len=SHAPESIZE_LEN, stretch_wid=SHAPESIZE_WID)  # Set size of the food
        self.color(FOOD_COLOR)  # Set the color of the food
        self.speed(SPEED)  # Set the speed of the food

    def refresh(self):
        """Move the food to a random location within the game boundaries."""
        random_x_coor = random.randint(RAND_MIN, RAND_MAX)
        random_y_coor = random.randint(RAND_MIN, RAND_MAX)
        self.goto(random_x_coor, random_y_coor)
