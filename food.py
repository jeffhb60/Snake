from turtle import Turtle
import random

FOOD_SHAPE = "circle"
FOOD_COLOR = "red"
SPEED = "fastest"
SHAPESIZE_LEN = 1
SHAPESIZE_WID = 1
RAND_MIN = -280
RAND_MAX = 280

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=SHAPESIZE_LEN,stretch_wid=SHAPESIZE_WID)
        self.color(FOOD_COLOR)
        self.speed(SPEED)


    def refresh(self):
        random_x_coor = random.randint(RAND_MIN, RAND_MAX)
        random_y_coor = random.randint(RAND_MIN, RAND_MAX)
        self.goto(random_x_coor, random_y_coor)