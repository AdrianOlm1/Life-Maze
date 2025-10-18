import asyncio
import pygame
import random
from collections import deque
import sys
import platform

# Initialize pygame (same as Bubble Trouble - no custom mixer settings)
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
TILE_SIZE = 40

WIDTH = 41  # Must be odd to allow walls and paths properly
HEIGHT = 21

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Sound will be initialized in the main async function
coinsound = None
background_music = None
music_loaded = False

traits = ["compassion", "patience", "kindness", "courage", "empathy", "generosity", "friendship", "loyalty", "dedication", "intelligence"]
random.shuffle(traits)  # Randomize traits so they appear differently each game
trait_index = 0  # Tracks which trait to display

# Load the title screen background image
try:
    title_background = pygame.image.load('Maze/download.jpeg')
    title_background = pygame.transform.scale(title_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
except:
    title_background = None
    print("Background image not available")

# Define maze layout (1: wall, 0: path)
def create_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def carve_path(x, y):
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width-1 and 1 <= ny < height-1 and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[y + dy//2][x + dx//2] = 0
                carve_path(nx, ny)

    maze[1][1] = 0
    carve_path(1, 1)

    return maze

def find_reachable_positions(maze, start_x, start_y):
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    queue = deque([(start_x, start_y)])
    reachable = []

    while queue:
        x, y = queue.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = True
        reachable.append((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 0 and not visited[ny][nx]:
                queue.append((nx, ny))

    return reachable

maze = create_maze(WIDTH, HEIGHT)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze with Vision System")

font = pygame.font.SysFont(None, 55)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE - 2, TILE_SIZE - 2))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vision_radius = 1  # Start with a small vision radius

    def move(self, dx, dy):
        if 0 <= self.rect.left + dx < SCREEN_WIDTH and 0 <= self.rect.top + dy < SCREEN_HEIGHT:
            new_rect = self.rect.move(dx, dy)
            if maze[new_rect.top // TILE_SIZE][new_rect.left // TILE_SIZE] == 0:
                self.rect.move_ip(dx, dy)

    def increase_vision(self):
        self.vision_radius += 1  # Increase vision radius with each collectible

# Collectible class (Green sprites)
class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE - 2, TILE_SIZE - 2))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

player = Player(TILE_SIZE + 1, TILE_SIZE + 1)
player_group = pygame.sprite.Group(player)
collectibles_group = pygame.sprite.Group()

reachable_positions = find_reachable_positions(maze, 1, 1)

for i in range(len(traits)-1):
    if reachable_positions:
        x, y = random.choice(reachable_positions)
        reachable_positions.remove((x, y))
        collectibles_group.add(Collectible(x * TILE_SIZE + 1, y * TILE_SIZE + 1))

def display_title_screen():
    if title_background:
        screen.blit(title_background, (0, 0))
    else:
        screen.fill(BLACK)
    title_font = pygame.font.SysFont(None, 80)
    title_text = title_font.render("Journey of Life", True, WHITE)
    instruction_text = font.render("Press any key to start", True, WHITE)
    screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, SCREEN_HEIGHT//3))
    screen.blit(instruction_text, (SCREEN_WIDTH//2 - instruction_text.get_width()//2, SCREEN_HEIGHT//2))
    pygame.display.flip()

def render_vision(maze, player):
    screen.fill(WHITE)
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            # Only draw tiles within the player's vision radius
            if abs(player.rect.top // TILE_SIZE - row) <= player.vision_radius and abs(player.rect.left // TILE_SIZE - col) <= player.vision_radius:
                if maze[row][col] == 1:
                    pygame.draw.rect(screen, BLACK, pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

async def main():
    """
    Main async game loop for pygbag compatibility
    """
    global trait_index, coinsound, background_music, music_loaded

    # Give browser time to initialize
    await asyncio.sleep(0)

    running = True
    clock = pygame.time.Clock()
    display_message = False
    message = ""
    game_started = False

    # Title screen loop
    display_title_screen()
    waiting_for_key = True

    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_key = False
                running = False
            if event.type == pygame.KEYDOWN:
                waiting_for_key = False
                game_started = True

                # Initialize all sounds AFTER user interaction (required for web browsers)
                if not music_loaded:
                    try:
                        # Load coin sound first
                        coinsound = pygame.mixer.Sound('Maze/sounds/coin.ogg')
                        print(f"Coin sound loaded: {coinsound is not None}")
                    except Exception as e:
                        print(f"Coin sound error: {e}")
                        coinsound = None

                    # Try to load and play background music (use OGG like Bubble Trouble)
                    try:
                        # Use music module for long audio files
                        print("Loading background music...")
                        pygame.mixer.music.load('Maze/sounds/home.ogg')
                        pygame.mixer.music.set_volume(0.6)
                        pygame.mixer.music.play(-1)  # Loop forever (same as Bubble Trouble)
                        music_loaded = True
                        print(f"Background music playing: {pygame.mixer.music.get_busy()}")
                    except Exception as e:
                        print(f"Background music error: {e}")
                        music_loaded = False

        await asyncio.sleep(0)  # Yield control to browser

    # Main game loop
    message_timer = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-TILE_SIZE, 0)
        if keys[pygame.K_RIGHT]:
            player.move(TILE_SIZE, 0)
        if keys[pygame.K_UP]:
            player.move(0, -TILE_SIZE)
        if keys[pygame.K_DOWN]:
            player.move(0, TILE_SIZE)

        collected = pygame.sprite.spritecollide(player, collectibles_group, True)

        if collected and trait_index < len(traits):
            if coinsound:
                coinsound.play()
            player.increase_vision()  # Increase vision radius
            message = f"You've learned {traits[trait_index]}!"
            display_message = True
            message_timer = pygame.time.get_ticks()
            trait_index += 1

            # If all traits are learned, exit the game
            if trait_index == len(traits)-1:
                message = "These are my standards of integrity!"
                display_message = True
                message_timer = pygame.time.get_ticks()
                pygame.time.wait(2000)
                running = False

        if display_message:
            # Check if 1 second has passed
            if pygame.time.get_ticks() - message_timer > 1000:
                display_message = False

            screen.fill(BLACK)
            text = font.render(message, True, WHITE)
            screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))
        else:
            render_vision(maze, player)
            player_group.draw(screen)
            collectibles_group.draw(screen)

        pygame.display.flip()
        clock.tick(10)

        await asyncio.sleep(0)  # Yield control to browser

    pygame.quit()

# Pygbag-compatible entry point
asyncio.run(main())
