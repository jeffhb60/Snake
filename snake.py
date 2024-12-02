from turtle import Turtle
from constants import *  # Import snake constants

class Snake:
    def __init__(self):
        """Initialize the snake with predefined properties."""
        self.body_segments = []  # List to hold snake segments
        self.create_snake()  # Create initial snake body
        self.head = self.body_segments[0]  # Head of the snake

    def create_snake(self):
        """Create the initial snake body based on starting positions."""
        for snake_position in START_POS:
            self.add_body_segment(snake_position)

    def add_body_segment(self, position):
        """Add a new segment to the snake at the specified position."""
        new_body_segment = Turtle(shape=BODY_SHAPE)
        new_body_segment.color(BODY_COLOR)
        new_body_segment.penup()
        new_body_segment.goto(position)
        self.body_segments.append(new_body_segment)

    def grow(self):
        """Add a new segment to the snake's tail when it grows."""
        self.add_body_segment(self.body_segments[-1].position())

    def move(self):
        """Move the snake by updating each segment's position."""
        for body_segment_number in range(len(self.body_segments) - 1, 0, -1):
            new_x_coord = self.body_segments[body_segment_number - 1].xcor()
            new_y_coord = self.body_segments[body_segment_number - 1].ycor()
            self.body_segments[body_segment_number].goto(new_x_coord, new_y_coord)
        self.head.forward(MOVE_DIST)

    def move_up(self):
        """Change the snake's direction to up if not moving down."""
        if self.head.heading() != DOWN_DIR:
            self.head.setheading(UP_DIR)

    def move_down(self):
        """Change the snake's direction to down if not moving up."""
        if self.head.heading() != UP_DIR:
            self.head.setheading(DOWN_DIR)

    def move_left(self):
        """Change the snake's direction to left if not moving right."""
        if self.head.heading() != RIGHT_DIR:
            self.head.setheading(LEFT_DIR)

    def move_right(self):
        """Change the snake's direction to right if not moving left."""
        if self.head.heading() != LEFT_DIR:
            self.head.setheading(RIGHT_DIR)
