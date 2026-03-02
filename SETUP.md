# FlapDash Setup Instructions

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## Step 1: Install Dependencies

From the project root directory, run:

```bash
pip install -r requirements.txt
```

Or install Pygame directly:

```bash
pip install pygame
```

## Step 2: Organize Assets

The project expects assets to be organized in specific directories:

### Images
Place all image files in `assets/images/`:
- `bg.png` - Background
- `ground.png` - Ground/floor
- `pipe.jpg` - Pipe obstacle
- `restart1.png` - Restart button
- `exit.png` - Exit button
- `play.png` - Play button
- `blue_bird1.png` through `blue_bird4.png` - Blue bird animation
- `green_bird1.png` through `green_bird4.png` - Green bird animation
- `red_bird1.png` through `red_bird4.png` - Red bird animation
- `yellow_bird1.png` through `yellow_bird4.png` - Yellow bird animation

### Sounds
Place all audio files in `assets/sounds/`:
- `flying_sound.mp3` - Jump/flap sound
- `score_sound.mp3` - Scoring sound
- `died_sound.mp3` - Collision/death sound

## Step 3: Run the Game

Navigate to the src directory and run:

```bash
cd src
python main.py
```

## Directory Structure After Setup

```
FlapDash/
├── src/
│   └── main.py
├── assets/
│   ├── images/
│   │   ├── bg.png
│   │   ├── ground.png
│   │   ├── pipe.jpg
│   │   ├── restart1.png
│   │   ├── exit.png
│   │   ├── play.png
│   │   ├── blue_bird1.png
│   │   ├── blue_bird2.png
│   │   ├── blue_bird3.png
│   │   ├── blue_bird4.png
│   │   ├── green_bird1.png
│   │   ├── green_bird2.png
│   │   ├── green_bird3.png
│   │   ├── green_bird4.png
│   │   ├── red_bird1.png
│   │   ├── red_bird2.png
│   │   ├── red_bird3.png
│   │   ├── red_bird4.png
│   │   ├── yellow_bird1.png
│   │   ├── yellow_bird2.png
│   │   ├── yellow_bird3.png
│   │   └── yellow_bird4.png
│   └── sounds/
│       ├── flying_sound.mp3
│       ├── score_sound.mp3
│       └── died_sound.mp3
├── data/
│   └── score.text (auto-generated)
├── docs/
│   └── README.md
├── .gitignore
├── requirements.txt
├── SETUP.md (this file)
└── README.md
```

## Troubleshooting

### Missing Asset Files
If you get errors about missing image or sound files:
1. Verify files are in the correct subdirectories under `assets/`
2. Check that file names match exactly (case-sensitive on some systems)
3. Ensure files are readable and not corrupted

### Pygame Not Found
If you get "ImportError: No module named pygame":
1. Verify Pygame is installed: `pip list | grep pygame`
2. Reinstall if needed: `pip install --upgrade pygame`

### Port/Display Issues
If the game window won't open:
1. Ensure you have display capabilities (X11 on Linux, proper display on WSL)
2. Try updating Pygame: `pip install --upgrade pygame`

## Notes

- High scores are automatically saved to `data/score.text`
- The game expects to run from the `src/` directory due to relative asset paths
- All asset files must be in place for the game to run
