# FlapDash

A fun and addictive Flappy Bird-style game built with Python and Pygame. Navigate your randomly-colored bird through obstacles, rack up points, and compete against your high score!

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Mechanics](#game-mechanics)
- [Controls](#controls)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Requirements](#requirements)

## Features

✨ **Random Bird Selection** - Experience different colored birds (blue, green, red, or yellow) on each playthrough

📈 **Progressive Difficulty** - Game becomes increasingly challenging as your score increases, with pipe frequency and speed adjustments at specific milestones (5, 10, 20, 30... up to 100 points)

🎵 **Audio Effects** - Immersive sound design with:
  - Flying/jumping sounds
  - Scoring sounds
  - Death/collision sounds

🏆 **High Score Tracking** - Your best score is automatically saved and persists across game sessions

🎨 **Smooth Animations** - Animated bird wings and seamless background scrolling

## Installation

### Prerequisites

- Python 3.x
- Pygame library

### Setup Steps

1. **Clone or download the project** to your local machine

2. **Install Pygame** if not already installed:
   ```bash
   pip install pygame
   ```

3. **Ensure all required assets are in the project directory:**
   - Images go in `assets/images/`:
     - `bg.png` - Background image
     - `ground.png` - Ground/floor image
     - `pipe.jpg` - Pipe obstacle image
     - `restart1.png` - Restart button
     - `exit.png` - Exit button
     - `play.png` - Play/Start button
     - Bird animation frames:
       - `blue_bird1.png` through `blue_bird4.png`
       - `green_bird1.png` through `green_bird4.png`
       - `red_bird1.png` through `red_bird4.png`
       - `yellow_bird1.png` through `yellow_bird4.png`
   - Sound files go in `assets/sounds/`:
     - `flying_sound.mp3` - Jump sound
     - `score_sound.mp3` - Scoring sound
     - `died_sound.mp3` - Collision/death sound

4. **Run the game from the src directory:**
   ```bash
   cd src
   python main.py
   ```

## How to Play

1. **Start Screen** - Press the play button to begin the game

2. **Gameplay** - Once started, navigate your bird through the pipes:
   - Press **SPACEBAR** to make the bird jump/flap
   - Avoid hitting the pipes and the ground
   - Avoid flying above the screen
   - Each successful passage through pipes earns 1 point

3. **Game Over** - When you hit an obstacle or the ground:
   - Click **Restart** to play again
   - Click **Exit** to quit the game

## Game Mechanics

### Scoring System

- Gain 1 point for successfully passing through each pipe gap
- Your high score is automatically saved to `data/score.text`
- High score persists between game sessions

### Difficulty Scaling

The game automatically increases in difficulty at specific score milestones:

| Score | Speed Increase | Pipe Frequency Change |
|-------|----------------|-----------------------|
| 5     | +0.01          | -2 ms                 |
| 10    | +0.012         | -2 ms                 |
| 20    | +0.014         | -2 ms                 |
| 30    | +0.016         | -3 ms                 |
| 40    | +0.018         | -3 ms                 |
| 50    | +0.020         | -3 ms                 |
| 60    | +0.022         | -4 ms                 |
| 70    | +0.024         | -4 ms                 |
| 80    | +0.026         | -4 ms                 |
| 90    | +0.028         | -5 ms                 |
| 100   | +0.030         | -5 ms                 |

### Pipe Mechanics

- Pipes spawn every 1500ms (adjustable based on difficulty)
- Pipe gap: 150 pixels (adjustable)
- Random vertical offset to keep gameplay varied
- Pipes scroll left and disappear when off-screen

### Bird Physics

- Gravity: 0.5 pixels/frame acceleration downward
- Max falling velocity: 8 pixels/frame
- Jump velocity: -10 pixels/frame
- Bird rotates based on velocity for visual feedback

## Controls

- **SPACEBAR** - Jump/Flap (hold for continuous flapping)
- **MOUSE** - Click buttons (Play, Restart, Exit)
- **X Button** - Close window / Quit game

## Project Structure

```
FlapDash/
├── src/
│   └── main.py                      # Main game executable
├── assets/
│   ├── images/                      # Game graphics
│   │   ├── bg.png
│   │   ├── ground.png
│   │   ├── pipe.jpg
│   │   ├── restart1.png
│   │   ├── exit.png
│   │   ├── play.png
│   │   ├── blue_bird1-4.png
│   │   ├── green_bird1-4.png
│   │   ├── red_bird1-4.png
│   │   └── yellow_bird1-4.png
│   └── sounds/                      # Audio files
│       ├── flying_sound.mp3
│       ├── score_sound.mp3
│       └── died_sound.mp3
├── data/
│   └── score.text                   # High score storage (auto-generated)
├── docs/
│   └── README.md                    # This file
└── README.md                        # Quick reference (root level)
```

## Technical Details

### Classes

**Ibon (Player Character)**
- Inherits from `pygame.sprite.Sprite`
- Manages bird animation, physics, and collision handling
- Supports 4 bird color variants with separate animation frames
- Plays sound on jump action

**Pipe (Obstacles)**
- Inherits from `pygame.sprite.Sprite`
- Creates paired top and bottom pipes
- Automatically scrolls and removes itself when off-screen
- Position parameter determines orientation (1 = top pipe, -1 = bottom pipe)

**Button (UI Elements)**
- Handles button rendering and click detection
- Used for Play, Restart, and Exit buttons
- Returns `True` when clicked

### Game Configuration

- **Screen Resolution**: 855 x 936 pixels
- **FPS**: 60 frames per second
- **Initial Pipe Gap**: 150 pixels
- **Initial Pipe Frequency**: 1500ms
- **Initial Scroll Speed**: 4 pixels/frame
- **Ground Scroll**: 35-pixel cycle for seamless looping

### File I/O

The game automatically reads and writes to `data/score.text` to persist high scores between sessions. If the file doesn't exist or is empty, the high score starts at 0.

## Requirements

- Python 3.6+
- Pygame 2.0+
- All game assets must be organized in `assets/` directory (images and sounds)

## Future Enhancement Ideas

- Add power-ups or special items
- Implement multiple difficulty modes
- Add leaderboard system
- Create additional bird skins
- Add background music
- Implement pause functionality
- Create different game modes (endless, timed challenges, etc.)

## License

Created for educational and entertainment purposes.

---

**Have fun playing FlapDash! 🐦**