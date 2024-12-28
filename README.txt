
   _____              _            
  / ____|            | |           
 | (___   _ __   __ _| | _____ _ __ 
  \___ \ | '_ \ / _` | |/ / _ \ '__|
  ____) || | | | (_| |   <  __/ |   
 |_____/ |_| |_|\__,_|_|\_\___|_|   


# Snake Game

This project is a classic Snake Game developed in Python using the `turtle` graphics library. The game includes essential elements like score tracking, movement controls, food spawning, and game-over detection. It provides an engaging experience similar to the traditional snake games, with easy-to-understand code and modular design, making it a fun and instructive project.

## Features

- **Snake Movement**: The snake can move in all four directions using the arrow keys.
- **Food Object**: Food spawns randomly within the game area, and the snake grows longer each time it consumes food.
- **Score Tracking**: A scoreboard at the top keeps track of the score, updating with each piece of food eaten.
- **Collision Detection**: The game detects collisions with walls and the snake's tail, triggering a game-over message and ending the game.

## File Structure

- **`main.py`**: This is the main game file where the game loop is handled. It initializes the game screen, listens for user inputs, and coordinates interactions between the snake, food, and scoreboard.
- **`snake.py`**: Defines the `Snake` class, which manages the snake's creation, movement, and growth.
- **`food.py`**: Defines the `Food` class, responsible for spawning food at random locations within the game area.
- **`scoreboard.py`**: Defines the `ScoreBoard` class, which displays and updates the player's score and displays a game-over message.

## Requirements

- Python 3.x
- `turtle` library (usually included with Python)

## How to Run

1. Clone or download this repository.
2. Run the `main.py` file in a Python environment:

   ```bash
   python main.py
   ```

3. Use the arrow keys to control the snake's movement.

## Game Controls

- **Up Arrow**: Move up
- **Down Arrow**: Move down
- **Left Arrow**: Move left
- **Right Arrow**: Move right

## Future Improvements

- Adding levels with increasing difficulty.
- Implementing a high score feature.
- Adding sounds for a more immersive experience.

## License

This project is open-source and available for use without a License.
