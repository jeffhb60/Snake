# Project Scaling-Invention: Snake Game
A classic Snake game built using Python's `turtle` module. The game includes features like snake movement, dynamic growth, collision detection, scoring, and game-over mechanics.

## Table of Contents
<ol>
    <li><a href="#features">Features</a></li>
    <li><a href="#gameplay-instructions">Gameplay Instructions</a></li>
    <li><a href="#file-structure">File Structure</a></li>
    <li>
      <a href="#code-overview">Code Overview</a>
        <ul><a href="#main-components">Main Components</a></ul>
        <ul><a href="#constants">Constants</a></ul>
    </li>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#how-to-run">How to Run</a></li>
    <li><a href="#future-improvments">Future Improvements</a></li>
</ol>

## Features
1. Snake Movement:
    * Controlled using arrow keys (`Up`, `Down`, `Left`, `Right`).
2. Food:
    * Randomly spawns on the screen.
    * Snake grows when it eats food.
3. Scoreboard:
    * Displays the current score at the top of the screen.
    * Displays "GAME OVER!" when the game ends.
4. Collision Detection:
    * Ends the game if the snake hits the screen boundaries or its own body.
5. Dynamic Growth:
    * Snake grows each time it eats food.

## Gameplay Instructions
1. Start the game by running the main.py file.
2. Use the arrow keys to control the snake's direction.
3. Eat the red food to increase your score.
4. Avoid colliding with the screen boundaries or the snake's own tail.

## File Structure
    ```
    .
    ├── main.py          # Entry point for the game
    ├── food.py          # Handles the food's appearance and behavior
    ├── snake.py         # Manages the snake's movement and growth
    ├── scoreboard.py    # Displays and updates the score
    ├── constants.py     # Centralized constants for the game
    └── README.md        # Game documentation
    
    ```
## Code Overview

### Main Components
1. `main.py`:
    * Initializes the game.
    * Listens for keyboard inputs.
    * Updates the screen and checks for collisions.
2. `food.py`:
    * Manages the food object, including random repositioning after consumption.
3. `snake.py`:
    * Handles the snake's creation, movement, direction changes, and growth.
4. `scoreboard.py`:
    * Displays the score and game-over message.
5. `constants.py`:
    * Stores all constants to ensure maintainability and ease of updates.

### Constants
1. Key constants are stored in `constants.py`:
2. Screen Dimensions: `SCREEN_WIDTH`, `SCREEN_HEIGHT`
3. Snake Properties: `BODY_SHAPE`, `BODY_COLOR`, `MOVE_DIST`
4. Food Properties: `FOOD_SHAPE`, `FOOD_COLOR`, `RAND_MIN`, `RAND_MAX`
5. Scoreboard Properties: `FONT_TYPE`, `ALIGNMENT`, `GAME_OVER_X`, `GAME_OVER_Y`

## Requirements
* Python 3.x
* `turtle` module (built-in with Python)


## How to Run
1. Clone the repository or download the source files.
2. Ensure `main.py`, `food.py`, `snake.py`, `scoreboard.py`, and `constants.py` are in the same directory.
3. Run the following command in your terrminal:
   * `python main.py`
5. Enjoy the game.

## Future Improvements
1. Restart Option:
    * Allow the user to restart the game after it ends.
2. High Score Tracking:
    * Save and display the highest score achieved.
3. Obstacles:
    * Add random obstacles to increase difficulty.
4. Levels:
    * Increase game speed as the score increases.
5. Sound Effects:
    * Add sounds for eating food and game-over events.
