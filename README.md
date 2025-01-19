# Pong Game

## Overview
This is a simple Pong game implemented using Python and Pygame. It features two paddles (controlled by players), a ball that bounces around, and a scoring system. The game is played in a 1280x720 window.

## Features
- Two paddles: one for the player and one for the opponent.
- A ball that moves across the screen and bounces off the walls and paddles.
- Collision detection for paddles and walls.
- Scoring system displayed at the top of the screen.
- Dotted line in the center of the screen to divide the playfield.

## Controls
### Player 1 (Right Paddle):
- **Up Arrow (\u2191)**: Move the paddle up.
- **Down Arrow (\u2193)**: Move the paddle down.

### Player 2 (Left Paddle):
- **W**: Move the paddle up.
- **S**: Move the paddle down.

## How to Play
1. Run the script to start the game.
2. Use the controls above to move your paddle.
3. Prevent the ball from passing your paddle. If the ball passes the right paddle, the opponent scores, and vice versa.
4. First to reach the desired score wins (modify the code to set a win condition if needed).

## Installation and Requirements
### Prerequisites:
- Python 3.x
- Pygame library

### Installation:
1. Install Python: [Download Python](https://www.python.org/downloads/)
2. Install Pygame by running the following command in your terminal or command prompt:
   ```bash
   pip install pygame
   ```

### Running the Game:
1. Save the script as `pong.py`.
2. Run the script:
   ```bash
   python pong.py
   ```

## Code Breakdown
### Key Components:
1. **Screen Setup**:
   - Resolution: 1280x720
   - Caption: "Pong"

2. **Game Elements**:
   - Paddles: Represented as rectangles.
   - Ball: Represented as a circle.
   - Center Line: Dotted line in the middle of the screen for aesthetic purposes.

3. **Movement**:
   - Paddles: Controlled using the keyboard.
   - Ball: Moves automatically and bounces off walls and paddles.

4. **Collision Handling**:
   - Ball bounces off the top and bottom walls.
   - Ball direction changes when it collides with a paddle.

5. **Scoring**:
   - Player scores if the ball passes the opponent's paddle.
   - Opponent scores if the ball passes the player's paddle.
   - Scores are displayed at the top of the screen.

6. **Frame Rate**:
   - The game runs at 60 frames per second (FPS).

### Functions:
- `drawDotLine()`: Draws the center dotted line.

### Variables:
- **Player and Opponent Paddles**:
  - Controlled using keyboard inputs.
- **Ball**:
  - Moves automatically and reacts to collisions.
- **Scores**:
  - Keeps track of player and opponent scores.

## Customization
1. **Ball Speed**:
   - Modify `x_speed` and `y_speed` variables to increase or decrease ball speed.
2. **Paddle Speed**:
   - Adjust the values inside the movement conditions for `player` and `opponent`.
3. **Window Size**:
   - Change the `WIDTH` and `HEIGHT` variables to resize the game window.
4. **Font and Aesthetics**:
   - Change the font or colors to personalize the game.

## Known Issues
- Paddles may overlap the top and bottom edges slightly if moved rapidly.
- Ball speed does not gradually increase over time.

## Future Improvements
- Add sound effects for collisions and scoring.
- Implement AI for the opponent paddle.
- Add a main menu and game restart option.
- Introduce a win condition and display a victory screen.



