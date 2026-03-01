# Music Drop

A small rhythm-key input game built with `pygame`, designed as a step-by-step learning project. That features, key movements and a use of different packages to help us inorderto build games

## Overview

This project is a music rhythm key game, where the objective is simple to hit the keys at the right timing. This packet of steps and games helps to learn the application of differen packages, classes and other different coding methods in order to implement sound and shapes and function like a real game.

## Features

- Four-lane key input gameplay (`D`, `F`, `J`, `K`)
- Falling target notes with timing-based hit detection
- Score and lives system
- Hit sound effect (`sound/check.ogg`)

## Quick Start

### 1) Install dependency

```bash
pip install pygame
```

### 2) Run a step

From the workspace root, run any step file:

```bash
python music_drop/step01.py
python music_drop/step02.py
python music_drop/step03.py
python music_drop/step04.py
python music_drop/main.py
```

## Controls

- `D`, `F`, `J`, `K`: Hit falling targets
- Window close button: Quit game

## Project Structure

- `step01.py` — Create the game window and loop
- `step02.py` — Add basic target rendering and falling motion
- `step03.py` — Add keyboard hit detection
- `step04.py` — Add score, lives and sound effect
- `main.py` — The completed version
- `sound/` — Audio assets

## Learning Goals

- Understand the `event -> update -> draw` game loop pattern
- Practice real-time keyboard input handling
- Manage game state variables such as score and lives
- Integrate and play sound assets with `pygame`

## Images 
<img width="400" height="593" alt="Screenshot 2026-03-01 at 1 12 02 PM" src="https://github.com/user-attachments/assets/67c8bb62-2a89-4e2f-87ea-b36d02e11a8e" />
