from turtle import Turtle
from constants import *

class Snake:
    def __init__(self):
        self.body_segments = []
        self.create_snake()
        self.head = self.body_segments[0]

    def create_snake(self):
        for snake_position in START_POS:
            self.add_body_segment(snake_position)

    def move(self):
        for body_segment_number in range(len(self.body_segments) - 1, 0, -1):
            new_x_coord = self.body_segments[body_segment_number - 1].xcor()
            new_y_coord = self.body_segments[body_segment_number - 1].ycor()
            self.body_segments[body_segment_number].goto(new_x_coord, new_y_coord)
        self.body_segments[0].forward(MOVE_DIST)

    def add_body_segment(self, position):
        new_body_segment = Turtle(shape=BODY_SHAPE)
        new_body_segment.color(BODY_COLOR)
        new_body_segment.penup()
        new_body_segment.goto(position)
        self.body_segments.append(new_body_segment)

    def grow(self):
        self.add_body_segment(self.body_segments[-1].position())

    def move_up(self):
        if self.head.heading() != DOWN_DIR:
            self.head.setheading(UP_DIR)

    def move_down(self):
        if self.head.heading() != UP_DIR:
            self.head.setheading(DOWN_DIR)

    def move_left(self):
        if self.head.heading() != RIGHT_DIR:
            self.head.setheading(LEFT_DIR)

    def move_right(self):
        if self.head.heading() != LEFT_DIR:
            self.head.setheading(RIGHT_DIR)
