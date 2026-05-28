# Life Maze

**A procedurally generated maze game built with Pygame where you collect life traits to reach the end.**

Each playthrough generates a unique maze using recursive backtracking. Navigate through the paths, collect traits like courage, empathy, and kindness scattered throughout, and reach the exit before time runs out.

## Gameplay

- Procedurally generated mazes (41x21 grid) — every run is different
- Collect randomized life traits as you navigate
- Title screen with background art
- Sound effects for pickups and background music

## How It Works

The maze is generated using a **recursive carving algorithm**:
1. Start with a grid of walls
2. Pick a starting cell and carve a path
3. Randomly choose unvisited neighbors and carve connecting passages
4. Repeat until all cells are reachable

This guarantees a solvable maze with no isolated sections.

## Tech Stack

- **Python** + **Pygame** for rendering and game loop
- HTML/JS embed version available for web deployment
- Recursive backtracking for maze generation

## Running Locally

```bash
pip install pygame
python main.py
```

## License

MIT
