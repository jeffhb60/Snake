from turtle import Turtle
START_POS = [(0,0), (-20,0), (-40, 0)]
BODY_SHAPE = "square"
BODY_COLOR = "white"
MOVE_DIST = 20

class Snake:
    def __init__(self):
        self.body_segments = []
        self.create_snake()

    def create_snake(self):
        for snake_position in START_POS:
            new_body_segment = Turtle(shape=BODY_SHAPE)
            new_body_segment.color(BODY_COLOR)
            new_body_segment.penup()
            new_body_segment.goto(snake_position)
            self.body_segments.append(new_body_segment)

    def move(self):
        for body_segment_number in range(len(self.body_segments) - 1, 0, -1):
            new_x_coord = self.body_segments[body_segment_number - 1].xcor()
            new_y_coord = self.body_segments[body_segment_number - 1].ycor()
            self.body_segments[body_segment_number].goto(new_x_coord, new_y_coord)
        self.body_segments[0].forward(MOVE_DIST)
