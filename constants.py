# Screen constants
SCREEN_WIDTH = 600  # Width of the game screen
SCREEN_HEIGHT = 600  # Height of the game screen
BG_COLOR = "black"  # Background color of the game
TITLE = "Project Scaling Invention: Snake Game"  # Title of the game window
COLLISION_TOLERANCE = 15  # Distance threshold for detecting collision with food
TAIL_COLLISION_TOLERANCE = 10  # Distance threshold for detecting collision with the snake's tail

# Food constants
FOOD_SHAPE = "circle"  # Shape of the food
FOOD_COLOR = "red"  # Color of the food
SPEED = "fastest"  # Speed of the turtle drawing the food
SHAPESIZE_LEN = 1  # Length of the food's shape size
SHAPESIZE_WID = 1  # Width of the food's shape size
RAND_MIN = -280  # Minimum x or y coordinate for random food placement
RAND_MAX = 280  # Maximum x or y coordinate for random food placement

# Scoreboard constants
FONT_COLOR = "white"  # Color of the scoreboard text
FONT_TYPE = "Courier New"  # Font type for the scoreboard
FONT_SIZE = 24  # Font size for the scoreboard text
FONT_WEIGHT = "bold"  # Font weight for the scoreboard
ALIGNMENT = "center"  # Alignment of the scoreboard text
POS_X = 0  # X-coordinate for the scoreboard position
POS_Y = 260  # Y-coordinate for the scoreboard position
GAME_OVER_X = 0  # X-coordinate for the "GAME OVER" text
GAME_OVER_Y = 0  # Y-coordinate for the "GAME OVER" text

# Snake constants
START_POS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake's segments
BODY_SHAPE = "square"  # Shape of each snake segment
BODY_COLOR = "white"  # Color of each snake segment
MOVE_DIST = 20  # Distance the snake moves in one step

# Direction constants
UP_DIR = 90  # Heading for moving upward
DOWN_DIR = 270  # Heading for moving downward
LEFT_DIR = 180  # Heading for moving left
RIGHT_DIR = 0  # Heading for moving right
